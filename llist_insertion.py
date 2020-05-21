'''
LUCID PROGRAMMING REVIEW: LINKED LIST
    - Create Node and Linked Lists Classes
    - Create append, prepend, insert after node methods
'''

# Create class for node
class Node:
    # Create constructor and give it the argument of self and data
    # Data argument since we need to tell it what to pass into this node
    def __init__(self, data):
        self.data = data
        # Set self to None initially
        self.next = None


# Create class for linked list
class LinkedList:
    # Constructor
    def __init__(self):
        # Start of the list gets a head pointer
        self.head = None

    # function to print out the entries of a list
    # takes self as an argument because it's a Class function
    def print_list(self):
        current_node = self.head
        # While current_node is not NULL
        while current_node:
            print(current_node.data)
            # Move to next node in the list
            current_node = current_node.next

    # Function to append item to end of linked list
    def append(self, data):
        # First Case: If the linked list is empty and we need to append the first node
        # Create new node object and pass "data" as argument since the Node class takes an argument
        new_node = Node(data)

        # check if head of list is empty
        if self.head is None:
            self.head = new_node
            return

        # Next Case: If the linked list is not empty, we need to move the head pointer through each of the nodes
        # in the list to see where the end of the list is, so that we know where to input the new node
        # Define last_node and initially be equal to the head (b/c we're at the start of the list)
        last_node = self.head
        # While the next pointer of the node that we're currently on is not NULL, continue on the loop
        while last_node.next:
            # Move the head pointer to the right
            last_node = last_node.next
        # When loop has concluded last_node will point to the last node and now we can append node to end of list
        last_node.next = new_node


    # Function to prepend item to start of linked list
    def prepend(self, data):
        # Create new node object and pass "data" as argument since the Node class takes an argument
        new_node = Node(data)

        # We want the new node to point to the head (since we are prepending the new node to the start of the list)
        new_node.next = self.head
        # Set head to new node
        self.head = new_node


    # Function to insert item between two existing nodes in a linked list
    # Takes self since it's a Class function, previous node (so that we know what to insert after), and data
    def insert_after_node(self, prev_node, data):
        # If the prev_node (not we want to insert after) is not there; return
        if not prev_node:
            print('Previous node is not in the list')
            return

        # If prev_node is there, then create new node object
        new_node = Node(data)
        # Set new_node pointer to what prev_node is pointing to
        new_node.next = prev_node.next
        # Set prev_node pointer to new node
        prev_node.next = new_node



# Define a linked list object
llist = LinkedList()

# Function calls to append
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

# # Function call to prepend
# llist.prepend('E')

# Function call to insert between nodes
llist.insert_after_node(llist.head.next, 'E ')

llist.print_list()