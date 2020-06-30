# Doubly Linked List and operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            


    # def length(self):
    #     cur = self.head
    #     total = 0
    #     while cur.next != None:
    #         total += 1
    #         cur = cur.next
    #     return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        print(elems)

    # def get(self, index):
    #     if index >= self.length():
    #         print("Error: 'Get' index out of range.")
    #         return None
    #     cur_idx = 0
    #     cur_node = self.head
    #     while True:
    #         cur_node = cur_node.next
    #         if cur_idx == index:
    #             return cur_node.data
    #         cur_idx += 1

    # def erase(self, index):
    #     if index >= self.length():
    #         print("Error: 'Erase' index out of range.")
    #         return
    #     cur_idx = 0
    #     cur_node = self.head
    #     while True:
    #         last_node = cur_node
    #         cur_node = cur_node.next
    #         if cur_idx == index:
    #             last_node.next = cur_node.next
    #             return
    #         cur_idx += 1


the_list = DoublyLinkedList()

the_list.display()

the_list.prepend(3)
the_list.append(7)
the_list.append(11)
the_list.append(33)
the_list.prepend(1)

the_list.display()
#print("Element at 2nd index:", the_list.get(2))


