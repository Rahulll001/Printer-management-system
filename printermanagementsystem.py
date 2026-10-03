# Printer Management System
# Stack and Queue using Linked List

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


# Stack
class Stack:
    def _init_(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Document", data, "added to history.")

    def pop(self):
        if self.top is None:
            print("Printed history is empty.")
            return

        print("Document", self.top.data, "removed from history.")
        self.top = self.top.next

    def display(self):
        temp = self.top
        if temp is None:
            print("Printed history is empty.")
            return

        print("Printed History:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Queue
class Queue:
    def _init_(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Print request", data, "added.")

    def dequeue(self, stack):
        if self.front is None:
            print("Print queue is empty.")
            return

        data = self.front.data
        print("Printing document", data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        # Add printed document to Stack
        stack.push(data)

    def display(self):
        temp = self.front

        if temp is None:
            print("Print queue is empty.")
            return

        print("Print Queue:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Main program
stack = Stack()
queue = Queue()

while True:
    print("\n--- PRINTER MANAGEMENT SYSTEM ---")
    print("1. Add Print Request")
    print("2. Print Document")
    print("3. Display Print Queue")
    print("4. Display Printed History")
    print("5. Remove Latest History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter Document Number: "))
        queue.enqueue(data)

    elif choice == 2:
        queue.dequeue(stack)

    elif choice == 3:
        queue.display()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        stack.pop()

    elif choice == 6:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
