class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node()
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: Insert a new node & count
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.count += 1

    def display(self):
        # TODO: Shows the elements in the list
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
            print(cur_node)                   # Showing the data address for each elements
        print(elems)

    def find(self, data):
        # TODO: Find the first-item with a given value
        item = self.head
        while item != None:
            if item.get_data() == data:
                return item
            else:
                item = item.get_next()

    def erase(self, index):
        # TODO: Delete an item at given index
        if index > self.count:
            print("ERROR: 'Erase' index out of range.")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            print(cur_node, cur_idx)             # Current node, index of each iteration
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:                 # when match the Respective index, which intend to delete
                prev_node.next = cur_node.next   # Biasing the pointer to next node            
                cur_node = None                  # Assign the node's pointer to none, it can't be accessed
                self.count -= 1
                break
            cur_idx += 1


# Create a linked list
theList = LinkedList()
theList.display()

# Insert some items
theList.insert(1)
theList.insert(3)
theList.insert(7)
theList.insert(11)
theList.insert(33)

print("Item count:", theList.get_count())
print("Finding item:", theList.find(7))
theList.display()

theList.erase(2)
print("Finding item:", theList.find(7))
print("Item count:", theList.get_count())
theList.display()