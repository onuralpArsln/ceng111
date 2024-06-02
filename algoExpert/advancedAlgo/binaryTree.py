# here is a binary tree that adds integer values to left if they are smaller and right if they are bigger 

# node for tree 


class TreeNode:
    # node has two ends  left is  for smaller value right is for bigger values 
    def __init__(self,data) -> None:
        self.data= data
        self.right = None
        self.left = None 

    def nodeAppend(self,data):


        if data > self.data:
            # eğer data benden büyükse sağa atcam yeni node içinde
            self.right = TreeNode(data)

        else:
            self.left  = TreeNode(data)



class BinaryTree:
    __sortMem=""

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            #eğer ilk node yok ise bir node oluştur 
            self.head = TreeNode(data)

        else:
            currentNode=self.head # başlangıcı currenta aldım
            lastNode = self.head

            while currentNode != None:
                if data > currentNode.data:
                    #eğer data büyükse sağa gidiyoz 
                    lastNode = currentNode
                    currentNode = currentNode.right
                    
                else:
                    #eğer data küçükse sola gidiyoz 
                    lastNode = currentNode
                    currentNode = currentNode.left

            #artık current node boş yani last node göre eklicez 
            # last nodea smart eklme yaptırcaz şimdi
                    
            lastNode.nodeAppend(data) # it auto creates node 


    def selfSorter(self):
        mem=""
        def sortHelper(node, mem):
            if node:
            #recursive bi şekilde en alta gidioz eğer node.left None ise ife girmeyecek 
                sortHelper(node.left, mem)
            # son reccursivede if node false olacağı için daha recursive yemeyecek buraya gelecek
                mem += str(node.data)
            # sol bittiği için sağı cekecek 
                sortHelper(node.right, mem)
        sortHelper(self.head,mem)
        return str(mem)


    def __repr__(self) -> str:
        self.sortMem = ""
        def recursiveHelper(node):
            if node: # if node none so ther is no error by node.left 
                recursiveHelper(node.left)
                self.sortMem += str(node.data) 
                self.sortMem += " "
                recursiveHelper(node.right)
        recursiveHelper(self.head)
        return self.sortMem
                


    

# In-order traversal is one of the basic tree traversal algorithms used to visit and process all the nodes in a binary tree.
def tree_to_sorted_list(node, result):
    if node:
        #recursive bi şekilde en alta gidioz eğer node.left None ise ife girmeyecek 
        tree_to_sorted_list(node.left, result)
        # son reccursivede if node false olacağı için daha recursive yemeyecek buraya gelecek
        result.append(node.data)
        # sol bittiği için sağı cekecek 
        tree_to_sorted_list(node.right, result)
       
   



# tree creator  for test 
import random        
tree = BinaryTree()
for i in range(6):
    tree.append(random.randint(0,100)) 




"""
# Initialize an empty list to store the sorted elements
sorted_list = []

# Convert the binary tree to a sorted list
tree_to_sorted_list(tree.head, sorted_list)

# Print the sorted list
print(sorted_list)
"""

print(tree)

