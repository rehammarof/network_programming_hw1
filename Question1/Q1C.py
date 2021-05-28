students_list=['Reham','Sara','Abeer','Ali','Jaber']
student = input("Enter your first name: ")
for s in students_list:
    if s==student:
        print("Yes, you are graduate")
        break
else:
    print("Sorry, you are not graduate")
