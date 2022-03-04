#Changing and Adding elements in dictionary.

studentlist = int(input("enter the number of students:"))
data = []
for i in range (0,studentlist):
    name = input("enter the name:")
    subject = input("enter the subject:")
    percentage = input("enter the percentage:")
    studentdata = {
        "student name": name,
        "subject name": subject,
        "student percentage": percentage
    }
    data.append(studentdata)
    age = input("enter the age:")
    studentdata["student age"]= age
    studentdata["student age"] = 27
    print(studentdata)