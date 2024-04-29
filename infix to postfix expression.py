def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []  # to keep operators
    postfix = []  # to build the output expression
    for char in expression:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:  # the character is an operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) <= precedence.get(char, 0)):
                postfix.append(stack.pop())
            stack.append(char)

    # pop all the operators in the stack
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

def main():
    # Get input from the user
    expression = input("Enter an infix expression: ")
    # Remove spaces to simplify parsing, in case they enter spaces
    expression = expression.replace(" ", "")
    # Convert the infix expression to postfix
    postfix_expression = infix_to_postfix(expression)
    # Print the result
    print("Postfix expression:", postfix_expression)

if __name__ == "__main__":
    main()
