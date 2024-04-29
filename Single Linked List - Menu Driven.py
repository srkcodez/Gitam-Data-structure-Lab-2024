class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(position - 1):
            if temp is None:
                raise IndexError("The position is out of the range")
            temp = temp.next
        if temp is None:
            raise IndexError("The position is out of the range")
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_at_ending(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while (second_last.next.next):
            second_last = second_last.next
        second_last.next = None

    def delete_at_position(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                raise IndexError("The position is out of the range")
        if temp.next is None:
            raise IndexError("The position is out of the range")
        temp.next = temp.next.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

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
    llist = LinkedList()
    while True:
        print("\n--- Linked List Operations Menu ---")
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
            llist.insert_at_beginning(data)
        elif choice == '2':
            data = int(input("Enter data to insert at ending: "))
            llist.insert_at_ending(data)
        elif choice == '3':
            position = int(input("Enter position to insert: "))
            data = int(input("Enter data to insert: "))
            llist.insert_at_position(position, data)
        elif choice == '4':
            llist.delete_at_beginning()
        elif choice == '5':
            llist.delete_at_ending()
        elif choice == '6':
            position = int(input("Enter position to delete: "))
            llist.delete_at_position(position)
        elif choice == '7':
            data = int(input("Enter data to search: "))
            found = llist.search(data)
            print("Element found!" if found else "Element not found.")
        elif choice == '8':
            print("Total nodes in list:", llist.count_nodes())
        elif choice == '9':
            print("List elements:", llist.display())
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    menu()
