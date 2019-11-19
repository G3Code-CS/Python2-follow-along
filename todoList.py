class TodoList:
    def __init__(self, name):
        self.name=name
        self.items=[]
    
    def __str__(self):
        return f"{self.name}: {self.items}"
    
    def __repr__(self):
        return f"TodoList({repr(self.name)})"

quit = False
all_lists = []
current_list = None

while not quit:
    #Get the input from the user
    command = input(f"(C)reate a new list\n(S)elect a list ({all_lists})\n(A)dd an item\n(Q)uit\nCommand : ")
    
    command = command.lower().strip()[0]
    if command == 'q': # quit
        quit = True

    elif command == 'c': # create
        name = input("Enter list name :").strip()
        
        new_list = TodoList(name)
        all_lists.append(new_list)
        print(all_lists)

    elif command == 's': # Select
        name = input("Enter list name:").strip()
        named_list = None

        for l in all_lists:
            if l.name == name:
                named_list = l
                break
        
        if named_list is None:
            print(f"No such list named {name}")

        else:
            current_list = named_list
            print(f"Current selected list is ({current_list})")
