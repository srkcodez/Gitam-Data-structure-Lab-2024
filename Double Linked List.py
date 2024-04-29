class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(position):
            temp = temp.next
            if temp is None:
                raise IndexError("The position is out of range")
        new_node.prev = temp.prev
        new_node.next = temp
        if temp.prev:
            temp.prev.next = new_node
        temp.prev = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_ending(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def delete_at_position(self, position):
        if self.head is None:
            return
        temp = self.head
        for i in range(position):
            temp = temp.next
            if temp is None:
                raise IndexError("The position is out of range")
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == self.head:  # If the head is to be deleted
            self.head = temp.next

    def search(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index += 1
        return -1

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


def menu():
    dllist = DoublyLinkedList()
    while True:
        print("\n--- Doubly Linked List Operations Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at Ending")
        print("3. Insert at Position")
        print("4. Delete at Beginning")
        print("5. Delete at Ending")
        print("6. Delete at Position")
        print("7. Search for an Element")
        print("8. Count Nodes")
        print("9. Display List")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to insert at beginning: "))
            dllist.insert_at_beginning(data)
        elif choice == '2':
            data = int(input("Enter data to insert at ending: "))
            dllist.insert_at_ending(data)
        elif choice == '3':
            position = int(input("Enter position to insert: "))
            data = int(input("Enter data to insert: "))
            dllist.insert_at_position(position, data)
        elif choice == '4':
            dllist.delete_at_beginning()
        elif choice == '5':
            dllist.delete_at_ending()
        elif choice == '6':
            position = int(input("Enter position to delete: "))
            dllist.delete_at_position(position)
        elif choice == '7':
            data = int(input("Enter data to search: "))
            result = dllist.search(data)
            if result != -1:
                print(f"Element found at position {result}.")
            else:
                print("Element not found.")
        elif choice == '8':
            print("Total nodes in list:", dllist.count_nodes())
        elif choice == '9':
            print("List elements:", dllist.display())
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    menu()
