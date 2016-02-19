from node import Node, RootNode, BinaryNode
from math import pow, ceil

#SWITCH LIST
IP     = 0
SUBNET = 1
MAC    = 2
NAME   = 3
DPID   = 4

#Type of search
INTERNAL = 0
CHILDREN = 1


class BinaryTrie:
    """Binary Tree Class, enables ip-lookup for Ryu Openflow
    controller
    """
    switches_network = {}
    root_node = None

    def __init__(self, switch_list):
        """Constructor of the class, calls method to build the tree"""
        self.switch_list_to_switches_network(switch_list)
        print("-- Building Binary Trie (" + str(len(switch_list)) + 
            " Switches")
        self.build_tree()


    def switch_list_to_switches_network(self, switch_list):
        """Ips and subnet to Prefix Table"""
        print("-- Creating Switches Network Array (Prefix Table)")
        switches_network = {}
        for switch in switch_list:
            prefix = self.ip_to_prefix(switch_list[switch][IP], 
            int(switch_list[switch][SUBNET]))
            self.add_prefix_to_table(prefix, switch)

        print("Prefix Table:")
        for ip,id2 in sorted(self.switches_network.items(), 
            key=lambda x:x[1]):
            print("--- ["+ id2 +"] : "+ ip)
        print("\n-- Finished Switches Network Array\n")

    def ip_to_prefix(self, ip, subnet):
        "From ip to binary prefix"
        ip_bin = self.ip_to_bin(ip)
        return self.ip_bin_and_subnet_to_prefix(ip_bin, subnet)


    def ip_to_bin(self, ip):
        """Converts ip in format (x.x.x.x) to binary"""
        return "".join([bin(int(x)+256)[3:] for x in ip.split('.')])


    def ip_bin_and_subnet_to_prefix(self, ip, subnet):
        """Cuts the IP to a prefix according to a subnet"""
        return ip[:subnet]


    def add_prefix_to_table(self, prefix, dpid):
        self.switches_network[prefix] = dpid

    def build_tree(self):
        """Creates the binary trie. 

        Starts by creating the root_node and then enters a recursive 
        algorithm to build the complete tree

        """
        print("--- Creating Root Node")
        self.root_node = BinaryNode()
        self.create_node(self.root_node)
        print("-- Bitmap Tree Built with Success")

    def create_node(self, node, ip = ""):
        """Creates the node, while creating children the method becomes 
        recursive.
        """
        print("--- Building Node (" + ip +")")
        self.check_for_results(node, ip)
        self.check_for_children(node, ip)

    def check_for_results(self, node, ip):
        """Looks in the @self.switches_network for a match with the ip 
        represented by the @node.
        """
        if (ip in self.switches_network):
                self.add_result(ip, node)


    def add_result(self, ip, node):
        """Adds a result to the node"""
        print("----- Adding Result")
        result = self.retrieve_and_delete_result_from_switches_network(ip)
        node.result = result
    

    def retrieve_and_delete_result_from_switches_network(self, ip):
        """retrives result from the switches_network list and deletes 
        the it from the same list
        """
        result = self.switches_network[ip]
        del self.switches_network[ip]
        return result


    def check_for_children(self, node, ip):
        """Goes trough the 2 ips possible for children of this node 
        and calls a method to check if there is in fact a child for 
        that ip, creating an object if there is.
        """
        left_node = self.check_for_child(node, ip + "0")
        if left_node:
            node.left_child = left_node
            self.create_node(left_node, ip + "0")

        right_node = self.check_for_child(node, ip + "1")
        if right_node:
            node.right_child = right_node
            self.create_node(right_node, ip + "1")



    def check_for_child(self,node,ip):
        """Looks in the @self.switches_network for a partial match with 
        the ips represented by the @node.
        
        If there is a partial match it means that this node is a father 
        of the node representing that prefix. A node is created and the 
        algorithm continues in the new node (recursive)
        """
        for network in self.switches_network:
            if network.startswith(ip):
                print("----- Adding Child")
                return BinaryNode()


    def ip_lookup(self, ip):
        """Method respondible for the ip_lookup. Receives an ip and goes
        to the tree until the end, finding the longest prefix match.

        To do that it is called a recursive method, to assure that 
        backtraking is possible 
        """
        ip_bin = self.ip_to_bin(ip)
        print("\n\nLookup of IP "+ ip +" (binary: "+ ip_bin + ")")

        result = self.next_child(self.root_node, ip_bin, 0)

        print ("\n\nSearch ended!\nResult: "+ result)
        return result


    def next_child(self, node, ip, i):
        """Recursive method that goes until the last correspondent node
        of the trie.
        The i represents the current level of the trie

        The function returns None while there is no matching result and
        returns the result already obtained after arriving to the
        longest prefix match
        """
        result = None
        next_node = None
        if (ip[i] == "0"):
            if node.left_child:
                next_node = node.left_child
        elif (ip[i] == "1"):
            if node.right_child:
                next_node = node.right_child
        
        if next_node:       
            result = self.next_child(next_node, ip, i+1)

        if result:
            return result
        else:
            return node.result



class BitmapTree(BinaryTrie):
    """Bitmap Tree Class, enables ip-lookup for Ryu Openflow controler"""
    stride = 2
    
    def __init__(self, switch_list, stride = 2):
        """Constructor of the class, calls method to build the tree"""
        self.stride = stride
        self.switch_list_to_switches_network(switch_list)
        print("-- Building Bitmap Tree (stride = "+ str(self.stride)
            + ") with " + str(len(switch_list)) +" Switches")
        self.build_tree()


    def build_tree(self):
        """Creates the bitmap tree. 

        Starts by creating the root_node and then enters a recursive 
        algorithm to build the complete tree

        """
        print("--- Creating Root Node")
        self.root_node = RootNode(self.stride)
        self.create_node(self.root_node)
        print("-- Bitmap Tree Built with Success")


    def create_node(self, node, ip = ""):
        """Creates the node, while creating children the method becomes 
        recursive.
        
        Before checking for internal results and children, the idxs are 
        set to the next position available in each array
        """
        print("--- Building Node")
        node.update_idx(self.root_node)
        self.check_for_internal_results(node, ip)
        self.check_for_children(node, ip)


    def check_for_internal_results(self, node, ip):
        """Looks in the @self.switches_network for a match with the ips 
        represented by the @node.

        If there is a match it means that this node is representing that 
        prefix. So this prefix result is added to the internal bitmap 
        of that node and to the list of results.
        """
        print("---- Building Internal Bitmap")
        actual_ip = ""
        for actual_idx in range(0, Node.max_nodes_in_node(self.stride, 
            INTERNAL)):
            complete_ip = ip + actual_ip
            if (complete_ip in self.switches_network):
                self.add_result(actual_idx, complete_ip, node)
            actual_ip = self.next_ip(actual_ip)
        print("---- Finish Internal Bitmap")


    def add_result(self, idx, ip, node):
        """Adds a result to the node"""
        print("----- Adding Result")
        result = self.retrieve_and_delete_result_from_switches_network(ip)
        node.add_result(idx, result, self.root_node)
        print("------ ["+ str(idx) +"] : "+ result)


    def check_for_children(self, node, ip):
        """Goes trough all the ips possible for children of this node 
        and calls a method to check if there is in fact a child for 
        that ip, creating an object if there is.

        Loops the list of children created and creates the node(fills 
        the object previously created) for each one (in this fase the 
        function becames recursive - Each child will create all it's 
        children before returning )
        """
        print("---- Building Child Bitmap")
        i = self.zero_in_binary()
        children_nodes = []
        children_ip = {}
        child_node = None
        for position in range(0, Node.max_nodes_in_node(self.stride, 
            CHILDREN)):
            complete_ip = ip + i
            child_node = self.check_for_child(node,complete_ip, position)
            if child_node:
                children_nodes.append(child_node)
                children_ip[children_nodes[-1]] = complete_ip
                child_node = None
            i = self.next_ip(i)
        print("---- Finish Child Bitmap")
        for child_node in children_nodes:
            self.create_node(child_node, children_ip[child_node])


    def zero_in_binary(self):
        """Return, depending on the stride, the correct binary for 0"""
        return "".join(["0" for x in range(0, self.stride +1)])


    def check_for_child(self,node,ip, position):
        """Looks in the @self.switches_network for a partial match with 
        the ips represented by the @node.
        
        If there is a partial match it means that this node is a father 
        of the node representing that prefix. A node is created and the 
        algorithm continues in the new node (recursive)
        """
        for network in self.switches_network:
            if network.startswith(ip):
                print("----- Adding Child")
                print("------ ["+ str(position) +"] : "+ ip)
                return node.add_child (position, self.root_node)


    def next_ip(self, actual_ip):
        """Small method to get the next ip to go to trough the tree in 
        the bitmap style (like a snake). ->Used for internal search
        
        If there is no change in the number of bits represented it 
        works as a simple sum of 1. -> Used for children search
        """
        if (actual_ip == ""):
            return "0"
        last_idx = len(actual_ip) - 1
        last_char = actual_ip[last_idx]
        if (last_char == "0"):
            return actual_ip[:last_idx] + "1"
        elif (last_char == "1"):
            for i in range (last_idx - 1, -1, -1):
                if(actual_ip[i] == "0"):
                    return actual_ip[:i] + "1" + "".join("0" for x in range (i
                        , last_idx))
            return "".join("0" for x in range (last_idx + 2))


    def ip_lookup(self, ip):
        """Method respondible for the ip_lookup. Receives an ip and goes
        to the tree until the end, finding the longest prefix match.

        Searches if there is a child and them gets, if possible, the
        result correspondent to the longest match (until now).
        Goes to next node, if it was found, or stops the search
        returning the last result obtained.
        """
        ip_bin = self.ip_to_bin(ip)
        print("\n\nLookup of IP "+ ip +" (binary: "+ ip_bin + ")")

        max_lookup_depth = self.max_lookup_depth(ip_bin)
        next_node = self.root_node

        for lookup_depth in range(0,max_lookup_depth):
            short_ip = ip_bin[lookup_depth*(self.stride +1):(lookup_depth+1)*(
                self.stride +1)]

            child_pointer = self.lookup_child(next_node, short_ip)
            internal_pointer = self.lookup_internal(next_node, short_ip)

            if internal_pointer is not None:
                print ("Found result in "+ str(internal_pointer))
                result = internal_pointer

            if child_pointer is not None:
                print ("Found child in "+ str(child_pointer))
                next_node = self.root_node.children[child_pointer]
            else:
                break

        result = self.root_node.results[result]
        print ("\n\nSearch ended!\nResult: "+ result)
        return result

    def max_lookup_depth(self,ip_bin):
        """Returns the maximum number of node levels may need to be
        visited.

        One node with stide x has the correspondent to x+1 levels of
        binary tree nodes.
        """
        return int(ceil(len(ip_bin)/(self.stride +1)))


    def lookup_child(self, node, ip):
        """Search for an exact match in the child bitmap"""
        position = int(ip, 2)
        if node.child_bitmap[position]:
            return node.child_idx + node.number_of_ones(CHILDREN, position)
        else: 
            return None

    def lookup_internal(self, node, ip):
        """Does a loop in the internal bitmap until a result is found or
        all possible nodes have been searched.

        The ip is decreased in one bit in each loop so the longest match
        is the one found first.
        """
        while True:
            ip = ip[:(len(ip)-1)]
            if ip == '':
                position = 0
            else:
                position = self.ip_to_internal_bitmap_position(ip)
            if node.internal_bitmap[position]:
                return node.internal_idx + node.number_of_ones(INTERNAL, 
                    position)
            if len(ip) == 0:
                return None

    @staticmethod
    def ip_to_internal_bitmap_position(ip):
        """Returns the position on the internal bitmap based on the ip.

        The power of the number of bits gives the number of nodes in the
        current level of the correspondent binary tree. This -1 gives
        the number of nodes in the levels before.
        Then we just add the number to get the correct node.
        """
        return int (pow(2, len(ip)) - 1 + int(ip, 2))