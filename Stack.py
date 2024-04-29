class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def display(self):
        if not self.is_empty():
            return " -> ".join(map(str, reversed(self.items)))
        return "Stack is empty"

def menu():
    stack = Stack()
    while True:
        print("\n--- Stack Operations Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == '2':
            print("Popped item:", stack.pop())
        elif choice == '3':
            print("Top item:", stack.peek())
        elif choice == '4':
            print("Stack contents:", stack.display())
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    menu()
