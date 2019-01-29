# class TaskList:
#     def __init__(self,task1,task2,task3):
#         self.task1 = task1
#         self.task2 = task2
#         self.task3 = task3
#     def __str__(self):
#         return(f"{self.task1}\n{self.task2}\n{self.task3}")


taskList = ["School","Work","Laundry"]
newTask = ""
# taskToRemove=""
def main():
    problem1()



# Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program.
# Congratulations! You're running [YOUR NAME]'s Task List program.

# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program

def problem1():
    # userInputArray = []
    userInput = ""

    while userInput != '0':
        userInput= input("What would you like to do next?\n1. List all tasks.\n2. Add a task to the list.\n3. Delete a task.\n0. To quit the program\n")
        # print(userInput)

        if userInput == "1":
            print("To Do List!")
            print(listAll())
        elif userInput == "2":
            newTask = input("Add Task! ")
            print(addTask(newTask))
            # print(taskList)
        elif userInput =="3":
            taskToRemove = input("Enter task to remove ")
        elif userInput == 0:
            print("Invalid Option, Try Again!")




            # print(listAll())
            print(removeTask())

        #
        #
        # if userInput != '0':
        # userInputArray.append(userInput)
    # print('\n'.join(userInputArray))

def listAll():
    for itemInArray in taskList:
        return ('\n'.join(taskList))

def addTask(newTask):
    taskList.append(newTask)
    return ('\n'.join(taskList))
def removeTask():
    # taskList.remove(taskToRemove)
    # if taskToRemove == 1:
    taskList.remove("Laundry")

    return ('\n'.join(taskList))

    # newMyTaskList = TaskList("1. school", "2. work","3. laundry")
    # print(newMyTaskList)

# def deleteTask():




if __name__ == '__main__':
    main()
# userTask = []


# def main():
#     problem1()
#
#
# def problem1():
#     asktask1 = ""
#
#     while asktask1.lower() != "no":
#         menu_Selection = int(input("1.List Task, 2.Add task, 3.Delete Task, 4.Quit\n"))  #provding options for user to select
#         if menu_Selection == 1:              #if 1 is selected it will call my list task function
#             list_task()
#         elif menu_Selection == 2:                 #if 2 is selected it will call my add task function
#             add_Task()
#         elif menu_Selection == 3:                  #if 3 is selected it will call my delete task function
#             delete_Task()
#         elif menu_Selection == 4:                  #if 4 is selected it will call my quit function
#             quitFunction()
#             break
#         else:
#             print("Not an entry")
#
# # userRequest()
# def list_task():                           #this function is iterating through the elements in my array
#     for elements in userTask:
#         print(elements)
#
#
#
# def add_Task():
#     task_added = input("what task would you like to add?\n")            #asking user what task they ould like to add
#     userTask.append(task_added)
#     print(userTask)
#
#
# def delete_Task():
#     for element in userTask:                   #provding a reference to the user before they delete
#         print(element)
#     task_deleted = input("what task would you like to delete?\n")
#     if task_deleted in userTask:
#         userTask.remove(task_deleted)
#     else:
#         print("task not available")
#
# def quitFunction():
#     print("Thanks for trying ")              #good bye comment to user if they quit
# if __name__ == '__main__':
#     main()