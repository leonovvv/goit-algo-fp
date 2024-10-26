class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other_list):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other_list.head

        while a and b:
            if a.value <= b.value:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.value >= current.value:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next is not None and temp.next.value < current.value:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_list

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Example usage
list1 = LinkedList()
list1.append(4)
list1.append(2)
list1.append(5)
list1.append(1)

print("Original List:")
list1.print_list()

print("Reversed List:")
list1.reverse()
list1.print_list()

print("Sorted List:")
list1.insertion_sort()
list1.print_list()

list2 = LinkedList()
list2.append(3)
list2.append(6)

print("Merged Sorted Lists:")
merged_list = list1.sorted_merge(list2)
merged_list.print_list()
