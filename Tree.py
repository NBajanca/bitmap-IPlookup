from math import pow

#NODE CLASS
INTERNAL    = 100
CHILD       = 101
COMPLETE    = 102
MAX_ITERNAL_BITMAP = 7
MAX_CHILD_BITMAP = 8

#SWITCH LIST
IP     = 0
SUBNET = 1
MAC    = 2
NAME   = 3
DPID   = 4

class BitmapTree:
    def __init__(self, switch_list, stride):
        print("-- Building Bitmap Tree (stride = "+ str(stride) +") with "+ str(len(switch_list)) +" Switches")
        self.switch_list = switch_list
        self.stride = stride
        self.switch_list_to_switches_network()
        print("--- Creating Root Node")
        self.root_node = RootNode()
        self.create_node(self.root_node,"")
        print("-- Bitmap Tree Built with Success")

    def switch_list_to_switches_network(self):
        print("--- Creating Switches Network Array (Prefix Table)")
        self.switches_network = {}
        i = 0
        for switch in self.switch_list:
            ip_network = "".join([bin(int(x)+256)[3:] for x in switch.split('.')])
            ip_network = ip_network[:int(self.switch_list[switch][SUBNET])]
            self.switches_network[ip_network] = switch
            print("---- ["+ self.switches_network[ip_network] +"] : "+ip_network)

    def create_node(self, node, ip):
        print("---- Building Node")
        self.check_for_internal_results(node, ip)
        self.check_for_childrens(node, ip)

    def check_for_internal_results(self, node, ip):
        print("----- Building Internal Bitmap")
        max_ip = bin(int(pow(2, self.stride))-1)[2:]
        actual_idx = 0
        actual_ip = ""
        while 1:
            complete_ip = ip+actual_ip
            if (complete_ip in self.switches_network):
                print("------ Adding Result")
                result = self.switches_network[ip+actual_ip]
                del self.switches_network[ip+actual_ip]
                print("------- ["+ str(actual_idx) +"] : "+ result)
                node.add_result(actual_idx, result)
            if actual_ip == max_ip:
                break
            else:
                actual_ip = self.next_ip(actual_ip)
                actual_idx +=1
        print("----- Finish Internal Bitmap")

    #NOT SAFE FOR DIFERENT STRIDES
    def check_for_childrens(self, node, ip):
        print("----- Building Child Bitmap")
        i = "000"
        j = 0
        while i != "111":
            self.check_for_child(node,ip + i, j)
            i= self.next_ip(i)
            j +=1
        print("----- Finish Child Bitmap")

    def check_for_child(self,node,ip, position):
        for network in self.switches_network:
            if network.startswith(ip):
                print("------ Adding Child")
                print("------- ["+ str(position) +"] : "+ ip)
                child_node = node.add_child (position)
                self.create_node(child_node, ip)
                return
        

    def next_ip(self, actual_ip):
        if (actual_ip == ""):
            return "0"
        last_idx = len(actual_ip) - 1
        last_char = actual_ip[last_idx]
        if (last_char == "0"):
            return actual_ip[:last_idx] + "1"
        elif (last_char == "1"):
            for i in range (last_idx - 1, -1, -1):
                if(actual_ip[i] == "0"):
                    return actual_ip[:i] + "1" + "".join("0" for x in range (i, last_idx))
            return "".join("0" for x in range (last_idx + 2))

class Node:
    def __init__(self, root_node, internal_idx, child_idx):
        self.root_node = root_node
        self.internal_idx = internal_idx
        self.child_idx = child_idx
        self.initialize_bitmap()

    #NOT SAFE FOR DIFERENT STRIDES
    def initialize_bitmap(self):
        self.internal_bitmap = [0,0,0,0,0,0,0]
        self.child_bitmap = [0,0,0,0,0,0,0,0]

    def add_result(self, position, result):
        self.internal_bitmap[position] = 1
        self.root_node.add_result_info(result)

    def add_child (self, position):
        self.child_bitmap[position] = 1
        return self.root_node.add_child_node()
        
    def number_of_ones(self, bitmap_id, position):
        number_of_ones = 0
        if (bitmap_id == INTERNAL):
            if (position == COMPLETE):
                position = MAX_INTERNAL_BITMAP
            for i in range(0, position - 1):
                if (self.internal_bitmap[i] == 1):
                    number_of_ones +=1
        elif (bitmap_id == CHILD):
            if (position == COMPLETE):
                position = MAX_CHILD_BITMAP
            for i in range(0, position - 1):
                if (self.child_bitmap[i] == 1):
                    number_of_ones +=1
        return number_of_ones
        


class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__(self, 0, 0)
        self.initialize_bitmap()
        self.results = []
        self.childs = []

    def add_child_node(self):
        child = Node(self, len(self.results), len(self.childs))
        self.childs.append(child)
        return child

    def add_result_info(self, result):
        self.results.append(result)
        

def print_node (node):
    print ("["+str(node.internal_idx)+"]", end=" ")
    for i in node.internal_bitmap:
        print (str(i)+"|", end="")
    print ("")
    print ("["+str(node.child_idx)+"]", end=" ")
    for i in node.child_bitmap:
        print (str(i)+"|", end="")
    print ("")

def print_tree(tree):
    print("\n\nPRINTING TREE\n--ROOT NODE")
    print_node(tree.root_node)
    i=0
    for node in tree.root_node.childs:
        print("\n--NODE "+str(i))
        print_node(node)
        i+=1

    print("\n\n--RESULTS")
    i=0
    for result in tree.root_node.results:
        print("["+str(i)+"] "+result)
        i+=1                
        
        
#Example used in the first meating
switch_list = {}
switch_list["195.0.0.254"  ] = ["195.0.0.254","8" ,"00:00:00:11:11:01","s1","1"] 
switch_list["128.128.0.254"] = ["128.128.0.254","8","00:00:00:11:11:02","s2","2"] 
switch_list["154.128.0.254"] = ["154.128.0.254","8","00:00:00:11:11:03","s3","3"] 
switch_list["197.160.0.254"] = ["197.160.0.254","8","00:00:00:11:11:04","s4","4"] 
tree = BitmapTree(switch_list, 2)
print_tree(tree)
