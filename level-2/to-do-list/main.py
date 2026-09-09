import json

def display_task(task, complete):
    if complete:
        return ''.join(char + '\u0336' for char in task)
    return task

def read_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            if data:
                return data
            else:
                print("There's no tasks right now.")
                return data
    except FileNotFoundError:
        print("The tasks file not found.")
    

def show_tasks(data):
    try:
        for i in range(len(data['id'])):
            print(f"{i+1}- {display_task(data['task'][i], data['complete'][i])}")
    except TypeError:
        print("There's no data.")

def add_task(task,file_name):
    if task:
        data = read_tasks(file_name)
        if data['id']:
            last_id = data['id'][len(data['id'])-1]
            data['id'].append(last_id+1)
            data['task'].append(task)
            data['complete'].append(False)
        else:
            data['id'].append(1)
            data['task'].append(task)
            data['complete'].append(False)
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("the task added successfully")
        except FileNotFoundError:
            print("The tasks file not found.")
    else:
        print("the task is empty.")

def delete_task(id,file_name):
    data = read_tasks(file_name)
    try:
        id = int(id)
        if id in data['id']:
            index = data['id'].index(id)
            data['id'].pop(index)
            data['task'].pop(index)
            data['complete'].pop(index)
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                print("the task deleted successfully")
            except FileNotFoundError:
                print("The tasks file not found.")
        else:
            print("invalid task number.")
    except ValueError:
        print("invalid task number.")


def mark_task(id,file_name):
    data = read_tasks(file_name)
    try:
        id = int(id)
        if id in data['id']:
            index = data['id'].index(id)
            data['complete'][index] = True
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                print("the task completed successfully")
            except FileNotFoundError:
                print("The tasks file not found.")
        else:
            print("invalid task number.")
    except ValueError:
        print("invalid task number.")


def to_do_list(file_name):
    while True:
        try:
            data = read_tasks(file_name)
            if data['id']:
                show_tasks(data)
                print("\n")
            choice = input("1-add task\n2-complete task\n3-delete task\n4-exit\n")
            if choice=="1":
                task = input("Enter task: ")
                add_task(task,file_name)
            elif choice=="2":
                id = input("Enter task number: ")
                mark_task(id,file_name)
            elif choice=="3":
                id = input("Enter task number: ")
                delete_task(id,file_name)
            elif choice=="4":
                print("Thanks to use our program.")
                break
            else:
                print("Wrong input.")
        except TypeError:
            print("Invalid file path.")
            break

to_do_list("to-do-list/tasks.json")