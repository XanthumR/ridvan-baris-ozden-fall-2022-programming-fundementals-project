def listallcourses():
    file = open("course.txt","r")
    for er in file:
        ty=er.split(";")
        print(ty[1])
    file.close()
def listallcoursesatleast1student():
    file = open("course.txt","r")
    for er in file:
        ty=er.split(";")
        if int(ty[3])> 0 :
            print(ty[1])
def addnewcourse(coursecode,coursename,teacher):
    u = [coursecode.upper(),coursename,teacher,"0"]
    my = open("course.txt","a")
    for i in range(4):
        if i != (3):
            my.write(u[i] + ";")
        elif i == (3):
            my.write(u[i]+"\n")
    my.close()
def searchacoursebycode():
    row = open("course.txt","r")
    o=row.readlines()
    while True:
        b = True
        a=input("enter coursecode if you want to exit write break")
        uppera =a.upper()
        for i in range(len(o)):
            if uppera in o[i].split(";"):
                print(o[i].split(";")[1])
                b=False
        if b and a !="break":
            print("tryagain")
        elif a =="break":
            break
def searchacoursebyname():
    while True:
        row = open("course.txt","r")
        b = True
        a=input("enter course name if you want to exit write break")
        for i in row:
            if a in i:
                print(i.split(";")[1])
                b=False
        if b and a != "break":
            print("tryagain")
        elif a =="break":
            break
def registerstudent(studentid,coursecode):
    addedstudent = []
    courses = []
    students = []
    studentid = str(studentid)
    coursecod = coursecode.upper()
    row = open("student.txt","r")
    row34 = open("course.txt","r")
    for iz in row34:
        lop = iz.split(";")
        courses.append(lop[0])
    for i in row:
        d =i.split(";")
        students.append(d[0])
        for op in range(3):
            addedstudent.append(d[op])
    valu1=0
    velu2=2
    dfg = True
    for n in range(int(len(addedstudent)/3)):
        if studentid not in students:
            print("wrong student id")
            break
        elif studentid in addedstudent[valu1]:
            if coursecod not in addedstudent[velu2] and coursecod in courses:
                addedstudent[velu2]=addedstudent[velu2].replace("\n","").__add__(coursecod+","+"\n")
            else:
                print("try again this student is already registered to "+coursecod+" or you entered the wrong coursecode")
                dfg = False

        valu1= valu1+3
        velu2 = velu2+3
    vc = []

    row2 = open("course.txt","r")
    for lo in row2:
        dez = lo.split(";")
        for opc in range(4):
            vc.append(dez[opc])
    mk=0
    for ok in range(int(len(vc)/4)):
        if coursecod in vc[mk] and dfg and studentid in students:
            vc[mk+3]= str((int(vc[mk+3].replace("\n",""))+1))+"\n"
        mk = mk +4

    row3 = open("course.txt","w")
    mn=0
    mo =3
    mp=[]
    for tuv in range(len(vc)):
        mp.append(mo)
        if mn not in mp:
            row3.write(vc[mn]+";")
        elif mn in mp:
            row3.write(vc[mn])
        mn =mn+1
        mo = mo+4
    row1 = open("student.txt","w")
    h = 0
    g = 2
    uh = []
    for po in addedstudent:
        uh.append(g)
        if h not in uh:
                row1.write(po + ";")
        elif h in uh:
                row1.write(po)
        h=h+1
        g=g+3
    row1.close()
def listallcoursetostudent():
    row = open("student.txt","r")
    for i in row:
        lok =0
        split = i.split(";")
        print("\n"+split[1])
        row1 = open("course.txt","r")
        for ip in row1:
            split1 = ip.split(";")
            if split1[0] in split[2]:
                print(split1[1])
                lok = lok +1
        if lok ==0:
            print([])
while True:

    print("press 1 to list all the courses"+"\n"+
          "press 2 to list all the course that have at least one student registered"+"\n"+
          "press 3 to add a new course "+"\n"+
          "press 4 to search a course by coursecode"+"\n"+
          "press 5 to search a course by course name"+"\n"+
          "press 6 to register a student to a course"+"\n"+
          "press 7 to list all the students and their registered course"+"\n"+
          "press 8 to save all changes"+"\n"+
          "press 9 to exit (exit's without saving)")
    a = int(input())
    if a == 1 :
        listallcourses()
    elif a ==2:
        listallcoursesatleast1student()
    elif a == 3:
        coursecode=input("enter course code you want to add")
        coursename=input("enter course name you want to add")
        teacher = input("enter teacher of your course you want to add")
    elif a == 4:
        searchacoursebycode()
    elif a== 5:
        searchacoursebyname()
    elif a ==6:
        studentid= input("please enter the student id of the student you want to register to a course")
        coursecode1= input("please enter the course code you want the student to register")

    elif a ==7:
        listallcoursetostudent()
    elif a==8:
        try:
            addnewcourse(coursecode,coursename,teacher)
        except:
            pass
        try:
            registerstudent(studentid,coursecode1)
        except:
            pass
    elif a== 9 :
        break
