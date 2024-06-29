task=[]

print("--------------------")
print("WELCOME TO TODO_LIST")
print("--------------------")

def add_task():
    task_name=input("Name of your task: ")
    priority=input("priority(HIGH, MEDIUM, LOW): ").upper()
    if priority=="":
        priority=None
        task.append(f"{task_name}:{priority}")
    else:
        task.append(f"{task_name}:{priority}")
        

def delete_task(delete):
    del task[delete-1]

def completed_task(completed):
    task[completed-1]=f"{task[completed-1]}=completed"


def priority(level):
    l=[]
    for i in range(len(task)):
        if f":{level}" in task[i]:
            l.append(task[i])
    print(l,"\n")


def home():
    print("'1' ADD TASKS")
    print("'2' DELETE TASKS")
    print("'3' COMPLETED TASKS")
    print("'4' PRIORITY TASKS")
    print("'0' END","\n")
    print(f"Your current tasks-> {task}","\n")
    opt=input("Select your choice: ")
    return opt

run=True

while run:
    opt=home()

    if opt==str(0):
        run=False

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
        which_task=int(input("which task is completed: "))
        if "=completed" in task[which_task-1]:
            print("Already mark as completed...\n")
        else:
            completed_task(which_task)

    elif opt==str(4):
        dic={1:'LOW' , 2:'MEDIUM' , 3:'HIGH'}
        level=input("which task level('1':LOW , '2':MEDIUM , '3':HIGH): ")
        if str(0)<level and level<str(4):
            priority(dic[int(level)])
        else:
            print("wrong option selected")

    else:
        print("Incorrect option selected!!")
    