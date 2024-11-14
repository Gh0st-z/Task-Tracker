import sys
import task


print("-----------------------------------------")
print("Welcome to Task Tracker!")
print("-----------------------------------------")

task_obj = task.Task()

def continue_operation():
        user_input = input("Do you wish to continue? Y/N: ")
        print("-----------------------------------------")
        if user_input.upper() == "Y":
             userInput()
        
        elif user_input.upper() == "N":
             print("Thank you for using the program!")
             print("-----------------------------------------")
             input("Press any button to close the program...")
             sys.exit(0)
        
        else:
             print("Please enter valid input!")
             print("-----------------------------------------")
             continue_operation()

def userInput():
    try:
        user_input = int(input("What would you like to do?\n"
                    "1. Add To-Do Tasks\n"
                    "2. Remove Tasks\n"
                    "3. Update Tasks\n"
                    "4. List All Tasks\n"
                    "5. List Completed Tasks\n"
                    "6. List In Progress Tasks\n"
                    "7. List To-Do Tasks\n"
                    "Enter Input (Press 0 to quit): "))
        print("-----------------------------------------")
        
        if  user_input == 1:
            task_obj.add_task()
            continue_operation()

        elif user_input == 2:
            task_obj.remove_task()
            continue_operation()

        elif user_input == 3:
            task_obj.update_status()
            continue_operation()

        elif user_input == 4:
            task_obj.list_task()
            continue_operation()

        elif user_input == 5:
            task_obj.list_completed()
            continue_operation()

        elif user_input == 6:
            task_obj.list_progressing()
            continue_operation()

        elif user_input == 7:
            task_obj.list_pending()
            continue_operation()

        elif user_input == 0:
            print("Thank you for using the program!")
            print("-----------------------------------------")
            input("Press any button to close the program...")
            sys.exit(0)

        else:
            print("Enter the options that are available to you!")
            userInput()
        
    except ValueError:
        print("Please Enter Appropriate Value (1 to 7)!")
        userInput()


userInput()

