class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        print(curr_node)


    def print_inline(self):
        if self.head is None:
            print("List is empty")
            return

        curr_node = self.head
        llstr = ''

        while curr_node:
            llstr += str(curr_node.data) + " --> "
            curr_node = curr_node.next

        print(llstr)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(4)
llist1.append(5)

llist1.print_list()
llist1.print_inline()