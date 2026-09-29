
condition=True

def add_task():
    n=input("enter your task")
    m=open("task_to_do.txt","a")
    m.write(n + "\n")
    m.close()
def view_task():
    h=open("task_to_do.txt","r")
    v=h.read()
    print(v)
    h.close()
def delete_tasks():
    remaining_tasks=[]
    p=input('enter the task you want to remove')
    r=open("task_to_do.txt","r")
    task=r.readlines()
    for i in task:
        i=i.strip()
        if i!=p:
            remaining_tasks.append(i)
    r.close()
    w=open("task_to_do.txt","w")
    for h in remaining_tasks:
        w.write(h + "\n")
    w.close()
    print("task removed successfully")
while condition==True:
    print("----------TO_DO_LIST_CLI---------")
    print("1:Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")
    try:
        choice=int(input("enter your choice:"))
    except ValueError:
        print("Invalid Input")
        continue
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        delete_tasks()
    elif choice==4:
        condition=False
    else:
        print("Invalid Choice")
        
    


