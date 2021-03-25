class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''

        if not isinstance(x, Node):
            x = Node(x)

        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x


    def __str__(self):
        # [5->4->10->1]
        to_print = ""
        # iterate through list
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next

        if to_print:
            return "[" + to_print[:-2] + "]"
        else:
           return "[]0"


    def add_to_start(self, x):
        '''add x to the left of the list making it the head'''

        if not isinstance(x, Node):
            x = Node(x)

        if self.head is None:
            self.head = x
            x.next = None
        else:
            x.next = self.head
            self.head = x

    def search_val(self, x):
        '''return indices where x was found'''
        curr = self.head
        index = 0
        foundIndicesList = []
        while curr is not None:
            if curr.data == x:
                foundIndicesList.append(index)
            curr = curr.next
            index += 1

        return foundIndicesList


    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        curr = self.head
        prev = self.head
        index = 0
        while curr is not None:
            if index == x:
                prev.next = curr.next

            if index > 1:
                prev = prev.next

            curr = curr.next
            index += 1

    def length(self):
        '''return the length of the list, rep'd by the number of nodes'''
        curr = self.head
        index = 0
        foundIndicesList = []
        while curr is not None:
            curr = curr.next
            index += 1
        return index

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        # Given [1->2->3->4->5] reverse pointers [5->4->3->2->1]

        # Empty list
        if self.head == None:
            return
        elif current.next == None:
            # Base case is when we have reached the end of the list
            self.tail = self.head
            current.next = previous.next
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recur(next, current)


node1 = Node(4)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
# print(node1)

my_list = LinkedList()
# my_list.append_val(node1)
# my_list.append_val(node2)
# my_list.append_val(node3)
# my_list.append_val(node4)
# my_list.append_val(node5)
# my_list.append_val(10)
# my_list.add_to_start(8)
# print(my_list)

# searchList = my_list.search_val(4)
# print("4 is found at ", searchList)
#
# print("Length of my_list", my_list.length())

my_list.append_val(1)
my_list.append_val(2)
my_list.append_val(3)
my_list.append_val(4)
my_list.append_val(5)
#
# my_list.remove_val_by_index(3)
print(my_list)

my_list.reverse_list_recur(my_list.head, None)
print(my_list)



# my_empty_list = LinkedList()
# my_empty_list.add_to_start(6)
# print(my_empty_list)