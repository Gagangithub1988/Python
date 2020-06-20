#employee_name=["Gagan","Bandhan","Gopal","Khirod","Manoj"]
#employee_id=["M9006960","M9008309","M9010415","M9006505","M1051946"]

employee_band=["C1","C2","C3","C4"]
def office():
    if jband in employee_band and dep_code in range(110,125):
            if emp_id=="m9006960" and jband=="C1" and dep_code == 110:
                emp1()
            elif emp_id=="m9008309" and jband=="C2" and dep_code == 111:
                emp2()
            elif emp_id == "m1051946" and jband == "C2" and dep_code == 112:
                emp3()
            elif emp_id == "m9006505" and jband == "C3" and dep_code == 113:
                emp4()
            elif emp_id == "m9010415" and jband == "C2" and dep_code == 114:
                emp5()
            else:
                print("Invalid input.")

    else:
        print("Invalid input.")

def emp1():
    print("Name: Gagan Bihari Bhoula\nMID:M9006960\nDepartment:CIS\nDesignation:AV Engineer")
def emp2():
    print("Name: Bandhan Kumar\nMID:M9008309\nDepartment:CIS\nDesignation:Senior Network Engineer")

def emp3():
    print("Name: Manoj kumar\nMID:M1051946\nDepartment:CIS\nDesignation:Senior Engineer")

def emp4():
    print("Name: Khirod Kumar\nMID:M9006505\nDepartment:CIS\nDesignation:Associate Manager")

def emp5():
    print("Name: Gopal Sahoo\nMID:M9010415\nDepartment:CIS\nDesignation:Senior Engineer")

emp_id=str(input("Employee ID: "))
jband=input("Enter the job Band: ")
dep_code=int(input("Enter the department code: "))
office()