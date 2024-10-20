# Initialize an empty list to represent the queue
queue = []

# Function to check if the queue is empty
def is_empty():
    return len(queue) == 0

# Function to add an element to the end of the queue
def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item} to the queue")

# Function to remove and return the front element of the queue
def dequeue():
    if is_empty():
        return "Queue is empty"
    return queue.pop(0)

# Function to peek at the front element of the queue
def peek():
    if is_empty():
        return "Queue is empty"
    return queue[0]

# Function to display the current elements in the queue
def display():
    if is_empty():
        print("Queue is empty")
    else:
        print("Queue contents:", queue)

# User interaction loop
while True:
    print("\n**** QUEUE DEMONSTRATION ******")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. PEEK")
    print("4. SHOW QUEUE")
    print("0. EXIT")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        val = int(input("Enter Item to Enqueue: "))
        enqueue(val)
    
    elif choice == 2:
        val = dequeue()
        if val == "Queue is empty":
            print(val)
        else:
            print("\nDequeued Item was:", val)
    
    elif choice == 3:
        val = peek()
        if val == "Queue is empty":
            print(val)
        else:
            print("Front Item:", val)
    
    elif choice == 4:
        display()
    
    elif choice == 0:
        print("Goodbye!")
        break
    
    else:
        print("Invalid Choice, please try again.")
