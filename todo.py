import pickle
def print_todos(todos):
    print("=======Pending======")
    for index in range(len(todos)):
        if not todos[index]["completed"]:
            print(f"{index} : {todos[index]['title']}")
    print("======================")
    print("=======Completed======")
    for index in range(len(todos)):
        if todos[index]["completed"]:
            print(f"{index} : {todos[index]['title']}")      
    print("======================")   
    # if len(todos) == 0:
    #     print("You have nothing to do.")
    # else:
    #     i = 0
    #     for todo in todos:
    #         print(f"{i}: {todo}")
    #         i += 1

def add_todo(todos, item):
    todos.append({'title': item, 'completed' : False})

def delete_todo(todos, index):
    try:
        if todos[index]['completed']:
            print("You've already done this! Good job.")
        else:
            todos[index]['completed']=True
    except IndexError:
        print("That todo does not exist.")

def print_menu():
    message = """
    Todo App
==================
0. quit
1. print todos
2. add a todo
3. complete a todo
"""
    print(message)

def get_choice(prompt="Choose one: "):
    is_valid_choice = False
    choice = 0
    while not is_valid_choice:
        try:    
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Please enter a number.")
    return choice
    
def main():
    todo_list = []
    file_name = "todo.pickle"
    try:
        with open (file_name, 'rb') as file_handle:
            todo_list = pickle.load(file_handle)
    except:
        pass

    is_running = True
    while is_running:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("K. Byeeee!")
            is_running = False
        elif choice == 1:
            print_todos(todo_list)
        elif choice == 2:
            new_todo = input("Enter a todo: ")
            add_todo(todo_list, new_todo)
        elif choice == 3:            
            index_to_delete = get_choice("Enter the index to complete: ")
            delete_todo(todo_list, index_to_delete)
    with open(file_name, "wb") as file_handle:
        pickle.dump(todo_list, file_handle)  

main()
