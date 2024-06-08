class Node:
  def __init__(self, data):
    self.data=data
    self.next = None
    self.previous = None

class doubleLinkedList:
  length = 0
  head= None
  tail= None
  
  def append(self,Node):
    if self.head== None: #eğer ilk itemse
      self.head = Node # artık bir head var
      self.tail = Node  # son eleman
    else: # eğer head varsa
      self.tail.next = Node # son elmanin sonrasina ekledi 
      Node.previous = self.tail # node öncesine sonu ekledik
      self.tail = Node
  
  def __repr__(self):
    result = ""
    currentNode = self.head
    while currentNode != None:
      result += str(currentNode.data) + " "
      currentNode = currentNode.next

    return result




#test 
  
node1 = Node(0)
node2= Node(1)
node3 = Node(3)


link = doubleLinkedList()
link.append(node1)
link.append(node2)
link.append(node3)

print(link)