import csv
import pdb


class Employees():
    
    def show_employees(self):
        #Show the employees in a list of some sort
        data = open('employees.csv',encoding="utf-8")
        csv_data = csv.reader(data)
        employees_list = list(csv_data)
        data.close()
        
        for line in employees_list:
            print(line)
    
    def hire_person(self, name, last_name, position, salary, rate):
        #Hire someone taking into account the ^ variables
        f = open('employees.csv','a',newline='')
        csv_writer = csv.writer(f)
        try:
            csv_writer.writerow([name, last_name, position, salary, rate])
        except:
            print("The operation was not succersful, please check your data")
        
        f.close()
    
        
    def fire_person(self, name, last_name):
        #Delete someone from the csv file and return if it was not found or if the operations was succesful
        data = open('employees.csv',encoding="utf-8")
        csv_data = csv.reader(data)
        employees_list = list(csv_data)
        data.close()
        found = 'Not found'
        for row in employees_list:
            if row[0] == name:
                if row[1] == last_name:
                    row[0] = ' ' 
                    row[1] = ' '
                    row[2] = ' '
                    row[3] = 0 
                    row[4] = 0
                    
                    file_to_output = open('employees.csv','w',newline='', encoding='utf-8')
                    csv_writer = csv.writer(file_to_output,delimiter=',')
                    csv_writer.writerows(employees_list)
                    file_to_output.close()
                    found = 'employer was Fired'
                    break
        print(found)
        
                
        
        

    def raise_person(self, name, last_name, position):
        #Elevate someone's position and modify the value on the csv file 
        data = open('employees.csv',encoding="utf-8")
        csv_data = csv.reader(data)
        employees_list = list(csv_data)
        data.close()
        
        found = 'Not found'
        for row in employees_list:
            if row[0] == name:
                if row[1] == last_name:
                    row[2] = position
                    file_to_output = open('employees.csv','w',newline='', encoding='utf-8')
                    csv_writer = csv.writer(file_to_output,delimiter=',')
                    csv_writer.writerows(employees_list)
                    file_to_output.close()
                    found = 'employer was received a raise succesfully'
                    break
        print(found)
                
                
employer = Employees()
operation = ''

while operation != 'quit' and operation != 'q':
    #Here the main code will be run
    #Ask for what operation is desired to be run or if desired to quit program
    operation = input('Try: employees, hire, raise, fire or quit to continue \n')
    
    #Flow through functions of Employees class
    if operation.lower() == 'employees':
        employer.show_employees()
        
    elif operation.lower() == 'hire':
        hire_name = input('Please enter the name \n')
        hire_last_name = input('Please enter the last name \n')
        valid_position = False
        while valid_position != True:
            hire_position = input('What is the position of the employee?\n')
            if hire_position.lower() in ['executive', 'salariedemployee', 'manager', 'hourlyemployee']:
                valid_position = True
            else:
                print("That is not a valid position please try again \n")
        try:
            hire_salary = int(input('What is the monthly salary of this employee? \n'))
            try:
                hire_rate = int(input('What is the hourly rate of this employee? \n'))
            except:
                print('That was not a valid input, the request will not proceed \n')
            else:
                employer.hire_person(hire_name, hire_last_name, hire_position, hire_salary, hire_rate)
                print('Content updated succesfully')
        except:
            print('That was not a valid input, the request will not proceed')
    
    elif operation.lower() == 'raise':
        raise_name = input("What is the name of the person you want to give a raise to? \n")
        raise_last_name = input("What is the last name of the person you want to give a raise to? \n")
        raise_position = input("What is the position you want to give him? \n")
        employer.raise_person(raise_name, raise_last_name, raise_position)
        
        
    elif operation.lower() == 'fire':
        fire_name = input("What is the name of the person you want to fire? \n")
        fire_last_name = input("What is the last name of the person you want fire? \n")
        employer.fire_person(fire_name, fire_last_name)
    
    
    elif operation.lower() == 'q' or operation.lower() == 'quit':
        print("Program closed")
    else:
        print('Not a valid input ')
        
    # pdb.set_trace()
    

    
    