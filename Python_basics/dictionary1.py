n=int(input("Enter the number of students:"))
d={}
for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter student marks:"))
    d[name]=marks
print(d)
while(True):
    name=input("Enter the student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("Student not found")
    else:
        print("The marks of {}:{}".format(name,marks))
    option=input("Do you want to get another student marks[Yes|No]:")
    if option=="No":
        break
print("Thanks for using our App")