tasks = []

def add_task():
    task = input("Enter a task:  ")
    tasks.append({"task":task, 'status':'undone'})
def view_task():
    print("   Tasks     status")
    t = 1
    for i in tasks:
        print(str(t) + '.' +  i["task"] + "   " + i["status"])  
        t += 1
def delete_task():
    print('   Choose Task To Delete  ')  
    view_task()
    num = int(input("Enter a Number:  "))
    tasks.pop(num-1)
def mark_task():
    print('   Choose a task to mark as done  ')
    view_task()
    num = int(input("Enter a Number:  "))
    tasks[num-1]["status"] = "Done"
def main():
    while True:
       print('    To Do List')
       print('1. Add Task')
       print("2. View Task")
       print("3. Delete Task")
       print("4. Mark Task")
       print("5. Exit")
       chose = int(input("   Choose Number 1-5  "))
       if chose == 1:
           add_task()
       elif chose == 2:
           view_task()
       elif chose == 3:
           delete_task()
       elif chose == 4:
           mark_task()
       elif chose == 5:
           print("   Goodbye")
           break
       else:
           print("invalid number please try again")
main()                           

                    