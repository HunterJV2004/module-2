#Hunter Vevia
#Student GPA conditions
#Uses user defined input to determine if a student is in the honor roll, dean's list, or nothing. 
#Terminate the program when a non float is entered for the gpa or when zzz (non case dependent) is entered for the last name.
while(True):
    lastname = str(input("Enter the student's last name."))
    if lastname.lower() == "zzz":
        break
    firstname = str(input("Enter the student's first name."))
    gpa = float(input("Enter the student's GPA."))
    if gpa >= 3.5:
        print("The student has made the Dean's List")
    elif gpa >= 3.25:
        print("The student has made the Honor Roll")
        
