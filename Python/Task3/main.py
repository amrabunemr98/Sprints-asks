def is_balanced(s):
    # This function checks if a given string of brackets is balanced.

    # Create a stack to store the open brackets.
    stack = []

    # Iterate over the string.
    for c in s:

        # If the current character is an open bracket, push it onto the stack.
        if c == '(' or c == '[' or c == '{':
            stack.append(c)

        # If the current character is a closing bracket, pop the top element off the stack.
        # If the top element is not the matching open bracket, return False.
        elif c == ')' and (not stack or stack[-1] != '('):
            return False
        elif c == ']' and (not stack or stack[-1] != '['):
            return False
        elif c == '}' and (not stack or stack[-1] != '{'):
            return False

        # If the current character is not an open or closing bracket, pop the top element off the stack.
        else:
            stack.pop()

    # If the stack is empty, the brackets are balanced. Otherwise, they are not balanced.
    return not stack


# Get the input from the user.
s = input("Please Enter Brackets: ")

# Check if the brackets are balanced.
if is_balanced(s):
    # The brackets are balanced.
    print("Yes,Balanced Brackets")
else:
    # The brackets are not balanced.
    print("No,Not Balanced Brackets")
