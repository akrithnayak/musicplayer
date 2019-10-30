class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next=next
        self.prev=prev
        self.data=data
    head = None

    def add(self, data):

        new_node = Node(data=data)
        last = self.head
        new_node.next=None

        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return
        while(last.next is not None):
            last=last.next
        last.next=new_node
        new_node.prev=last

# first = Node()
# first.add(2)
# print(first.head.data)
