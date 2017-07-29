#Create a classEmployee and then do the following
class Employee(object):

#initializing with it zero
    employeesCount = 0

#Create a constructor to initialize name and salary and function for the count

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeesCount += 1

#displaying the  display count

    def displayCount(self):
        print( "Total Employee %d" % Employee.empCount)


#displaying the employee name and salary

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


class Manager(Employee):
    def __init__(self, name,salary,age):
        super(Manager, self).__init__(name,salary)
        self.age=24
    def displayManager(self):
        print("name:",self.name,",salary:",self.salary,",Age:",self.age)


mgr= Manager("ash",200,24)
mgr.displayManager()

emp1 = Employee("avinash", 200)
emp2 = Employee("hsaniva", 500)
emp3= Employee("harsha",400)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print( "Total Employee: %d" % Employee.employeesCount)

