
print("welcome to task manager")


print("Task Manager Started")

tasks =[]
 
  def add_task(task):
      tasks.append(task)


print ("welcome to Task Manager")



def list_tasks():
    return tasks


def complete_task(index):

  tasks.pop(index)
