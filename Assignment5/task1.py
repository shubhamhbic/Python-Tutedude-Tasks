student = {'Rahul': 85, 'Shubham':96, 'Alice':85}
name = input("Enter the student's name: ")
if name in student:
    print(name+"'s marks:", student[name])
else:
    print("Student not found.")
