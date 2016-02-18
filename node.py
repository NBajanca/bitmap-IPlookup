#Type of search
INTERNAL = 0
CHILDREN = 1


class Node:
    """Class for a node in a bitmap binary tree """
    internal_idx = 0
    child_idx = 0
    internal_bitmap = []
    child_bitmap = []


    def __init__(self, internal_idx = 0, child_idx = 0, stride = 2):
        """Constructor of the class, initializes the variables

        Initialized for root_node - For other nodes it is updated 
        during children discovery
        """
        self.internal_idx = internal_idx
        self.child_idx = child_idx
        self.initialize_bitmap(stride)


    def initialize_bitmap(self, stride):
        """Initializes bitmaps to zero"""
        self.internal_bitmap = []
        self.child_bitmap = []
        for i in range(0,self.max_nodes_in_node(stride)):
            self.internal_bitmap.append(0)
            self.child_bitmap.append(0)
        self.child_bitmap.append(0)


    @staticmethod
    def max_nodes_in_node(stride, type_of_search = INTERNAL):
        """Defines max number of binary trie nodes inside a bitmapTree

        Can also be used to know the number of binary trie nodes that 
        are children of a bitmapTree node
        """
        if type_of_search is INTERNAL:
            return int(pow(2, stride +1) - 1)
        else:
            return int(pow(2, stride +1))


    def add_result(self, position, result, root_node):
        """Changes to 1 the @position of the @internal_bitmap and calls 
        the method @add_result_info of @root_node to keep the @result
        """
        self.internal_bitmap[position] = 1
        root_node.add_result_info(result)


    def update_idx(self, root_node):
        """Updates the idxs so they match the next position in the 
        respective arrays"""
        self.child_idx = len(root_node.children)
        self.internal_idx = len(root_node.results)


    def add_child(self, position, root_node):
        """Changes to 1 the @position of the @child_bitmap and calls 
        the method @add_child_node of @root_node to create a new 
        @child_node
        """
        self.child_bitmap[position] = 1
        return root_node.add_child_node()
    

    def number_of_ones(self, bitmap_id, position):
        """Counts the @number_of_ones before @position in the bitmap 
        indicated by @bitmap_id 
        """
        number_of_ones = 0
        if (bitmap_id == INTERNAL):
            for i in range(0, position):
                if (self.internal_bitmap[i] == 1):
                    number_of_ones +=1
        elif (bitmap_id == CHILDREN):
            for i in range(0, position):
                if (self.child_bitmap[i] == 1):
                    number_of_ones +=1
        return number_of_ones
        

class RootNode(Node):
    """class for the root_node in a bitmap binary tree (extends Node)"""
    results = []
    children = []
    stride = 2


    def __init__(self, stride = 2):
        """Constructor of the class, initializes the variables"""
        Node.__init__(self, stride = stride)
        self.stride = stride


    def add_result_info(self, result):
        """Adds a result to the @self.results array"""
        self.results.append(result)


    def add_child_node(self):
        """Creates a new node, with the current array sizes as idxs and 
        puts it in the @self.children array
        """
        child = Node(stride = self.stride)
        self.children.append(child)
        return child

