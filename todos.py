todos=[]

while True:
    user_action=input("enter your option ADD,SHOW,REPLACE,READ,EXIT:\n")
    
    match user_action:
        
        case "add":
            todo=input("Enter your todo Item:\n")+" "
            todos.append(todo)
            file=open("todos.txt","w")
            file.writelines(todos)
            file.close()
        case "show":
            print("Items in todo")
            for index,item in enumerate(todos,1):
                print(index,item)
                
        case "replace":
            listindex=int(input("Enter the todo item replace number:"))
            listindex=listindex-1
            new_item=input("Enter your replace item:")+" "
            todos[listindex]=new_item
        
        case "read":
            file=open("todos.txt","r")
            todos=file.readlines()
            print(todos)
            file.close()
            
        case exit:
            break
        
print("Thank you")

