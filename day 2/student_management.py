print("program started")
student =[]
while True:
    print("\n.STUDENT MANAGEMENT")
    print("1.Add student")
    print("2.View student")
    print("3.Search student")
    print("4.Update student")
    print("5.Delete student")
    print("6.Marks")
    print("7.Top performer")
    print("8.Remove Duplicates")
    print("9.Exit")
    choice = int(input("enter your choice: "))
    print("You have entered:",choice)
    if choice == 1:
        name=input("enter name: ")
        marks=int(input("enter marks: "))
        student.append([name,marks])
        print(student)
        print("student added")
    elif choice == 2:
        print("choice 2 reached")
        print(student)
        for i in student:
            print(i)
    elif choice == 3:
        search=input("enter student name: ")
        found = False
        for i in student:
            if i[0] == search:
                print("student found")
                print(i)
                found = True
                break
        if not found:
            print("student not found")
    elif choice == 4:
        search = input("enter name to update: ")
        for i in student:
            if i[0] == search:
                i[1] = int(input("Enter new marks: "))
                print("updated successfully")
                break
    elif choice == 5:
        search=input("enter name to delete:")
        for i in student:
            if i[0] == search:
                student.remove(i)
                print("removed successfully")
                break
    elif choice == 6:
        student.sort(key=lambda x: x[1])
        for i in student:
            print(i)
    elif choice == 7:
        if len(student) == 0:
            print("No students found")
        else:
            top = student[0]

            for i in student:
                if i[1] > top[1]:
                    top = i
            print("Top Performer:")
            print(top)
    elif choice == 8:
        names = []
        for i in student:
            names.append(i[0])
        names = list(set(names))
        print(names)
    elif choice == 9:
        print("Exiting...")
        break