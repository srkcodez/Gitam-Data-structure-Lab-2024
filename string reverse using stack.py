class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""

    # Push all characters of string to stack
    for char in input_string:
        stack.push(char)

    # Pop all characters from stack and append to reversed_string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

def main():
    input_string = input("Enter a string to reverse: ")
    result = reverse_string(input_string)
    print("Reversed string:", result)

if __name__ == "__main__":
    main()
