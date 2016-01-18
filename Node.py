INTERNAL    = 100
CHILD       = 101
COMPLETE    = 102

MAX_ITERNAL_BITMAP = 7
MAX_CHILD_BITMAP = 8

class Node:
    def __init__(self, root_node, internal_idx, child_idx):
        self.root_node = root_node
        self.internal_idx = internal_idx
        self.child_idx = child_idx
        self.initialize_bitmap()

    def initialize_bitmap(self):
        self.internal_bitmap = [0,0,0,0,0,0,0]
        self.child_bitmap = [0,0,0,0,0,0,0,0]

    def add_result(self, position, result):
        self.internal_bitmap[position] = 1
        root_node.add_result_info(result)

    def add_child (self, position):
        self.child_bitmap[position] = 1
        return root_node.add_child_node()
        
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
        self.internal_idx = 0
        self.child_idx = 0
        self.initialize_bitmap()
        self.results = []
        self.childs = []

    def add_child_node(self):
        child = Node(self, len(self.results), len(self.childs))
        self.childs.append(child)
        return child

    def add_result_info(self, result):
        self.results.append(result)