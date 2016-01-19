#NODE CLASS
INTERNAL    = 100
CHILD       = 101
COMPLETE    = 102
MAX_ITERNAL_BITMAP = 7
MAX_CHILD_BITMAP = 8

"""
" Node
" 
" description: class for a node in a bitmap binary tree
"""
class Node:
    """
    " __init__()
    " 
    " input: @self, @root_node, @internal_idx, @child_idx
    " output:
    " changes: @self.root_node, @self.internal_idx, @self.child_idx, @self.internal_bitmap, @self.child_bitmap
    "
    " description: Constructor of the class, initializes the variables
    """
    def __init__(self, root_node, internal_idx, child_idx):
        self.root_node = root_node
        self.internal_idx = internal_idx
        self.child_idx = child_idx
        self.initialize_bitmap()

    #WARNING: NOT SAFE FOR STRIDES != 2
    """
    " initialize_bitmap()
    " 
    " input: @self
    " output:
    " changes: @self.internal_bitmap, @self.child_bitmap
    "
    " description: Initializes bitmaps to zero
    """
    def initialize_bitmap(self):
        self.internal_bitmap = [0,0,0,0,0,0,0]
        self.child_bitmap = [0,0,0,0,0,0,0,0]

    """
    " add_result()
    " 
    " input: @self, @position, @result
    " output:
    " changes: @self.internal_bitmap, @self.root_node
    "
    " description: Changes to 1 the @position of the @internal_bitmap and calls the method @add_result_info of @root_node to keep the @result
    """
    def add_result(self, position, result):
        self.internal_bitmap[position] = 1
        self.root_node.add_result_info(result)

    
    """
    " add_child()
    " 
    " input: @self, @position
    " output: @child_node
    " changes: @self.internal_bitmap, @self.root_node
    "
    " description: Changes to 1 the @position of the @child_bitmap and calls the method @add_child_node of @root_node to create a new @child_node
    """
    def add_child (self, position):
        self.child_bitmap[position] = 1
        return self.root_node.add_child_node()
    
    """
    " number_of_ones()
    " 
    " input: @self, @bitmap_id, @position
    " output: @number_of_ones
    " changes: 
    "
    " description: Counts the @number_of_ones before @position in the bitmap indicated by @bitmap_id 
    """
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

    """
    " print_node()
    " 
    " input: @self
    " output: 
    " changes: 
    "
    " description: Prints the node: The idxs and the bitmaps
    """
    def print_node (self):
        print ("["+str(self.internal_idx)+"]", end=" ")
        for i in self.internal_bitmap:
            print (str(i)+"|", end="")
        print ("")
        print ("["+str(self.child_idx)+"]", end=" ")
        for i in self.child_bitmap:
            print (str(i)+"|", end="")
        print ("")
        

"""
" RootNode(Node)
" 
" description: class for the root_node in a bitmap binary tree (extends class Node)
"""
class RootNode(Node):
    """
    " __init__()
    " 
    " input: @self
    " output:
    " changes: @self.root_node, @self.internal_idx, @self.child_idx, @self.internal_bitmap, @self.child_bitmap
    "
    " description: Constructor of the class, initializes the variables. As this is the root_node the Super Constructor is called with idxs = 0
    """
    def __init__(self):
        super(RootNode, self).__init__(self, 0, 0)
        self.initialize_bitmap()
        self.results = []
        self.childs = []

    """
    " add_result_info()
    " 
    " input: @self, @result
    " output: 
    " changes: @self.results
    "
    " description: Adds a result to the @self.results array
    """
    def add_result_info(self, result):
        self.results.append(result)

    """
    " add_child_node()
    " 
    " input: @self
    " output: @child_node
    " changes: @self.childs
    "
    " description: Creates a new node, with the current array sizes as idxs and puts it in the @self.childs array
    """
    def add_child_node(self):
        child = Node(self, len(self.results), len(self.childs))
        self.childs.append(child)
        return child

