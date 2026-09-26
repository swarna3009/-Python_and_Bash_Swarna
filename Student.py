students={}
n=int(input("How many Students"))
for i in range(n):
    name = input("enter student name")
    grade=int(input("enter grade"))
    students[name]=grade
    
name = input("enter the name which you have to update")
grade = int(input("enter the gradeb to update"))
    
if name in students:
    students[name]=grade
else:
    students[name]=grade
for name ,grade in students.items():
    print(name ,":",grade)