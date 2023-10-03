print("WELCOME TO ABC IIT-JEE/MEDICAL COACHING INSTITUTE")
tfees=106400                                                            # Two Year Total Fees
ofees=102400                                                            # One Year Total Fees
bfees=45000                                                              # Booster Course Fees
dfees=35000                                                              #Dumee School Charges

import mysql.connector                                         #Importing module
passwd=input("ENTER PASSWORD : ")

mysql=mysql.connector.connect(host="localhost",user="root",passwd=passwd,charset="utf8")#Establishing connection
mycursor=mysql.cursor()

mycursor.execute("create database if not exists PHSS")  #Creating Database
mycursor.execute("use PHSS")

#Creating the necessary Tables
mycursor.execute("create table if not exists JEE(name varchar(30),fathername varchar(30),mothername varchar(30),gender varchar(30),DOB  varchar(30) ,contact int(10),adress varchar(50),username varchar(50) primary key)")
mycursor.execute("create table if not exists NEET(name varchar(50),fathername varchar(50),mothername varchar(50),gender varchar(50),DOB  varchar(50) ,contact int(10),adress varchar(50),username varchar(50) primary key)")
mycursor.execute("create table if not exists Faculty(name varchar(50),DOB varchar(50),gender varchar(10),degree varchar(50),contact int(10),address varchar(50),username varchar(50) primary key)")

mycursor.execute("create table if not exists userdata(username varchar(50) primary key,password varchar(50) default'123')")


                 #Loop for  the Main Menu
while(True):
        print("""
             Main Menu
             1:)About Us
             2:)Our Results
             3:)Fee Structure
             4:)New admission
             5:)Faculty Application
             6:)Login
             7:)EXIT
           """)
        a=int(input("Enter choice-->>"))
        #First Option-About Us
        if a==1 :
            print("\nFirst of all memorising everything for the students has been become very difficult.")
            print("The major outcome of our institute is to overcome this problems.")
            print("\nTo overcome this:-")
            print("\t-->Personal attention is given to all the students.")
            print("\t-->We have developed various activities so that it becomes easy for the students to remember it.")
            print("\t-->Students are provided with practice sheets so that the concept gets clear.")
            print("\t-->We also take students to science tours.")
            print("\t-->Extra lectures are taken so that the doubt gets clear.")
            print("\nOur institute have successfully completed 15 years.")
            print("Teachers also have a teaching experience of about 10 years")
            print("\n\t\t\t......Thank you for reading......")
            input("\n\t\t  >>Press Enter :--")
        #Second Option-Our Results
        elif a==2 :
            print("\t\t\t\t\t\t\t..........Our Result..........")
            
            print("""                                                             (2021-2022)""")
            print("\n\n\t\tSr No.\t\t\t   Name of\t\t\t\tAll India\t\t\t    \tTotal")
            print("\t\t\t\t\t   Student\t\t  \t \t Rank\t\t\t\t    Marks")
            print("\n\n\t\t  1.\t\t\t  Manoj Kumar\t\t\t  [5]\t\t\t\t   325/360")
            print("\t\t  2.\t\t\t  Shrey Choksi\t\t\t  [12]\t\t\t\t   315/360")
            print("\t\t  3.\t\t\t  Priya Junjunwala\t\t \t   [18]\t\t\t\t   298/360")
            print("\t\t  4.\t\t\t  Raj Daruwala\t\t\t  [29]\t\t\t\t   291/360")
            print("\t\t  5.\t\t\t  Kusum Shah\t\t\t  [105]\t\t\t\t   275/360")
            print("\t\t  6.\t\t\t  Mukesh Ambani\t\t\t  [421]\t\t\t\t   200/360")
            print("\t\t  7.\t\t\t  Dev Hashmukh\t\t\t  [501]\t\t\t\t   187/360")
            print("\t\t  8.\t\t\t  Vanshika Choksi\t\t         \t  [1024]\t\t\t  \t   145/360")
            print("\t\t  9.\t\t\t  Krishna Shah\t\t\t  [5990]\t\t\t   \t   125/360")
            print("\t\t  10.\t\t\t  Saumya Sheth\t\t\t  [8000]\t\t\t\t   110/360")
            print("\n\n\t\t\t\t-->>We assure you the best result.")
            print("\t\t\t\t-->>Hope to get a successfull response")
            input("\n\t\t  >>Press Enter :--")
            
        #Third Option-Fee Structue   
        elif a==3 :
            while True:
                print("""\n    1.    2 Years Total Fees (Physics + Chemistry + Maths/Biology)
    2.    One Year Total Fees (Physics + Chemistry + Maths/Biology)  (For 12 th Std )
    3.    Booster Course Fees ( For Droppers)
    4.    Dumee Charges
    5.    Exit""")
                c=input("\nEnter Number(1,2,3,4,5):--")
                if c=='1':
                    x1,y1,z1=7093.3,7093.3,7093.3
                    x2,y2,z2=7093.3,7093.3,7093.3
                    x3,y3,z3=7093.3,7093.3,7093.3
                    x4,y4,z4=4729,4729,4729
                    x5,y5,z5=4729,4729,4729
                    x6,y6,z6=4729,4729,4729
                    s1=x1+y1+z1
                    s2=x2+y2+z2
                    s3=x3+y3+z3
                    s4=x4+y4+z4
                    s5=x5+y5+z5
                    s6=x6+y6+z6

                    T1=s1+s2+s3+s4+s5+s6
                    
                    print("""\n\t\t~~~>""")
                    print("\n\t\t\t\tMonth\t\t\tPhysics\t\t\tChemistry\t\t\tMaths/Biology\t\t\tTotal")
                    print("""\n\t\t\t              March2022\t\t                   (7093.3                    +                    7093.3                    +                    7093.3)                    ~~~~>>                    """,s1)
                    print("""\n\t\t\t              August2022\t\t                   (7093.3                    +                    7093.3                    +                    7093.3)                    ~~~~>>                    """,s2)
                    print("""\n\t\t\t             December2022\t                    (7093.3                   +                    7093.3                    +                    7093.3)                    ~~~~>>                    """,s3)
                    print("""\n\t\t\t              March2023\t\t                    (4729                      +                        4729                    +                       4729)                    ~~~~>>                    """,s4)
                    print("""\n\t\t\t              August2023\t\t                    (4729                      +                        4729                    +                       4729)                    ~~~~>>                    """,s5)
                    print("""\n\t\t\t             December2023\t                   (4729                       +                        4729                    +                        4729)                    ~~~~>>                    """,s6)
                    print("\n Therfore\n\t\tTotal Fees is~~>",T1)
                    input("\n\t\t  >>Press Enter :--")
                    
                if c=='2':
                    x1,y1,z1=11378,11378,11378
                    x2,y2,z2=11378,11378,11378
                    x3,y3,z3=11378,11378,11378
                   
                    s1=x1+y1+z1
                    s2=x2+y2+z2
                    s3=x3+y3+z3
                    T1=s1+s2+s3
                    
                    
                    print("""\n\t\t~~~>""")
                    print("\n\t\t\t\tMonth\t\t\tPhysics\t\t\tChemistry\t\t\tMaths/Biology\t\t\tTotal")
                    print("""\n\t\t\t              March2023\t\t                   (11378                    +                    11378                    +                    11378)                    ~~~~>>                    """,s1)
                    print("""\n\t\t\t              August2023\t\t                   (11378                    +                    11378                    +                    11378)                    ~~~~>>                    """,s2)
                    print("""\n\t\t\t             December2023\t                    (11378                   +                    11378                    +                    11378)                    ~~~~>>                    """,s3)
                    print("\n Therfore\n\t\tTotal Fees is~~>",T1)
                    input("\n\t\t  >>Press Enter :--")
                        
                          
                if c=='3':
                    x1,y1,z1=5000,5000,5000
                    x2,y2,z2=5000,5000,5000
                    x3,y3,z3=5000,5000,5000
                   
                    s1=x1+y1+z1
                    s2=x2+y2+z2
                    s3=x3+y3+z3

                    T1=s1+s2+s3
                    
                    print("""\n\t\t~~~>""")
                    print("\n\t\t\t\tMonth\t\t\tPhysics\t\t\tChemistry\t\t             Maths/Biology\t\t        Total")
                    print("""\n\t\t\t              March2023\t\t                   (5000                    +                    5000                    +                    5000)                    ~~~~>>                    """,s1)
                    print("""\n\t\t\t              April2023\t\t                   (5000                    +                    5000                    +                    5000)                    ~~~~>>                    """,s2)
                    print("""\n\t\t\t             May2023\t\t                    (5000                   +                    5000                    +                    5000)                    ~~~~>>                    """,s3)
                    print("\n Therfore\n\t\tTotal Fees is~~>",T1)
                    input("\n\t\t  >>Press Enter :--")


                if c=='4':
                        print("\n\tExtra Charges For Dumee Will be Rs35000")
                        input("\n\t\t  >>Press Enter :--")

                if  c=='5':
                        break

            

        

        
        # Fourth option- New Admission

        
        
        elif a==4 :
            #Inputting the Data
            nme=input("\nENTER YOUR NAME : ")
            fnme=input("\nENTER FATHER NAME : ")
            mnme=input("\nENTER MOTHER NAME : ")
            gen=input("\nGENDER :")
            ad1=input("\nADDRESS LINE 1:")
            dob=(input("\nBIRTH DATE : "))
        
            ph1=input("\nCONTACT NUMBER :")
        
            eml=input("\nEMAIL ID : ")
            pass1=input("\nPASSWORD : ")
            mycursor.execute("insert into userdata values('"+eml+"','"+pass1+"')")
            
            dum=input("\nDO YOU WANT US TO ALLOT A DUMME SCHOOL?(EXTRA CHARGES OF DUMME SCHOOL WILL APPLY)(Y/N) ")
            
            print("\n\tFollowing courses are avalable-->>")

            
            crs=int(input("""\n
                           1:)2 YEAR COURSE FOR JEE MAINS & ADVANCED
                           2:)2 YEAR COURSE FOR NEET
                           3:)1 YEAR COURSE FOR JEE MAINS & ADVANCED(FOR 12 STANDARD STUDENTS)
                           4:)1 YEAR COURSE FOR NEET(FOR 12 STANDARD STUDENTS)
                           5:)BOOSTER COURSE FOR JEE MAINS AND ADVANCED(FOR DROPPERS)
                           6:)BOOSTER COURSE FOR NEET(FOR DROPPERS)
                           ENTER CHOICE : """))
            #Storing the Data
            if crs==1 or crs==3 or crs==5 :
                    mycursor.execute("insert  into JEE values('"+nme+"','"+fnme+"','"+mnme+"','"+gen+"','"+dob+"','"+ph1+"','"+ad1+"','"+eml+"')")
                    mysql.commit()
                    print("SUCCESFULLY REGISTERED")

            if crs==2 or crs==4 or crs==6 :
                    mycursor.execute("insert into NEET values('"+nme+"','"+fnme+"','"+mnme+"','"+gen+"','"+dob+"','"+ph1+"','"+ad1+"','"+eml+"')")
                    mysql.commit()
                    print("SUCCESFULLY REGISTERED")
           

        

           # If the User choose course 1 or 2
            if crs==1 or crs==2 :
                
                    
                print("\nWE HAVE A SCHOLARSHIP TEST FOR 2 YEAR COURSE STUDENTS ")
                sch=input("\nDO U WANT TO GIVE THE SCHOLARSHIP EXAM(Y/N)? ")                                                        # sch=Scholarship Test

                if sch=="Y" :
                    
                    print(""" \nWELCOME TO THE SCHOLARSHIP TEST.\n\t\t\n THE TEST WILL CONSIST OF
                               PHYSICS ,CHEMISTRY ,MATHEMATICS/BIOLOGY \t\t(60 MARKS ) (Syllabus-X std)
                                                                                (+4 Marks,-1 Marks)""")

                    print("""          ******PHYSICS*********""")                                                                                                               #pq=Physics Questions


                    pq1="""Q1)THE BEST MATERIAL TO MAKE PERMANENT MAGNET IS : 
                           (A)ALUMINIUM
                           (B)SOFT IRON
                           (C)COPPER
                           (D)ALNICO
                           """
                    pq2="""Q2) THE DIRECTION OF INDUCED CURRENT IS GIVEN BY : 
                           (A)FLEMING'S RIGHT HAND RULE
                           (B)FLEMING'S LEFT HAND RULE
                           (C)RIGHT HAND THUMB RULE
                           (D)LEFT HAND THUMB RULE
                           """
                    pq3="""Q3) MAGNIFYING POWER OF A CONCAVE LENS IS : 
                           (A)ALWAYS > 1
                           (B)ALWAYS < 1
                           (C)ALWAYS = 1
                           (D)CAN HAVE ANY VALUE
                           """
                    pq4="""Q4) IF THE POWER OF A LENS IS -2D,WHAT IS ITS FOCAL LENGTH ? 
                           (A)+50 cm
                           (B)-100 cm
                           (C)-50 cm
                           (D)+100 cm
                           """
                    pq5="""Q5) 100 J OF HEAT IS PRODUCED EACH SECOND IN A 4ohm RESISTOR.THE POTENTIAL DIFFERENCE
                            ACROSS THE RESISTOR WILL BE :
                            (A)30 V
                            (B)10 V
                            (C)20 V
                            (D)25 V
                            """

                    pqst={pq1:"D",pq2:"A",pq3:"B",pq4:"C",pq5:"B"}                                         #pqst=Physics answer key                  
                    mks=0
                    # Calculation of physics marks
                    for i in pqst :
                        print(i)
                        pans=input("ANSWER : ")                                                                             #mks=Marks

                        if pans==pqst[i] :
                            mks+=4
                        elif  pans==None :
                            mks=mks
                        
                        else :
                            mks-=1

                    print("                 ***********CHEMISTRY**************               )")                                                                                        #Chemistry Questions


                    cq1="""Q1)WHICH OF THE FOLLOWING IS NOT AN ALKALINE EARTH METAL ? :
                              (A)STRONTIUM(Sr)
                              (B)MAGNESIUM(Mg)
                              (C)BERYLLIUM(Be)
                              (D)BARIUM(Ba)
                              """
                    cq2="""\nQ2)WHICH OF THE FOLLOWING IS PREPARED BY "SOLVAY'S PROCESS" ?
                              (A)CAUSTIC SODA
                              (B)BLEACHING POWDER
                              (C)BRINE
                              (D)WASHING SODA
                              """
                    cq3="""\nQ3)SOAPS ARE FORMED BY THE SAPONIFICATION OF ?
                              (A)ALCHOHOL
                              (B)CARBOXYLIC ACID
                              (C)SIMPLE ESTER
                              (D)GLYCERIDES
                              """
                    cq4="""\nQ4)SOLUBLITY OF ALCHOHOL IN WATXER IS DUE TO ?
                              (A)LOW DENSITY
                              (B)VOLATILE NATURE
                              (C)HYDROGEN BONDING
                              (D)IONISATION
                              """
                    cq5="""\nQ5)SCANDIUM(Sc) BELONGS TO WHICH GROUP ?
                              (A)GROUP 3
                              (B)GROUP 4
                              (C)GROUP 5
                              (D)GROUP 6
                         """
                    cqst={cq1:"C",cq2:"D",cq3:"D",cq4:"C",cq5:"A"}                                                                                              #cqst=Chemistry Answer Key
                    #Calculation of Chemistry Marks 
                    for j in cqst :
                        print(j)

                        cans=input("ANSWER : ")

                        if cans==cqst[j] :
                            mks=mks+4
                        elif  cans==None :
                            mks=mks
                        else :
                            mks-=1

                    #If the user choose course one the Maths Game will get displayed
                    if crs==1 :
                       print("             ******MATHEMATICS**********             ")                                                                                                   #Maths Questions
 
                       mq1="""Q1) FIND THE AREA OF THE TRIANGLE BOUNDED BY THE COORDINATES 
                                 (-3,4);(1,-2);(5,5).
                                 (A)24
                                 (B)27
                                 (C)26
                                  (D)20
                                 """
                       mq2="""Q2) THE PARABOLA OF THE EQUATION : y^2-4x=0 WILL
                                   (A)OPEN UPWARDS
                                   (B)OPEN LEFTWARDS
                                   (C)OPEN RIGHTWARDS
                                   (D)OPEN DOWNWARDS
                                   """
                       mq3="""Q3) SLOPE OF THE LINE JOINING (12,3) and (15,16) IS :
                                   (A)13/3
                                   (B)15/16
                                   (C)8/5
                                   (D)1
                                   """
                       mq4="""Q4) WHICH OF THE FOLLOWING IS INCORRECT ?
                                   (A)sinAcosA+cosBsinB=cos(A+B)
                                   (B)sec^2 A - tan^2 A=1
                                   (C)sin^2 A + cos^2 A =1
                                   (D)sin2A=2sinAcosA
                                   """
                       mq5="""Q5) WHICH SEQUENCE IS THIS?
                                   0,1,1,2,3,5,8,13,21,....
                                   (A)AP
                                   (B)GP
                                   (C)A.G.P.
                                   (D)FIBONACCI SERIES
                                   """
                       mqst={mq1:"C",mq2:"B",mq3:"A",mq4:"A",mq5:"D"}                                                                           #mqst=Maths Answer key

                      #Calculation of Maths Marks
                       for k in mqst :
                           print(k)
                           mans=input("ANSWER : ")

                           if mans==mqst[k] :
                               mks=mks+4
                           elif  mans==None :
                               mks=mks
                           else :
                                mks-=1

                   #If the user chooses course 2 , then Biology Paper will get displayed
                    if crs==2 :
                        
                       print("""            *********BIOLOGY********           """ )                                                                                            #Biology Questions


                       bq1="""Q1)WHICH PLANT HORMONE PROMOTES CELL DIVISION  
                               (A)AUXIN
                               (B)GIBBERELLIN
                               (C)CYTOKININ
                               (D)ABSCISIC ACID
                               """
                       bq2="""Q2)POSTURE AND BALANCE OF THE BODY iS CONTROLLED BY
                               (A)CEREBELLUM
                               (B)MEDULLA OBLONGATTA
                               (C)PONS
                               (D)CEREBRUM
                           """
                       bq3="""Q3)GLYCOLYSIS PROCESS OCCURS IN WHICH PART OF THE CELL ?
                               (A)NUCLEUS
                               (B)CYTOPLASM
                               (C)MITOCHONDRIA
                               (D)CHLOROPLAST
                               """
                       bq4="""Q4)THE MOVEMENT OF FOOD IS CALLED ?
                               (A)TRANSPIRATION
                               (B)TRANSLOCATION
                               (C)RESPIRATION
                               (D)EVAPORATION
                                  """
                       bq5="""Q5)WHICH OF TH FOLLOWING IS THE ANCESTOR OF 'BROCCOLI' ?
                               (A)CABBAGE
                               (B)CAULIFLOWER
                               (C)WILD CABBAGE
                               (D)KALE
                               """

                       bqst={bq1:"C",bq2:"A",bq3:"B",bq4:"B",bq5:"C"}                                                                                           #bqst=Biology Answer Set

                       #Calculation of Biology Marks
                       for m in bqst:
                          
                          print(m)
                          bans=input("ANSWER : ")

                          if bans==bqst[m]:
                              mks=mks+4
                          elif  bans==None :
                              mks=mks
                          else :
                              mks-=1

  

            # Calculation Discount in fees according to the marks in above test
            if (crs==1 or crs==2) and (sch=="Y") :
                print("\nTHANK YOU FOR TAKING THE QUIZ")
                print("\nYOU SCORED\n\t ",mks,"/60")
                if mks>=50  :
                    tfees=0.55*tfees
                elif mks>=40 and mks<50 :
                    tfees=0.8*tfees
                elif mks>=25 and mks<40 :
                    tfees=0.95*tfees

                else :
                    tfees=tfees
            else :
                tfees=tfees
                
              #Displaying Final Fees to be paid          
            print("\n********FINAL FEE ********")

            #Adding over charges for dummee school
            if dum=="Y" :
                dfees=35000
            else :
                dfees=0

           
           #Calculating the fees by Installments
            if crs==1 or crs==2 :
                ins1=round(tfees*0.2,2)
                ins2=ins1
                ins3=ins1
                ins4=round(tfees*(40/300),2)
                ins5=ins4
                ins6=ins4
                ffs=round(ins1+ins2+ins3+ins4+ins5+ins6+dfees,2)

            elif crs==3 or crs==4 :
                ins1=round(ofees*(1/3),2)
                ins2=ins1
                ins3=ins1
                ffs=round(ins1+ins2+ins3+dfees,2)
            else :
                ins1=round(bfees*(1/3),2)
                ins2=ins1
                ins3=ins1
                ffs=round(ins1+ins2+ins3,2)


               


                   
        
           
           #Displaying the fees by installments
            if crs==1 or crs==2 :
                print("\nMARCH 2022 INSTALLMENT : Rs. ",ins1," ONLY ")
                print("\nAUGUST 2022 INSTALLMENT : Rs. ",ins2," ONLY")
                print("\nDECEMBER 2022 INSTALLMENT : Rs. ",ins3, " ONLY")
                print("\nMARCH 2023 INSTALLMENT : Rs. ",ins4," ONLY")
                print("\nAUGUST 2023 INSTALLMENT : Rs. ",ins5," ONLY")
                print("\nDECEMBER 2023 INSTALLMENT : Rs. ",ins6," ONLY")
                print("\nTOTAL FEES : Rs.",ffs," ONLY ")
            elif crs==3 or crs==4:
                print("\nMARCH 2023 INSTALLMENT : Rs. ",ins1," ONLY")
                print("\nAUGUST 2023 INSTALLMENT : Rs. ",ins2," ONLY")
                print("\nDECEMBER 2023 INSTALLMENT : Rs. ",ins3," ONLY")
                print("\nTOTAL FEES : Rs.",ffs," ONLY ")
            else :
                print("\nMARCH 2024 INSTALLMENT : Rs. ",ins1," ONLY")
                print("\nAPRIL 2024 INSTALLMENT : Rs. ",ins2," ONLY")
                print("\nMAY 2024 INSTALLMENT : Rs. ",ins3," ONLY")
                print("\nTOTAL FEES : Rs. ",ffs," ONLY ")
                                




            dec=input("\nDO YOU WANT TO CONFIRM YOUR ADMISSION ?(Y/N)")                                                         #dec=Confirm Admission or not???

            import random
        
            if dec=="Y" :
                print("\nYOUR ADMISSION HAS BEEN CONFIRMED")

                rno=random.randint(1000000,9999999)                                                                                                                                     #rno=Roll Number
                print("\nYOUR ROLL NO. IS :  ",rno)
            
            else :
                print("\nPLEASE TELL US WHERE TO IMPROVE AND GIVE A FEEDBACK")
                fdbck=input(" FEEDBACK : ")                                                                                                                                             #fdbck=Feedback
            

         #Fifth Option-Faculty Application
        elif a==5:
            #Inputting Data
                nme=input("ENTER YOUR NAME : ")
                dob=input("ENTER YOUR DATE OF BIRTH : ")
                gen=input("ENTER YOUR GENDER : ")
                degree=input("ENTER YOUR DEGREE : ")
                phno=input("ENTER YOUR CONTACT NO. : ")
                add=input("ENTER YOUR ADDRESS : ")

                eml=input("\nEMAIL ID : ")
                pass1=input("\nPASSWORD : ")
                mycursor.execute("insert into userdata values('"+eml+"','"+pass1+"')")
                #Storing Data
                mycursor.execute("insert into Faculty values('"+nme+"','"+dob+"','"+gen+"','"+degree+"','"+phno+"','"+add+"','"+eml+"')")
                mysql.commit()
                print("YOU ARE SUCCESFULLY REGISTERED ! ")
                print("BRANCH WILL CONTACT YOU AT THE EARLIEST")
                
                


        #Option 6-User Login
        elif a==6:
            #inputing user id and password
                
           user=input("ENTER EMAIL ID ")
           pw1=input("ENTER PW ")

           mycursor.execute("select password from userdata where (username='"+user+"')")
           row=mycursor.fetchall()
           zyx=mycursor.rowcount
           
           #authenticating user id and password
           for i in row:
                    xa=list(i)
                    if  zyx!=0 and xa[0]==str(pw1) :
           
                        #Login Menu
                        while(True):
                            print(""" 1.VIEW YOUR DETAILS
2.UPDATE YOUR DETAILS
3.DELETE YOUR DATA
4.EXIT
                                           """)
                            xyz=int(input("ENTER CHOICE : "))
                            #Option to view the details
                            if xyz==1 :
                                    yz=int(input("""1.JEE STUDENT
2.NEET STUDENT
3.APPLIED FOR FACULTY
ENTER CHOICE : """))
                                    if yz==1 :
                                            mycursor.execute("select* from JEE where(username='"+user+"')")
                                            row=mycursor.fetchall()

                                            if mycursor.rowcount==0 :
                                                print("You have deleted your records")
                                            else :
                                                
                                        
                                                for i in row:
                                                        v=list(i)
                                                        k=["NAME ","FATHER'S NAME","MOTHER'S NAME","GENDER","DATE OF BIRTH","CONTACT NO.","ADDRESS","USERNAME"]
                                                        d=dict(zip(k,v))
                                                        print(d)
                                    
                                                            

                                    if yz==2:
                                            mycursor.execute("select* from NEET where(username='"+user+"')")
                                            row=mycursor.fetchall()

                                            if mycursor.rowcount==0 :
                                                print("You have deleted your records")
                                            else :

                                                    for i in row:
                                                            v=list(i)
                                                            k=["NAME ","FATHER'S NAME","MOTHER'S NAME","GENDER","DATE OF BIRTH","CONTACT NO.","ADDRESS","USERNAME"]
                                                            d=dict(zip(k,v))
                                                            print(d)


                                    if yz==3:
                                            mycursor.execute("select* from Faculty where(username='"+user+"')")
                                            row=mycursor.fetchall()

                                            if mycursor.rowcount==0 :
                                                print("You have deleted your ")
                                            else :

                                                    for i in row:
                                                            v=list(i)
                                                            k=["NAME","DOB","GENDER","DEGREE","CONTACT NO. ","ADDRESS","USERNAME"]
                                                            d=dict(zip(k,v))

                                                            print(d)
                            #Option to Modify the details
                            elif xyz==2 :
                                    yz=int(input("""1.JEE STUDENT
2.NEET STUDENT
3.APPLIED FOR FACULTY
ENTER CHOICE : """))
                                    if yz==1 or yz==2 :
                                                            nme=input("ENTER NEW NAME : ")
                                                    
                                                            fnme=input("ENTER FATHER NAME : ")
                                                    
                                                            mnme=input("ENTER MOTHER NAME : ")
                                                    
                                                            gen=input("ENTER GENDER : ")
                                                    
                                                            dob=input("ENTER DOB : ")
                                                    
                                                            phno=input("ENTER CONTACT NO. : ")
                                                    
                                                            add=input("ENTER NEW ADDRESS : ")
                                                    
                                                            
                                                            mycursor.execute("update JEE set name='"+nme+"',fathername='"+fnme+"',mothername='"+mnme+"',gender='"+gen+"',DOB='"+dob+"',contact='"+phno+"',adress='"+add+"' where(username='"+user+"')")
                                                            mycursor.execute("update NEET set name='"+nme+"',fathername='"+fnme+"',mothername='"+mnme+"',gender='"+gen+"',DOB='"+dob+"',contact='"+phno+"',adress='"+add+"' where(username='"+user+"')")
                                            
                                    if yz==3 :
                                        
                                                    
                                                            nme=input("ENTER NEW NAME : ")
                                                   
                                                    
                                                            dob=input("ENTER DOB : ")

                                                
                                                            gen=input("ENTER GENDER : ")
                                                    
                                                            degree=input("ENTER DEGREE : ")
                                                    
                                                            phno=input("ENTER NEW CONTACT : ")
                                                    
                                                            add=input("ENTER NEW ADDRESS : ")
                                                    
                                                         
                                                            mycursor.execute("update Faculty set name='"+nme+"',DOB='"+dob+"',gender='"+gen+"',degree='"+degree+"',contact='"+phno+"',address='"+add+"' where(username='"+user+"')")         
                                                           
                                                            
                                                            
                                            





                            #Option to delete the details        
                            elif xyz==3 :
                                    yz=int(input("""1.JEE STUDENT
2.NEET STUDENT
3.APPLIED FOR FACULTY
ENTER CHOICE : """))
                                    if yz==1 :
                                            chc=input("ARE YOU SURE ? YOUR ALL DATA WILL BE ERASED ? (Y/N)")
                                            if chc=="Y" or chc=="y":
                                                    mycursor.execute("delete from JEE where(username='"+user+"')")
                                                    mysql.commit()
                                                    print("DATA DELETED")
                                            else :
                                                    print("DATA NOT DELETED ")
                                                    
                                    if yz==2 :
                                            chc=input("ARE YOU SURE ? YOUR ALL DATA WILL BE ERASED ? (Y/N)")
                                            if chc=="Y" or chc=="y":
                                                    mycursor.execute("delete from NEET where(username='"+user+"')")
                                                    mysql.commit()
                                                    print("DATA DELETED")
                                            else :
                                                    print("DATA NOT DELETED ")
                                            
                                    if yz==3 :
                                            chc=input("ARE YOU SURE ? YOUR ALL DATA WILL BE ERASED ? (Y/N)")
                                            if chc=="Y" or chc=="y":
                                                    mycursor.execute("delete from Faculty where(username='"+user+"')")
                                                    mysql.commit()
                                                    print("DATA DELETED")
                                            else :
                                                    print("DATA NOT DELETED ")
                                            
                            else :
                                    break
                                        
                        

                    else:
                        print("USER DOESNT EXIST ")

                
         
        #Seventh option -For exiting the program        
        elif a==7 :
            print("THANK YOU!")
            break
                
            
            

