class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def add_to_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete_node(self, key):
        if self.head:
            if self.head.data == key and self.head.next == self.head:
                self.head = None  # Deleting the only node in the list
            elif self.head.data == key:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            else:
                curr = self.head
                prev = None
                while curr.next != self.head:
                    prev = curr
                    curr = curr.next
                    if curr.data == key:
                        prev.next = curr.next
                        break

    def display(self):
        if not self.head:
            return "List is empty"
        result = []
        temp = self.head
        while True:
            result.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return " -> ".join(map(str, result))

def menu():
    clist = CircularLinkedList()
    while True:
        print("\n--- Circular Singly Linked List Menu ---")
        print("1. Add Node to End")
        print("2. Add Node to Beginning")
        print("3. Delete Node")
        print("4. Display List")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            data = int(input("Enter data to add to end: "))
            clist.add_to_end(data)
        elif choice == '2':
            data = int(input("Enter data to add to beginning: "))
            clist.add_to_beginning(data)
        elif choice == '3':
            data = int(input("Enter data of the node to delete: "))
            clist.delete_node(data)
        elif choice == '4':
            print("Current List: ", clist.display())
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    menu()
