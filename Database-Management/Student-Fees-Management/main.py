import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def showInfo():
  df = pd.read_csv('main.csv', index_col=0)
  info = df.loc[adminNo]
  print(info)

def getStudentClass():
    df = pd.read_csv('main.csv')
    global studentClass
    studentClass = df.iat[indexedadminNo,2]

def getLastAdminNo():
    df = pd.read_csv('main.csv')
    global lastAdminNo
    lastAdminNo = df['adminNo'].max()

def addStudent():
    getLastAdminNo()
    inputAdminNo=lastAdminNo + 1
    inputName=input(print("Enter the Student's Name: "))
    inputClass=(input("Enter the Student's Class: "))
    inputRollNo=(input("Enter the Student's Roll. No: "))
    inputFatherName=input(print("Enter the Student's Father's Name: "))
    inputMotherName=input(print("Enter the Student's Mother's Name: "))
    inputAddress=input(print("Enter the Student's Home Address: "))
    d={'adminNo':[inputAdminNo],'name':[inputName],'class':[inputClass],'rollNo':[inputRollNo],'fatherName':[inputFatherName],'motherName':[inputMotherName],'address':[inputAddress]}
    df=pd.DataFrame(d)
    df.to_csv("main.csv", mode='a', index=False, header=False)
    print("Data has been added.")
    input("Press any key to continue...")

def monthlyfee():
    df = pd.read_csv('monthlyfee.csv')
    getStudentClass()
    global studentMonthlyFee
    studentMonthlyFee = int(df.iat[studentClass,1])

def enterAdminNo():
    global adminNo
    global indexedadminNo
    adminNo=int(input("Enter The Admission No. of the Student: "))
    indexedadminNo = adminNo-1

def editStudent():
    df=pd.read_csv("main.csv")
    col=input("Enter column name to update:")
    val=input("Enter new value:")
    df.loc[df[df['adminNo']==adminNo].index.values,col]=val
    df.to_csv("main.csv",index=False)
    print("Record has been updated...")
    input("Press any key to continue...")

def inHandFees():
    global amount   

def payFees():
    inHandFees()
    amount = int(input(print('Enter the amount to pay: ')))
    d={'adminNo':[adminNo],'paidFees':[amount],'pendingFees':[0]}
    df=pd.DataFrame(d)
    df.to_csv("studentfeesummary.csv", mode='a', index=False, header=False)
    print('Fees payment has been registered')

def pendingFees():
    monthlyfee()
    df = pd.read_csv('studentfeesummary.csv')
    paid = df.iat[indexedadminNo,1]
    global pendingFees
    pendingFees = studentMonthlyFee - paid

def refreshProfile():
    pendingFees()
    df=pd.read_csv('studentfeesummary.csv')
    col=pendingFees
    df.loc[df[df['adminNo']==adminNo].index.values,col]=pendingFees
    df.to_csv("studentfeesummary.csv",index=False)
    print('Fee Profile has been updated')

def feeSummary():
    df = pd.read_csv('studentfeesummary.csv', index_col=0)
    info = df.loc[adminNo]
    print(info)

def StudentAcademicProfile():
      df = pd.read_csv('studentacademics.csv', index_col=0)
      info = df.loc[adminNo]
      print(info)

def addStudentAcademicProfile():
    test1=int(input(print('Enter the marks in Test1')))
    test2=int(input(print('Enter the marks in Test2')))
    test3=int(input(print('Enter the marks in Test3')))
    test4=int(input(print('Enter the marks in Test4')))
    test5=int(input(print('Enter the marks in Test5')))
    d={'adminNo':[adminNo],'Test 1':[test1],'Test 2':[test2],'Test 3':[test3],'Test 4':[test4],'Test 5':[test5]}
    df=pd.DataFrame(d)
    df.to_csv("studentacademics.csv", mode='a', index=False, header=False)
    print("Data has been added...")

def editAcademicProfile():
    df=pd.read_csv("studentacademics.csv")
    col=input("Enter the Test name to update:")
    val=input("Enter new value:")
    df.loc[df[df['adminNo']==adminNo].index.values,col]=val
    df.to_csv("studentacademics.csv",index=False)
    print("Record has been updated...")
    input("Press any key to continue...")

def academicGraph():
    df = pd.read_csv('studentacademics.csv', index_col=0)
    row = df.iloc[indexedadminNo]
    row.plot(kind='bar')
    plt.show()

def mainMenu():
    n=0

    enterAdminNo()

    print("                     ╔════════════════════════════════════════════╗")
    print("                     |          Student Management System         |")
    print("                     ╚════════════════════════════════════════════╝")

    while n!=6:
        print("""
              1. Show Information of Student
              2. Add a Student
              3. Edit the Student's Profile
              4. Enter the Fee Management Menu
              5. Enter the Academic Menu
              6. Exit
             """)
        
        n=int(input("Enter your choice:"))
        if n==1:
            showInfo()
        if n==2:
            addStudent()
        if n==3:
            editStudent()
        if n==4:
            FeeManagementMenu()
        if n==5:
            AcademicMenu()
        elif n==6:
            print("Exiting...")
            print("Thanks for Checking out Project!!")
            break

def FeeManagementMenu():
    print("                     ╔════════════════════════════════════════════╗")
    print("                     |            Fee Management Menu             |")
    print("                     ╚════════════════════════════════════════════╝")

    i=100
    while i!=105:
        print("""
              101. Show Fee Summary of the Student
              102. Pay Fees
              103. Pending Fees
              104. Monthly Fees of the Student
              105. Back to Main Menu
        """)
        i=int(input("Enter your choice:"))
        if i==101:
            feeSummary()
        if i==102:
            payFees()
        if i==103:
            pendingFees()
            print('The Pending Fee of student with Admission No. ',adminNo,' is ',pendingFees)
        if i==104:
            monthlyfee()
            print("The Monthly Fee of the student with Admission No.", adminNo,"is",studentMonthlyFee)
        elif i==105:
            mainMenu()

def AcademicMenu():
    print("                     ╔════════════════════════════════════════════╗")
    print("                     |          Student's Academics Menu          |")
    print("                     ╚════════════════════════════════════════════╝")

    s=200
    while s!=205:
        print("""
              201. Show Student's Academic Profile
              202. Add Student's Profile
              203. Edit Student's Profile
              204. Get Graphical Representation of Student's Scores
              205. Back to Main Menu
        """)
        s=int(input("Enter your choice:"))
        if s==201:
            StudentAcademicProfile()
        if s==202:
            addStudentAcademicProfile()
        if s==203:
            editAcademicProfile()
        if s==204:
            academicGraph()
        elif s==105:
            mainMenu()

mainMenu()