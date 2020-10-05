#Class created to implement the stack data structure
class stack():
#Initialisation
    def __init__(self, size):
#If the input for stack size is not an integer, the size will be defaulted to 10
        print("\nCreating Stack...")
        if isinstance(size, int):
            self.__size = size
        else:
            self.__size = 10
            print("Invalid Stack Size: Set to Default (10)")
#Sets the stack to an empty list
        self.__stack = []
#Sets the head pointer to -1 (Indexing Starts at 0)
        self.__head = -1
        print("Stack Created\n")

#Procedure used to add an input URL to the stack
    def push(self, URL):
        if isinstance(URL, str):
            if not self.isFull():
                
                self.__stack.append(URL)
                self.__head += 1
                print(URL, "has been Added to the Stack")
            else:
                print("Stack is Full: Cannot push", URL)
        else:
            print(URL, "is not a valid URL")

#Function used to remove the top item from the stack and return it to the user
    def popTop(self):
        if self.isEmpty():
            print("The Stack is Empty: Cannot Pop")
        else:
            top = self.__stack[self.__head]
            self.__stack[self.__head] = None
            self.__head -= 1
            return top

#Function used to print the top item in the stack
    def peek(self):
        if self.isEmpty():
            print("The Stack is Empty: Cannot Peek")
        else:
            print("Top of stack:", self.__stack[self.__head])

#Function used to check if the stack is empty
    def isEmpty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

#Function used to check if the stack is full (Opposite to isFull)
    def isFull(self):
        if len(self.__stack) == self.__size:
            return True
        else:
            return False

#TESTING
#Creates new stack
myStack = stack(3)
#Adds 3 URLs to Stack
myStack.push("afl.com.au")
myStack.push("theage.com.au")
myStack.push("hawthornfc.com.au")
#Removes the top item from the stack and prints it
lastPage = myStack.popTop()
print(lastPage)
#Prints the NEW top value of the stack
myStack.peek()
#Adds another item to the stack
myStack.push("outlook.com")
#Prints the NEW top value of the stack
myStack.peek()

#ERROR HANDLING TESTING
myStack2 = stack("hello")
myStack2.push(16)
myStack2.peek()
shouldBeEmpty = myStack2.popTop()
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
myStack2.push("afl.com.au")
