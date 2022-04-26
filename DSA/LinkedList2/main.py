
# defining node object
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def insert_front(self, data):
        # define new node
        new_node = Node(data)
        # set the second node to equal the old first node
        new_node.set_next(self.head)
        # the new head will be the new node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        head_node = self.head

        if head_node is None:
            head_node = new_node
            return

        # otherwise, lets find the last node
        last_node = head_node

        # as long as there is a next node it means we haven't reached the end
        while last_node.get_next() is not None:
            last_node = last_node.get_next()

        last_node.set_next(new_node)
        self.end = new_node





ll = LinkedList()
ll.insert_front(35)
ll.insert_front(37)
ll.insert_front(52)