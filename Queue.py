class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            return " -> ".join(map(str, self.items))
        return "Queue is empty"

def menu():
    queue = Queue()
    while True:
        print("\n--- Queue Operations Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Queue Size")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            print("Dequeued item:", queue.dequeue())
        elif choice == '3':
            print("Front item:", queue.peek())
        elif choice == '4':
            print("Queue contents:", queue.display())
        elif choice == '5':
            print("Queue size:", queue.size())
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    menu()
