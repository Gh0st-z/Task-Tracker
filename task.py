import datetime
import json
import os

class Task:
    def __init__(self):
        self.all_tasks = {}
        self.task_id = 0
        self.task_description = None
        self.task_status = None
        self.createdAt = None
        self.updatedAt = None


    def add_task(self):
        if not os.path.exists("task_list.json"):
            self.task_id += 1
            self.task_description = input("Enter the task to be done: ")
            self.task_status = "To Do"
            self.createdAt = str(datetime.datetime.now())

            self.all_tasks[f"task_id: {self.task_id}"]= {
                'task_description': self.task_description,
                'task_status': self.task_status,
                'created At': self.createdAt,
            }

            write_task = open("task_list.json", "w")
            json.dump(self.all_tasks, write_task, indent=4)
            print("-----------------------------------------")
            print("The task", self.task_description, "has been added sucessfully with status: ", self.task_status)
            print("-----------------------------------------")

        else:
            try:
                task_file = open("task_list.json", "r")
                task_list = json.load(task_file)
                id_list = []
                for items in task_list:
                    id_list.append(items)

                progressive_id = int(id_list[-1].split('task_id: ')[1])
                self.task_id = progressive_id + 1
                self.task_description = input("Enter the task to be done: ")
                self.task_status = "To Do"
                self.createdAt = str(datetime.datetime.now())

                task_list[f"task_id: {self.task_id}"]= {
                    'task_description': self.task_description,
                    'task_status': self.task_status,
                    'created At': self.createdAt,
                }
                
                self.all_tasks = task_list
                write_task = open("task_list.json", "w")
                json.dump(self.all_tasks, write_task, indent=4)
                print("-----------------------------------------")
                print("The task: ", self.task_description, "has been added sucessfully with status: ", self.task_status)
                print("-----------------------------------------")

            except:
                print("Please enter the details properly!")
                self.add_task()


    def remove_task(self):
        if not os.path.exists("task_list.json"):
            print("No tasks have been added! Please add tasks first!")
        
        else:
            try:
                task_file = open("task_list.json", "r")
                task_list = json.load(task_file)
                id_list = []
                updated_list = {}

                for items in task_list:
                    id_list.append(items)

                print("These are your available tasks: ")
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Task Id \t\t\t| " + "Task Description \t\t| " + "Task Status \t\t\t| " + "Created At \t\t\t\t| " + "Updated At")
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for items in task_list:
                    if len(task_list[items]) == 4:
                        print(items + "\t\t\t| " + task_list[items]['task_description'] + "\t\t\t| " + task_list[items]['task_status'] + "\t\t\t\t| " + task_list[items]['created At'] + "\t\t| " + task_list[items]['updated At'])
                    
                    else:
                        print(items + "\t\t\t| " + task_list[items]['task_description']  + "\t\t\t| " + task_list[items]['task_status'], "\t\t\t| " + task_list[items]['created At'] + "\t\t| " + "-")
                
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

                user_input = input("Enter the id of the task to remove: ")
                remove_id = "task_id: " + user_input

                if remove_id in task_list:

                    removed_task = task_list.pop(remove_id)
                    
                    for items in task_list:
                        updated_id = int(items.split("task_id: ")[1])
                        if updated_id > int(remove_id.split("task_id: ")[1]):
                            updated_id = int(items.split("task_id: ")[1]) - 1
                            updated_list[f"task_id: {updated_id}"] = task_list[items]
                        
                        else:
                            updated_list[f"task_id: {updated_id}"] = task_list[items]
                    
                    self.all_tasks = updated_list
                    update_file = open("task_list.json", "w")
                    json.dump(self.all_tasks, update_file, indent=4)

                    print("-----------------------------------------")
                    print("The task: ", removed_task["task_description"], "is removed successfully!")
                    print("-----------------------------------------")
                
                else:
                    print("-----------------------------------------")
                    print("Task with given id does not exist! Please enter valid id!")
                    print("-----------------------------------------")
                    self.remove_task()
            
            except:
                print("Please choose the tasks that are available!")
                self.remove_task()

                
    def update_status(self):
        if not os.path.exists("task_list.json"):
            print("No tasks have been added! Please add tasks first!")
        
        else:
            try:
                task_file = open("task_list.json", "r")
                task_list = json.load(task_file)
                id_list = []

                for items in task_list:
                    id_list.append(items)

                print("These are your available tasks: ")
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Task Id \t\t\t| " + "Task Description \t\t| " + "Task Status \t\t\t| " + "Created At \t\t\t\t| " + "Updated At")
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for items in task_list:
                    if len(task_list[items]) == 4:
                        print(items + "\t\t\t| " + task_list[items]['task_description'] + "\t\t\t| " + task_list[items]['task_status'] + "\t\t\t\t| " + task_list[items]['created At'] + "\t\t| " + task_list[items]['updated At'])
                    
                    else:
                        print(items + "\t\t\t| " + task_list[items]['task_description']  + "\t\t\t| " + task_list[items]['task_status'], "\t\t\t| " + task_list[items]['created At'] + "\t\t| " + "-")
                
                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

                field_update = input("Enter the id of the task you would like to update: ")
                update_id = "task_id: " + field_update

                if update_id in task_list:
                    update_progress = int(input("What would you like to set the progress to?\n 1. In Progress\n 2. Done: "))

                    if update_progress == 1:
                        task_list[update_id]['task_status'] = 'In Progress'
                        task_list[update_id]['updated At'] = str(datetime.datetime.now())

                    elif update_progress == 2:
                        task_list[update_id]['task_status'] = 'Done'
                        task_list[update_id]['updated At'] = str(datetime.datetime.now())

                    else:
                        print("Please enter valid number!")
                        print("-----------------------------------------")
                        self.update_status

                    self.all_tasks = task_list
                    update_tasks = open("task_list.json", "w")
                    json.dump(self.all_tasks, update_tasks, indent=4)

                else:
                    print("-----------------------------------------")
                    print("Task with given id does not exist! Please enter valid id!")
                    print("-----------------------------------------")
                    self.update_status()
            
            except:
                print("Please choose the tasks that are available!")
                self.update_status()


    def list_task(self):
        if not os.path.exists("task_list.json"):
            print("No tasks have been added! Please add tasks first!")
        
        else:
            task_file = open("task_list.json", "r")
            task_list = json.load(task_file)

            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Task Id \t\t\t| " + "Task Description \t\t| " + "Task Status \t\t\t| " + "Created At \t\t\t\t| " + "Updated At")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for items in task_list:
                if len(task_list[items]) == 4:
                    print(items + "\t\t\t| " + task_list[items]['task_description'] + "\t\t\t| " + task_list[items]['task_status'] + "\t\t\t\t| " + task_list[items]['created At'] + "\t\t| " + task_list[items]['updated At'])
                
                else:
                    print(items + "\t\t\t| " + task_list[items]['task_description']  + "\t\t\t| " + task_list[items]['task_status'], "\t\t\t| " + task_list[items]['created At'] + "\t\t| " + "-")
            
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    def list_completed(self):
        if not os.path.exists("task_list.json"):
            print("No tasks have been added! Please add tasks first!")
        
        else:
            task_file = open("task_list.json", "r")
            task_list = json.load(task_file)

            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Task Id \t\t\t| " + "Task Description \t\t| " + "Task Status \t\t\t| " + "Created At \t\t\t\t| " + "Updated At")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for items in task_list:
                if task_list[items]['task_status'] == "Done":
                    if len(task_list[items]) == 4:
                        print(items + "\t\t\t| " + task_list[items]['task_description'] + "\t\t\t| " + task_list[items]['task_status'] + "\t\t\t\t| " + task_list[items]['created At'] + "\t\t| " + task_list[items]['updated At'])
                    
                    else:
                        print(items + "\t\t\t| " + task_list[items]['task_description']  + "\t\t\t| " + task_list[items]['task_status'], "\t\t\t| " + task_list[items]['created At'] + "\t\t| " + "-")
            
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    def list_progressing(self):
        if not os.path.exists("task_list.json"):
            print("No tasks have been added! Please add tasks first!")
        
        else:
            task_file = open("task_list.json", "r")
            task_list = json.load(task_file)

            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Task Id \t\t\t| " + "Task Description \t\t| " + "Task Status \t\t\t| " + "Created At \t\t\t\t| " + "Updated At")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for items in task_list:
                if task_list[items]['task_status'] == "In Progress":
                    if len(task_list[items]) == 4:
                        print(items + "\t\t\t| " + task_list[items]['task_description'] + "\t\t\t| " + task_list[items]['task_status'] + "\t\t\t\t| " + task_list[items]['created At'] + "\t\t| " + task_list[items]['updated At'])
                    
                    else:
                        print(items + "\t\t\t| " + task_list[items]['task_description']  + "\t\t\t| " + task_list[items]['task_status'], "\t\t\t| " + task_list[items]['created At'] + "\t\t| " + "-")
            
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    def list_pending(self):
        if not os.path.exists("task_list.json"):
            print("No tasks have been added! Please add tasks first!")
        
        else:
            task_file = open("task_list.json", "r")
            task_list = json.load(task_file)

            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Task Id \t\t\t| " + "Task Description \t\t| " + "Task Status \t\t\t| " + "Created At \t\t\t\t| " + "Updated At")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for items in task_list:
                if task_list[items]['task_status'] == "To Do":
                    if len(task_list[items]) == 4:
                        print(items + "\t\t\t| " + task_list[items]['task_description'] + "\t\t\t| " + task_list[items]['task_status'] + "\t\t\t\t| " + task_list[items]['created At'] + "\t\t| " + task_list[items]['updated At'])
                    
                    else:
                        print(items + "\t\t\t| " + task_list[items]['task_description']  + "\t\t\t| " + task_list[items]['task_status'], "\t\t\t| " + task_list[items]['created At'] + "\t\t| " + "-")
            
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

