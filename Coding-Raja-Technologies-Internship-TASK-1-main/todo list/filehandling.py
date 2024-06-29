task=[]

print("--------------------")
print("WELCOME TO TODO_LIST")
print("--------------------")


def add_task():
    task_name= input("Name of your task: ")
    priority=input("priority(HIGH, MEDIUM, LOW otherwise None): ").upper()
    if priority=="HIGH" or priority=="MEDIUM" or priority=="LOW" and task_name!="":
        task.append(f"{task_name}:{priority}")
    else:
        if task_name!="":
            priority=None
            task.append(f"{task_name}:{priority}")
        else:
            print("Please give a name to the task!")
        

def delete_task(delete):
    del task[delete-1]

def completed_task(completed):
    task[completed-1]=f"{task[completed-1]}=completed"


def priority(level):
    l=[]
    for i in range(len(task)):
        if f":{level}" in task[i]:
            l.append(task[i])
    print(l)

def duedate(x):
    date,month,year=map(str,input(f"Date(DD MM YYYY): ").split())
    task[x-1]=f"{task[x-1]} duedate:{date}/{month}/{year}"
    print(f"Due Date is added to the task at {date}/{month}/{year}","\n")


def view(task):
    if task!=[]:
        print("_______________________________________________________")
        print("Name of the tasks:Priority duedate:__/__/____=completed")
        print("_________________________OR____________________________")
        print("Name of the tasks:Priority=completed duedate:__/__/____")
        print("_______________________________________________________")
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")
    else:
        print("EMPTY!!!")


def filehandle(file_name,mode):
    if file_name=="" or mode=="":
        print("No file name or mode!")
    elif file_name!="" and (mode=="a" or mode=="r"):
        print(f"File name: {file_name}, mode='{mode}'")
        file=open(f"{file_name}",f"{mode}")
        if mode=="r":
            print(file.read())
            file.close()

        elif mode=="a":
            write_words=input("Write tasks to add it to the existing file: ")
            file.write(f"\n{write_words}")
            file.close()
            print("Successfully added.")

        else:
            print("Not a right mode!!")



    elif file_name!="" and (mode!="a" or mode!="r"):
        print("wrong mode..")
        

def home():
    print()
    print("'00' To open the task file")
    print("'1' ADD TASKS")
    print("'2' DELETE TASKS")
    print("'3' COMPLETED TASKS")
    print("'4' PRIORITY TASKS")
    print("'5' GIVE DUE DATE TO A TASK")
    print("'6' VIEW FULL TASKS")
    print("'0' END","\n")
    print(f"Your current tasks-> {task}","\n")
    opt=input("Select your choice: ")
    return opt

run=True

while run:
    opt=home()

    if opt==str(0):
        run=False

    elif opt=="00":
        input_file=input("Name of your file(in exact same words): ")
        input_mode=input("Only for reading type:'r' or add something type:'a': ").lower()
        filehandle(input_file,input_mode)

    elif opt==str(1):
        add_task()
        
    elif opt==str(2):
        if task!=[]:
            which_task=int(input("which task to be delete: "))
            delete_task(which_task)
        else:
            print("task list is empty!!\n")
            continue

    elif opt==str(3):
        if task!=[]:
            which_task=int(input("which task is completed: "))
            if "=completed" in task[which_task-1]:
                print("Already mark as completed...\n")
            else:
                completed_task(which_task)
        else:
            print("Empty list..")


    elif opt==str(4):
        dic={1:'LOW' , 2:'MEDIUM' , 3:'HIGH', 4:None}
        level=input("which task level('1':LOW , '2':MEDIUM , '3':HIGH '4'.NONE): ")
        if str(0)<level and level<str(5):
            priority(dic[int(level)])
        else:
            print("wrong option selected")

    elif opt==str(5):
        if task!=[]:
            which_task=input("which task you want to give duedate: ")
            for i in range(len(task)):
                if i == int(which_task)-1:
                    duedate(int(which_task))
                    break
                else:
                    print("The task is not present!")
                    break
        else:
            print("Empty list..")

    elif opt==str(6):
        view(task)

    else:
        print("Incorrect option selected!!")
    