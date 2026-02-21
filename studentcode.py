student={}
while True:
    print("student record system:")
    print("1.add student")
    print("2.view student list")
    print("3.search student")
    print("4.update marks")
    print("5.delete student")
    print("6.exit")
    a=int(input("choose any option:"))
    if a==1:
        name=input("enter the name of the student to add:")
        maths=int(input("enter mark in maths:"))
        physics=int(input("enter mark in physics:"))
        if name in student:
            print(name,"already exist")
        else:
            student[name]={
                "maths":maths,
                "physics":physics
            }
            print("student added succesfully")
        print("-" * 30)
    elif a==2:
        for name,marks in student.items():
            print("name:",name)
            print("maths:",marks["maths"])
            print("physics:",marks["physics"])
        print("-" * 30)
    elif a==3:
        name=input("enter the name to be searched:")
        if name in student:
            for subject,score in student[name].items():
                print(subject,":",score)
        else:
            print("student not found")
        print("-" * 30)
    elif a==4:
        name=input("enter the name:")
        if name in student:
            for subject,score in student[name].items():
                student[name][subject]=int(input(f"enter the mark in {subject}:"))
            print("updated successfully")
        else:
            print("no student found")
        print("-" * 30)
    elif a==5:
        name=input("enter the name to delete:")
        if name in student:
            student.pop(name)
            print("deleted successfully")
        else:
            print("name not found")
        print("-" * 30)
    elif a==6:
        print("program exiting")
        break
        print("-" * 30)
    else:
        print("invalid option chosen")
        print("-" * 30)