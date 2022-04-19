import sys
class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree (object):
    def __init__ (self):
        self.root = None

    # insert values into tree
    def insert (self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lChild
                else:
                    current = current.rChild

            if (val < parent.data):
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        
        def helper(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2
            if node1.data != node2.data:
                return False
            return helper(node1.lChild, node2.lChild) and helper(node1.rChild, node2.rChild)
        
        return helper(self.root, pNode.root)

    # Returns a list of nodes at a given level from lChild to rChild
    def get_level (self, level):
        
        def helper(node, level, result):
            if not node:
                return 
            if level == 0:
                result.append(node)
                return
            
            helper(node.lChild, level - 1, result)
            helper(node.rChild, level - 1, result)
        
        ret = []
        helper(self.root, level, ret)
        return ret

    # Returns the height of the tree
    def get_height (self): 
        
        def helper(node):
            if not node:
                return 0
            return max(helper(node.lChild), helper(node.rChild)) + 1
        
        return helper(self.root) - 1
    # Returns the number of nodes in the lChild subtree and
    # the number of nodes in the rChild subtree and the root
    def num_nodes (self):
        def helper(node):
            if not node:
                return 0
            lChild, rChild = helper(node.lChild), helper(node.rChild)
            return lChild + rChild + 1
        
        return helper(self.root)

def main():
    # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()