"""
Tests the Node class
"""
from LinkedBag.linked_structure import Node,TwoWayNode

"""singly linked structure testing"""
head=None
#Add five nodes to the begining of the linked structure
for count in range(1,6):
    head=Node(count,head)

#Print the contents of the structure
while head!=None:
    print(head.data)
    head=head.next


"""doubly linked structure testing"""
#Create a doubly linked structure with one node
head=TwoWayNode(1)
tail=head
#Add four nodes to the end of the doubly linked structure
for data in range(2,6):
    tail.next=TwoWayNode(data,tail)
    tail=tail.next

#Print the contents of the linked structure in reverse order
prob=tail
while prob! =None:
    print(prob.data)
    prob=prob.previous

