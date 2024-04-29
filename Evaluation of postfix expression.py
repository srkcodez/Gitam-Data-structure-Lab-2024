class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0

def evaluate_postfix(expression):
    stack = Stack()

    for char in expression:
        if char.isdigit():  # Check if the character is a digit
            stack.push(int(char))  # Push it to the stack as an integer
        else:
            # Pop the two top items from the stack for the operation
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)

    # The result is the only item left in the stack
    return stack.pop()

def main():
    postfix_expression = input("Enter a postfix expression (each token separated by spaces): ")
    # Splitting for better handling of multi-digit numbers and spaces
    postfix_tokens = postfix_expression.split()
    result = evaluate_postfix(postfix_tokens)
    print("The result of the postfix evaluation is:", result)

if __name__ == "__main__":
    main()
