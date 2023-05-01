import json
from datetime import *

track_employee={}
track_task=[]
class Employee:
    def login(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
        self.login_time=datetime.now().strftime("%y-%m-%d  %H:%M:%S")
        track_employee.update(
            {'emp_name':self.name,
             'emp_id':self.emp_id,
             'login_time':self.login_time
             })

    def logout(self):
        end_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        track_employee.update({"logout_time":end_time})
        dt=date.today()
        filename=f'{self.name}_{dt}.json'
        emp_data=json.dumps(track_employee, indent=2)
        open(filename,"w").write(emp_data)

    def task(self):
        print("Task started")
        self.task_dic={}
        self.title=input("Enter task title: ")
        self.description=input("Enter task description:")
        self.start_time=datetime.now().strftime("%y-%m-%d: %H:%M")
        self.task_dic.update({
			'title':self.title,
			'description':self.description,
			'start_time':self.start_time
			})
        status=input("Press Y when you finished task : ")

        if status=='y' or status=='Y':
            self.end_time=datetime.now().strftime("%y-%m-%d: %H:%M")
            
            self.task_dic.update({
			'end_time':self.end_time
			})
        else:
             print("Invalid")    
        success=input("\nTask_success:\n 1:True\n 2:False\n Enter your choice: ")
        if success=='1':
            self.task_dic.update({
                'successful':True})
        elif success=='2':
                 self.task_dic.update({
                'successful':False})
        else:
             print("Invalid")

        track_task.append(self.task_dic)
        track_employee.update({'task':track_task})
            
        choice=input("\n 1:Start next task\n 2:Logout\n Enter your choice: ")
        if choice=="1":
            emp_obj.task()
        elif choice=='2':
            emp_obj.logout()
        else:
             print("Invalid")

emp_obj=Employee()
name=input("Enter Your name: ")
emp_id=input("Enter emp_id: ")
emp_obj.login(name,emp_id)
emp_obj.task()


