class TodoList:
    def __init__(self, name):
        self.name=name
        self.items=[]
    
    def __str__(self):
        return f"{self.name}: {self.items}"

quit = False

while not quit:
    #Get the input from the user
    command = input("(C)reate a new list\n(S)elect a list\n(A)dd an item\n(Q)uit\nCommand : ")
    
    command = command.lower().strip()[0]
    if command == 'q': # quit
        quit = True

    elif command == 'c': # create
        name = input("Enter list name :").strip()
        tl = TodoList("list 1")
        tl.items.append("Get milk")
        tl.items.append("Get roses")

        print(tl)
