# Initialize an empty list to represent the stack
stack = []

# Function to check if the stack is empty
def is_empty():
    return len(stack) == 0

# Function to push an element onto the stack
def push(item):
    stack.append(item)
    print(f"Pushed {item} onto the stack")

# Function to pop the top element from the stack
def pop():
    if is_empty():
        return "Stack is empty"
    return stack.pop()

# Function to peek at the top element of the stack
def peek():
    if is_empty():
        return "Stack is empty"
    return stack[-1]

# Function to display the current elements in the stack
def display():
    if is_empty():
        print("Stack is empty")
    else:
        print("Stack contents:", stack)


while True:
    print("**** STACK DEMONSTRATION ******")
    print("1. PUSH ")
    print("2. POP")
    print("3. PEEK")
    print("4. SHOW STACK ")
    print("0. EXIT")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        val = int(input("Enter Item to Push: "))
        push(stack, val)
    
    elif ch == 2:
        val = pop(stack)
        if val == "Underflow":
            print("Stack is Empty")
        else:
            print("\nDeleted Item was:", val)
    
    elif ch == 3:
        val = peek(stack)
        if val == "Underflow":
            print("Stack Empty")
        else:
            print("Top Item:", val)
    
    elif ch == 4:
        display(stack)
    
    elif ch == 0:
        print("Bye")
        break

    else:
        print("Invalid Choice, try again.")

