#=====importing libraries===========

from datetime import date, datetime

#====Function Section====

"""
def reg_user() : Takes a user and password to be registered. It displays the existing user names, so that the admin 
does not register a user that is already on the database. It will check if the new user entered already exists in the
database ("user.txt") as a fail safe. If no then it registers the username. It also checks if the password is entered 
correctly.
"""


def reg_user():
    while True:

        r_stored_user = []
        r_stored_password = []

        with open("user.txt", "r") as r:
            for i in r:
                user2, pass2 = i.strip("\n").split(", ")
                r_stored_user.append(user2)
                r_stored_password.append(pass2)

        print("These are the existing users ", r_stored_user)
        r_user = input("Please enter the new username to register: ")
        r_password = input("Please enter the new password to register: ")
        r_c_password = input("Please confirm the new password: ")

        if r_password == r_c_password and r_user not in r_stored_user:
            with open("user.txt", "a") as new_reg:
                new_reg.write("\n" + r_user)  # On a new line write the new user to user.txt
                new_reg.write(", " + r_password)  # After a comma and space first write the new password to user.txt
            print(f"You've successfully registered {r_user}")
            break
        else:
            if r_password != r_c_password:
                print("Password does not match, please try again")
                continue  # Goes back to the start and ask to enter details again
            else:
                print("This user is already registered")
                continue  # Goes back to the start and ask to enter details again


"""
def add_task() : Requests a user name and takes a input of task, adds it to the task database ("task.exe"), for only 
existing users. The user needs to submit a title, description, due date. The function sets the current date of when the task was 
uploaded. The function also sets a default value of "No". The function tests ro see if the due date set is not a date
that is passed.
"""


def add_task():
    while True:
        a_username = input("Enter the user you would like to assign a task to: ")  # Enter a user to assign a task to

        a_stored_user = []

        with open("user.txt", "r") as r:
            for i in r:
                user3, pass3 = i.strip("\n").split(", ")
                a_stored_user.append(user3)

        if a_username not in a_stored_user:
            print("User does not exist, please try again")
            continue
        else:
            a_title = input("Please enter a title of the task: ")
            a_description = input("Please enter a description of the task: ")
            while True:
                a_due_date = input("Please assign a due date for the task, eg 09 Oct 1994: ")

                # Coverts to yyyy mmm dd so that the date can be compared
                test_a_due_date = datetime.strptime(a_due_date, "%d %b %Y").strftime("%Y %b %d")

                today = date.today()
                current_date = today.strftime("%d %b %Y")  # Today's date in the stored in current_date
                test_current_date = today.strftime("%Y %b %d")  # Coverts to yyyy mmm dd so that the date can be compared

                if test_current_date <= test_a_due_date:  # This allows task due date not to fall before the current date
                    break
                else:
                    print("Due date has already passed")
                    continue

            a_task_indication = "No"

            with open("tasks.txt", "a") as new_task:
                new_task.write("\n" + a_username)
                new_task.write(", " + a_title)
                new_task.write(", " + a_description)
                new_task.write(", " + current_date)
                new_task.write(", " + a_due_date)
                new_task.write(", " + a_task_indication)
            print("You've successfully registered a task")
            break


"""
def view_all(): Views all the task available in the database. 
"""


def view_all():
    with open("tasks.txt", "r") as view_all:
        data = view_all.readlines()

        for j, i in enumerate(data, 1):
            split_line = i.strip().split(", ")
            line = f"₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋[{j}]₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋\n"
            line += "\n"  # New line
            line += f"Task: \t\t\t\t\t{split_line[1]}\n"  # Prints Task
            line += f"Assigned to: \t\t\t{split_line[0]}\n"  # Prints username
            line += f"Date assigned: \t\t\t{split_line[3]}\n"  # Prints assigned date
            line += f"Due Date: \t\t\t\t{split_line[4]}\n"  # Prints due date
            line += f"Task Complete: \t\t\t{split_line[5]}\n"  # Prints if the task is complete or not
            line += f"Task description:\n{split_line[2]}\n"  # Prints description of the task
            line += "\n"  # New line
            line += "₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋\n"
            print(line)


"""
def view_mine(): Views only task of the user that is currently logged in. If the user does not have a task assigned to
them, then an error message is given. This function allows the user to amend their task or go back to the main menu. If
user decides to edit. They can edit the due date and user in the task. They can also make it complete or not complete.
"""


def view_mine():
    with open("tasks.txt", "r") as view_mine:
        vm_view = view_mine.readlines()

        valid_user_store = []
        valid_task_store = []

        count = 1  # Start count at one for numbering task assigned to current user
        for line in vm_view:
            split_line = line.strip().split(", ")
            if split_line[0] == username:
                line = f"₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋[{count}]₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋\n"
                line += "\n"  # New line
                line += f"Task: \t\t\t\t\t{split_line[1]}\n"  # Prints Task
                line += f"Assigned to: \t\t\t{split_line[0]}\n"  # Prints username
                line += f"Date assigned: \t\t\t{split_line[3]}\n"  # Prints assigned date
                line += f"Due Date: \t\t\t\t{split_line[4]}\n"  # Prints due date
                line += f"Task Complete: \t\t\t{split_line[5]}\n"  # Prints if the task is complete or not
                line += f"Task description:\n{split_line[2]}\n"  # Prints description of the task
                line += "\n"  # New line
                line += "₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋₋\n"
                print(line)
                valid_user_store.append(split_line[0])
                valid_task_store.append(split_line)
                count += 1  # Adds one after every run

        if username not in valid_user_store:
            print("This user does not have any task.")
        else:
            while True:
                option = input("Would you like to edit a task? (Edit) or type \"-1\" to go back to the main menu: ")
                if option == "-1":
                    break
                if option.lower() != "edit":
                    print("You've selected an invalid choice")
                    continue

                task_choice = int(input("Please enter the task you like to edit? "))-1
                chosen_task = valid_task_store[task_choice]

                edit_task = int(input("""
1) Would you like to edit the task?
2) Would you like to mark task as complete?
Please enter your choice here (1 or 2): 
"""))

                if edit_task == 1:
                    input_a = input("Would you like to edit the user? (User) or the due date? (Due): ")
                    if input_a.lower() == "user":
                        while True:
                            user_input = input("Please choose a user to assign the task to: ")

                            b_stored_user = []

                            with open("user.txt", "r") as read_file:
                                for items in read_file:
                                    check_user, check_pass = items.strip().split(", ")
                                    b_stored_user.append(check_user)

                            if user_input not in b_stored_user or user_input == username:
                                print("Invalid user name was entered, please try again")
                                continue

                            with open("tasks.txt", "r+") as read_user:
                                r_user = read_user.readlines()
                                for index, line in enumerate(r_user):  # loops through tasks and numbers them
                                    _1_split_line = line.strip().split(", ")
                                    if chosen_task == _1_split_line:
                                        _1_split_line[0] = user_input  # Adds a new user to the task
                                        new_data = ", ".join(_1_split_line)
                                        r_user[index] = new_data + "\n"  # Locates the specific place to add the new user
                            with open("tasks.txt", "w") as r_user_final:
                                for new_line in r_user:
                                    r_user_final.write(new_line)  # Writes the new task into the task database
                                print(f"You've successfully assigned the task to {user_input}")
                                break
                    elif input_a.lower() == "due":
                        while True:
                            new_due_date = input("Please enter a new due date for the task, eg 09 Oct 1994: ")

                            # Coverts to yyyy mmm dd so that the date can be compared
                            test_a_due_date = datetime.strptime(new_due_date, "%d %b %Y").strftime("%Y %b %d")

                            today = date.today()  # Today's date
                            test_current_date = today.strftime(
                                "%Y %b %d")  # Coverts to yyyy mmm dd so that the date can be compared

                            if test_current_date <= test_a_due_date:  # This allows task due date not to fall before the current date
                                break
                            else:
                                print("Due date has already passed")
                                continue
                        with open("tasks.txt", "r+") as r_due:
                            edit_due = r_due.readlines()
                            for index, line in enumerate(edit_due):  # loops through tasks and numbers them
                                _2_split_line = line.strip().split(", ")
                                if chosen_task == _2_split_line:
                                    _2_split_line[-2] = new_due_date  # Adds a new date to the task
                                    new_data = ", ".join(_2_split_line)
                                    edit_due[index] = new_data + "\n"  # Locates the specific place to add the new date
                        with open("tasks.txt", "w") as r_2_final:
                            for new_line in edit_due:
                                r_2_final.write(new_line)  # Writes the new task into the task database
                            print("You've successfully changed the due date")
                            break

                if edit_task == 2:
                    with open("tasks.txt", "r") as r_2:
                        edit_yes = r_2.readlines()
                        for index, line in enumerate(edit_yes):  # loops through tasks and numbers them
                            _3_split_line = line.strip().split(", ")
                            if chosen_task == _3_split_line:
                                _3_split_line[-1] = "Yes\n"  # Adds a new value ("Yes") to the task
                                new_data = ", ".join(_3_split_line)
                                edit_yes[index] = new_data  # Locates the specific place to add the new value
                    with open("tasks.txt", "w") as r_2_final:
                        for new_line in edit_yes:
                            r_2_final.write(new_line)  # Writes the new task into the task database
                        print("The task is marked completed")
                continue


"""
def display_statistics(): Displays statistics for all the information in the database.
"""


def display_statistics():
    user_count = 0
    task_count = 0

    print("\033[1m", "Total users in the database")
    print("-----------------------------------------")
    with open("user.txt", "r") as r_user:
        for i in r_user:
            user_count += 1
        print("There are", user_count, "users in the database\n")

    print("\033[1m", "\nTotal tasks in the database")
    print("-------------------------------------------")
    with open("tasks.txt", "r") as r_task:
        for i in r_task:
            task_count += 1
        print("There are", task_count, "tasks in the database\n")

    print("\033[1m", "\n""This is the user overview")
    print("------------------------------------")
    with open("user_overview.txt", "r") as r_user_view:
        print(r_user_view.read())

    print("\033[1m", "\n""This is the task overview")
    print("------------------------------------")
    with open("task_overview.txt", "r") as r_task_view:
        print(r_task_view.read())


"""
def generate_report(): Generates a user and task report be displayed later, with display statistics.
"""


def generate_report():
    task_count = 0
    task_completed = 0
    task_notcompleted = 0
    task_overdue = 0
    task_store = []

    with open("tasks.txt", "r") as task:
        for items in task.readlines():
            temp_store = items.strip().split(", ")
            task_store.append(temp_store)
            task_count += 1
            if temp_store[-1] == "Yes":
                task_completed += 1
            if temp_store[-1] == "No":
                task_notcompleted += 1
            entered_due_date = temp_store[-2]

            # Coverts to yyyy mmm dd so that the date can be compared
            test_due_date = datetime.strptime(entered_due_date, "%d %b %Y").strftime("%Y %b %d")

            today = date.today()  # Today's date
            current_date = today.strftime("%Y %b %d")  # Coverts to yyyy mmm dd so that the date can be compared

            if current_date > test_due_date and temp_store[-1] == "No":
                task_overdue += 1
    per_incompleted = round((task_notcompleted/task_count)*100, 1)
    per_overdue = round((task_overdue/task_count)*100, 1)

    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f"There are {task_count} tasks in the database\n")
        task_overview.write(f"There is {task_completed} completed tasks in the database\n")
        task_overview.write(f"There is {task_notcompleted} not completed tasks in the database\n")
        task_overview.write(f"There is {task_overdue} over due tasks in the database\n")
        task_overview.write(f"The percentage not completed is {per_incompleted}%\n")
        task_overview.write(f"There percentage overdue is {per_overdue}%\n")

    overall_user_count = 0
    user_store = []

    with open("user.txt", "r") as users:
        total_users = users.readlines()
        for user_counter in total_users:
            user_split = user_counter.split(", ")
            user_store.append(user_split[0])
            overall_user_count += 1

    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f"The total numbers of registered users are {overall_user_count}\n")
        user_overview.write(f"There is {task_completed} completed tasks in the database\n")

        for user in range(0, overall_user_count):  # This is to loop through x number of times (4 = for the number of users)

            #  Locally stored counters
            total = task_count
            user_task = 0
            user_completed = 0
            user_not_completed = 0
            user_overdue = 0

            for task in range(0, total):  # Loops though the number of task in the database
                if user_store[user] == task_store[task][0] and task_store[task][-1].lower() == "yes":
                    user_task += 1
                    user_completed += 1
                elif user_store[user] == task_store[task][0] and task_store[task][-1].lower() == "no" and datetime.strptime(task_store[task][4], "%d %b %Y") < datetime.now():
                    user_task += 1
                    user_not_completed += 1
                    user_overdue += 1
                elif user_store[user] == task_store[task][0] and task_store[task][-1].lower() == "no":
                    user_task += 1
                    user_not_completed += 1

                task_percentage = 0
                complete_percentage = 0
                incomplete_percentage = 0
                overdue_percentage = 0

                task_percentage = round((user_task / total)*100, 1)
                if user_task != 0:
                    complete_percentage = round((user_completed / user_task)*100, 1)
                    incomplete_percentage = round((user_not_completed / user_task)*100, 1)
                    overdue_percentage = round((user_overdue / user_task)*100, 1)

            user_overview.write(f"\nUser: {user_store[user]}\n")
            user_overview.write(f"Number of tasks assigned to the {user_store[user]} is {user_task}\n")
            user_overview.write(f"The total percentage of tasks assigned to {user_store[user]} is {task_percentage}%\n")
            user_overview.write(f"The percentage of tasks completed by {user_store[user]} is {complete_percentage}%\n")
            user_overview.write(f"The percentage of tasks not completed by {user_store[user]} is {incomplete_percentage}%\n")
            user_overview.write(f"The percentage of tasks overdue by {user_store[user]} is {overdue_percentage}%\n")

    print("You have successfully generated the reports")


#====Login Section====

"""
The allows user to log in with a user name and their corresponding password only.
"""

while True:
    with open("user.txt", "r") as r:
        username = input("Please enter your username here: ")
        input_pass = input("Please enter your password here: ")

        dict = {}

        for i in r:
            user1, pass1 = i.strip("\n").split(", ")
            dict[user1] = pass1

        if username in dict and dict[username] == input_pass:
            break
        else:
            print("Your username or password is not correct, please try again")
    continue


while True:
    """
    presenting the menu to the user and
    making sure that the user input is converted to lower case.
    """

    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()  # If user is logged in as an admin show this menu. Any option in the menu is selected will be lower case
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()  # All other users are shown this menu. Any option in the menu is selected will be lower case

    if menu == 'r' and username == "admin":  # If user is an admin and chose "r", the code below is played.

        reg_user()

    elif menu == 'a':  # If any user types "a" the code below will run

        add_task()

    elif menu == 'va':  # If any user types "va" the code below will run

        view_all()

    elif menu == 'vm':  # If any user types "vm" the code below will run

        view_mine()

    elif menu == "ds":  # If admin types "ds" the code below will run to show

        display_statistics()

    elif menu == "gr":  # if user admin types in "gr

        generate_report()

    elif menu == 'e':  # If any user types "e" the code below will show statistics
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")  # If wrong choice was selected in the menu, then this will run
