# HW1 DAY.4

# Question 1
# Course Grade Application
studentinformationlist = []
startbold = "\033[1m"
endbold = "\033[0m"
ogrencisay = 2
for i1 in range(ogrencisay):
    studentinformation = {}
    studentname = input(str(i1+1) + ". Öğrenci isim ve soyadını giriniz: ")
    while True:
        midtermgrade = input(str(i1+1) + ". Öğrencinin ara sınav notunu giriniz (0-100 aralığında): ")
        try:
            midtermgrade_int = int(midtermgrade)
            if midtermgrade_int>=0 and midtermgrade_int<101:
                break;
            else:
                print(startbold + "0-100" + endbold + " aralığında bir sayı giriniz")
        except ValueError:
            print("0-100 aralığında bir " + startbold + "sayı" + endbold + " giriniz")
    while True:
        projectgrade = input(str(i1+1) + ". Öğrencinin proje notunu giriniz (0-100 aralığında): ")
        try:
            projectgrade_int = int(projectgrade)
            if projectgrade_int>=0 and projectgrade_int<101:
                break;
            else:
                print(startbold + "0-100" + endbold + " aralığında bir sayı giriniz")
        except ValueError:
            print("0-100 aralığında bir " + startbold + "sayı" + endbold + " giriniz")
    while True:
        finalgrade = input(str(i1+1) + ". Öğrencinin dönem sonu sınav notunu giriniz (0-100 aralığında): ")
        try:
            finalgrade_int = int(finalgrade)
            if finalgrade_int>=0 and finalgrade_int<101:
                break;
            else:
                print(startbold + "0-100" + endbold + " aralığında bir sayı giriniz")
        except ValueError:
            print("0-100 aralığında bir " + startbold + "sayı" + endbold + " giriniz")              
    passinggrade_int = int(midtermgrade_int*0.3 + projectgrade_int*0.3 + finalgrade_int*0.4)
    #studentinformation[studentname]=[midtermgrade_int,projectgrade_int,finalgrade_int,passinggrade_int]
    studentinformation['studentname'] = studentname
    studentinformation['midtermgrade'] = midtermgrade_int
    studentinformation['projectgrade'] = projectgrade_int
    studentinformation['finalgrade'] = finalgrade_int
    studentinformation['passinggrade'] = passinggrade_int
    studentinformationlist.append(studentinformation)
studentinformationlist.sort(key=lambda k : k['passinggrade'], reverse=True)   
studentinformationlist
