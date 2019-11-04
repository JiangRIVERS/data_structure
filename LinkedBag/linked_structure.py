#定义一个单链表节点类
class Node:
    """Represents a singly linked node"""

    def __init__(self,data,next=None):
        """Instantiates a Node with a default next of None"""
        self.data=data
        self.next=next

class TwoWayNode(Node):
    """Represents a doubly linked node"""
    def __init__(self,data,previous=None,next=None):
        """Instantiates a TwoWayNode"""
        Node.__init__(self,data,next=next)
        self.previous=previous







#if __name__=='__main__':
    #Just an empty link
   # node1=None
    #A node containing data and an empty link
   # node2=Node("A",None)
    #A node containing adata and a link to node2
  #  node3=Node("B",node2)






















































