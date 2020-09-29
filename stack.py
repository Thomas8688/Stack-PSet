#Class created to implement the stack data structure
class stack():
#Initialisation
    def __init__(self, size):
#If the input for stack size is not an integer, the size will be defaulted to 10
        if isinstance(size, int):
            self.__size = size
        else:
            self.__size = 10
            print("Invalid Stack Size: Set to Default (10)")
#Sets the stack to an empty list
        self.__stack = []

#Procedure used to add an input URL to the stack
    def push(self, URL):
        if isinstance(URL, str):
            if not self.isFull():
                self.__stack.append(URL)
            else:
                print("Stack is Full: Cannot push", URL)
        else:
            print(URL, "is not a valid URL")

#Function used to remove the top item from the stack and return it to the user
    def popTop(self):
        if self.isEmpty():
            print("The Stack is Empty")
        else:
            top = self.__stack[-1]
            self.__stack = self.__stack[:-1]
            return top

#Function used to print the top item in the stack
    def peek(self):
        if self.isEmpty():
            print("The Stack is Empty")
        else:
            print(self.__stack[-1])

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
myStack = stack(3)
myStack.push("afl.com.au")
myStack.push("theage.com.au")
myStack.push("hawthornfc.com.au")
lastPage = myStack.popTop()
print(lastPage)
myStack.peek()
myStack.push("outlook.com")
myStack.peek()
