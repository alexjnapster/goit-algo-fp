class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node()
        tail = dummy
        l1 = self.head
        l2 = other.head

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        self.head = dummy.next

    def insertion_sort(self):
        sorted_list = LinkedList()

        current = self.head
        while current:
            next_node = current.next
            sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list.head

def sorted_insert(sorted_list: LinkedList, new_node: Node):
    if sorted_list.head is None or sorted_list.head.data >= new_node.data:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node


# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(3)
llist1.insert_at_end(5)
llist1.insert_at_end(8)

llist2 = LinkedList()
llist2.insert_at_end(1)
llist2.insert_at_end(7)
llist2.insert_at_end(10)

print("Перший список:")
llist1.print_list()

print("Другий список:")
llist2.print_list()

# Об'єднання двох списків
llist1.sorted_merge(llist2)
print("Об'єднаний відсортований список:")
llist1.print_list()

# Реверсування списку
llist1.reverse()
print("Реверсований список:")
llist1.print_list()

# Сортування списку
llist1.insertion_sort()
print("Відсортований список:")
llist1.print_list()