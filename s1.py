import mysql.connector 
conn=mysql.connector.connect(host='localhost',user='root',passwd='PendyFoodie',database='sample66')
c1=conn.cursor()


print('\n\n\t\t\t\t\t\t\t\t\t\t Welcome To Indian Matchmaking')
def main():
    print('\n\n\t\t\t\t\t\t\t\t\t     MAIN MENU :')
    print("\n\t\t\t\t\t\t\t\t\t 1.Provide Details")
    print('\t\t\t\t\t\t\t\t\t 2.Search For Bride/Groom')
    print('\t\t\t\t\t\t\t\t\t 3.Delete Records')
    print('\t\t\t\t\t\t\t\t\t 4.Update Records')
    print('\t\t\t\t\t\t\t\t\t 5.Exit')
    def firstchoice():
        choice1=str(input('\n\t\t\t\t\t\t\t Enter The Number: '))
        if choice1 == '5':
            print('\n\n\t\t\t\t\t\t\t\t\t\t\t Have A Nice Day')

        elif choice1 == '4':
            print("\n\n\t\t\t\t\t\t\t\t\t 1. Update Groom's Profile")
            print("\t\t\t\t\t\t\t\t\t 2. Update Bride's Profile")
            upchoi= input('\n\t\t\t\t\t\t\t Enter Choice : ')


            def updateind():
                global uphno
                ufname= input('\n\t\t\t\t\t\t\t\t\t Enter registered First Name   : ')
                ulname= input('\t\t\t\t\t\t\t\t\t Enter registered Last Name    : ')
                uphno= int(input('\t\t\t\t\t\t\t\t\t Enter registered Phone Number : '))
                print('''\n\n\t\t\t\t\t\t\t\t\t Update Index:

                                               \t\t\t\t 1. First Name
                                               \t\t\t\t 2. Last Name
                                               \t\t\t\t 3. Age
                                               \t\t\t\t 4. Religion
                                               \t\t\t\t 5. Caste
                                               \t\t\t\t 6. Eductaion
                                               \t\t\t\t 7. Appearance
                                               \t\t\t\t 8. Height
                                               \t\t\t\t 9. Location
                                               \t\t\t\t 10. Profession
                                               \t\t\t\t 11. Phone Number''')

            if upchoi== '1':
                updateind()
                
                def updates():
                    choice=input('\n\t\t\t\t\t\t\t Enter Choice : ')

                    if choice == '1':
                        nfname=input('\n\t\t\t\t\t\t\t\t\t Enter New First Name : ')
                        sqlup = "update male set First_Name = '{}' where Phone_Number = {} ".format(nfname,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '2':
                        nlname=input('\n\t\t\t\t\t\t\t\t\t Enter New Last Name : ')
                        sqlup = "update male set Last_Name = '{}' where Phone_Number = {} ".format(nlname,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '3':
                        nage=input('\n\t\t\t\t\t\t\t\t\t Enter New Age : ')
                        sqlup = "update male set Age = '{}' where Phone_Number = {} ".format(nage,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '4':
                        nreli=input('\n\t\t\t\t\t\t\t\t\t Enter New Religion : ')
                        sqlup = "update male set Religion = '{}' where Phone_Number = {} ".format(nreli,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '5':
                        ncast=input('\n\t\t\t\t\t\t\t\t\t Enter New Caste : ')
                        sqlup = "update male set Caste = '{}' where Phone_Number = {} ".format(ncast,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '6':
                        nedu=input('\n\t\t\t\t\t\t\t\t\t Enter New Education : ')
                        sqlup = "update male set Education = '{}' where Phone_Number = {} ".format(nedu,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '7':
                        nappe=input('\n\t\t\t\t\t\t\t\t\t Enter New Appearance : ')
                        sqlup = "update male set Appearance = '{}' where Phone_Number = {} ".format(nappe,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '8':
                        nheigh=input('\n\t\t\t\t\t\t\t\t\t Enter New Height : ')
                        sqlup = "update male set Height = '{}' where Phone_Number = {} ".format(nheigh,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '10':
                        nprof=input('\n\t\t\t\t\t\t\t\t\t Enter New Profession : ')
                        sqlup = "update male set Profession = '{}' where Phone_Number = {} ".format(nprof,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '9':
                        nloca=input('\n\t\t\t\t\t\t\t\t\t Enter New Location : ')
                        sqlup = "update male set Location = '{}' where Phone_Number = {} ".format(nloca,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '11':
                        npho=input('\n\t\t\t\t\t\t\t\t\t Enter New Phone Number : ')
                        sqlup = "update male set Phone_Number = '{}' where Phone_Number = {} ".format(npho,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    else:
                        print('\n\n\t\t\t\t\t\t\t\t\t **Wrong Choice, Enter Again**')
                        updates()
                updates()

                
            elif upchoi =='2':
                updateind()

                def updatefem():
                    choice=input('\n\t\t\t\t\t\t\t Enter Choice : ')

                    if choice == '1':
                        nfname=input('\n\t\t\t\t\t\t\t\t\t Enter New First Name : ')
                        sqlup = "update female set First_Name = '{}' where Phone_Number = {} ".format(nfname,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '2':
                        nlname=input('\n\t\t\t\t\t\t\t\t\t Enter New Last Name : ')
                        sqlup = "update female set Last_Name = '{}' where Phone_Number = {} ".format(nlname,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '3':
                        nage=input('\n\t\t\t\t\t\t\t\t\t Enter New Age : ')
                        sqlup = "update female set Age = '{}' where Phone_Number = {} ".format(nage,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '4':
                        nreli=input('\n\t\t\t\t\t\t\t\t\t Enter New Religion : ')
                        sqlup = "update female set Religion = '{}' where Phone_Number = {} ".format(nreli,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '5':
                        ncast=input('\n\t\t\t\t\t\t\t\t\t Enter New Caste : ')
                        sqlup = "update female set Caste = '{}' where Phone_Number = {} ".format(ncast,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '6':
                        nedu=input('\n\t\t\t\t\t\t\t\t\t Enter New Education : ')
                        sqlup = "update female set Education = '{}' where Phone_Number = {} ".format(nedu,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '7':
                        nappe=input('\n\t\t\t\t\t\t\t\t\t Enter New Appearance : ')
                        sqlup = "update female set Appearance = '{}' where Phone_Number = {} ".format(nappe,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '8':
                        nheigh=input('\n\t\t\t\t\t\t\t\t\t Enter New Height : ')
                        sqlup = "update female set Height = '{}' where Phone_Number = {} ".format(nheigh,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '10':
                        nprof=input('\n\t\t\t\t\t\t\t\t\t Enter New Profession : ')
                        sqlup = "update female set Profession = '{}' where Phone_Number = {} ".format(nprof,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '9':
                        nloca=input('\n\t\t\t\t\t\t\t\t\t Enter New Location : ')
                        sqlup = "update female set Location = '{}' where Phone_Number = {} ".format(nloca,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    elif choice == '11':
                        npho=input('\n\t\t\t\t\t\t\t\t\t Enter New Phone Number : ')
                        sqlup = "update female set Phone_Number = '{}' where Phone_Number = {} ".format(npho,uphno)
                        c1.execute(sqlup)
                        commm="COMMIT"
                        c1.execute(commm)
                        print('\n\t\t\t\t\t\t\t\t\t Changes Are Successfully Made !!')
                        main()
                    else:
                        print('\n\n\t\t\t\t\t\t\t\t\t **Wrong Choice, Enter Again**')
                        updatefem()
                updatefem()

        elif choice1 == '3':
            print("\n\n\t\t\t\t\t\t\t\t\t 1.Male Records")
            print('\t\t\t\t\t\t\t\t\t 2.Female Records')
            ch= str(input('\n\t\t\t\t\t\t\tEnter Choice: '))
            if ch== '1':
                fn=str(input('\n\n\t\t\t\t\t\t\tEnter First Name: '))
                pn=str(input('\t\t\t\t\t\t\tEnter Phone Number: '))
                sql_del="delete from male where First_Name = '{}' and Phone_Number = '{}' ".format(fn,pn)
                c1.execute(sql_del)
                commm="COMMIT"
                c1.execute(commm)
                print('\n\n\t\t\t\t\t\t\t\t\t Record Deleted Successfully')

            elif ch== '2':
                fin=str(input('\n\t\t\t\t\t\t\tEnter First Name: '))
                pin=str(input('\t\t\t\t\t\t\tEnter Phone Number: '))
                sql_deel="delete from female where First_Name = '{}' and Phone_Number = '{}' ".format(fin,pin)
                c1.execute(sql_deel)
                coemm="COMMIT"
                c1.execute(coemm)
                print('\n\n\t\t\t\t\t\t\t\t\t Record Deleted Successfully')

            def therdchoice():
                            c=input("\t\t\t\t\t\t\t Do You Want To Delete Another Customer's Details (y/n): ")
                            if c=='y' or c=='Y':
                                print("\n\n\t\t\t\t\t\t\tEnter '3' to continue: ")
                                firstchoice()
                            elif c=='n' or c=='N':
                                main()
                                
                            else:
                                print('\n\n\t\t\t\t\t\t\t\t\t\t ***Invalid Choice***')
                                therdchoice()
            therdchoice()
            
            
        elif choice1 == '1':
            print('\n\n\t\t\t\t\t\t\t\t 1.Male customer details')
            print('\t\t\t\t\t\t\t\t 2.Female customer details')
            def secondchoice():
                choice2=str(input('\n\t\t\t\t\t\t\t\t Enter The Number: '))
                if choice2 == '1' :
                        a=str(input('\n\t\t\t\t\t\t\t\t Enter The First Name \t\t: '))
                        b=str(input('\n\t\t\t\t\t\t\t\t Enter The Last Name \t\t: '))
                        c=str(input('\n\t\t\t\t\t\t\t\t Enter The Age \t\t\t: '))
                        d=str(input('\n\t\t\t\t\t\t\t\t Enter The Religion \t\t: '))
                        e=str(input('\n\t\t\t\t\t\t\t\t Enter The Caste \t\t: '))
                        f=str(input('\n\t\t\t\t\t\t\t\t Enter The Education \t\t: '))
                        g=str(input('\n\t\t\t\t\t\t\t\t Enter The Appearance \t\t: '))
                        h=str(input("\n\t\t\t\t\t\t\t\t Enter The Height(in cms) \t: "))
                        i=str(input('\n\t\t\t\t\t\t\t\t Enter The Location \t\t: '))
                        j=str(input('\n\t\t\t\t\t\t\t\t Enter The Profession \t\t: '))
                        k=str(input('\n\t\t\t\t\t\t\t\t Enter The Phone Number \t: '))
                        c1=conn.cursor()
                        sql_insert="insert into male values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g,h,i,j,k)
                        c1.execute(sql_insert)
                        conn.commit()
                        print ('\n\n\t\t\t\t\t\t\t\t Details are successfully inserted')
                        def thirdchoice():
                            c=input(" Do You Want To Enter Another Customer's Details (y/n): ")
                            if c=='y' or c=='Y':
                                print("\n\t\t\t\t\t\t\t Enter '1' to continue: ")
                                firstchoice()
                            elif c=='n' or c=='N':
                                main()
                                
                            else:
                                print('\n\n\t\t\t ***Invalid Choice***')
                                thirdchoice()
                        thirdchoice()
                elif choice2 == '2':
                    l=str(input('\n\t\t\t\t\t\t\t\t Enter The First Name \t\t: '))
                    m=str(input('\n\t\t\t\t\t\t\t\t Enter The Last Name \t\t: '))
                    n=str(input('\n\t\t\t\t\t\t\t\t Enter The Age \t\t\t: '))
                    o=str(input('\n\t\t\t\t\t\t\t\t Enter The Religion \t\t: '))
                    p=str(input('\n\t\t\t\t\t\t\t\t Enter The Caste \t\t: '))
                    q=str(input('\n\t\t\t\t\t\t\t\t Enter The Education \t\t: '))
                    r=str(input('\n\t\t\t\t\t\t\t\t Enter The Appearance \t\t: '))
                    s=str(input("\n\t\t\t\t\t\t\t\t Enter The Height(in cms) \t: "))
                    t=str(input('\n\t\t\t\t\t\t\t\t Enter The Location \t\t: '))
                    u=str(input('\n\t\t\t\t\t\t\t\t Enter The Profession \t\t: '))
                    v=str(input('\n\t\t\t\t\t\t\t\t Enter The Phone Number \t: '))
                    c1=conn.cursor()
                    sql_insert="insert into female values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(l,m,n,o,p,q,r,s,t,u,v)
                    c1.execute(sql_insert) 
                    conn.commit()
                    print("\n\n\t\t\t\t\t\t\t\t Details are successfully inserted")
                    def fourthchoice():
                        c=input("\n\n\t\t\t\t\t\t Do You Want To Enter Another Customer's Details (y/n): ")
                        if c=='y' or c=='Y':
                            print("\n\n\t\t\t\t\t\t\t Enter '1' to continue ")
                            firstchoice()
                        elif c=='n' or c=='N':
                            main()
                            
                        else:
                            print('\n\n\t\t\t\t\t\t\t\t\t ***Invalid Choice***')
                            fourthchoice()
                                    
                    fourthchoice()
                else:
                    print('\n\n\t\t\t\t\t\t\t\t\t ***Invalid Choice***')

                    secondchoice()
            secondchoice()

                            
                           

    


        elif choice1=='2':
            print('\n\n\t\t\t\t\t\t\t\t\t 1. Handsome Groom ')
            print('\t\t\t\t\t\t\t\t\t 2. Beautiful Bride ')
            def fifthchoice():
                choice3=str(input('\n\t\t\t\t\t\t\t Enter The Number: '))
                if choice3 == '1':
                    prof = (input('''\n\t\t\t\t\t\t\t Enter the Profession
                                                         or type 'a' to show all: '''))


                    if prof.upper()== 'A':
                        showme="select * from male"
                        qq=c1.execute(showme)
                        alll=c1.fetchall()
                        print("\n\n+=========================================================================================================================================================================+")
                        print("| First Name   | last name  | Age  | Religion  | Caste       | Education         | Appearance        | Height  | Location           | Profession          | Phone Number  |")
                        print("+=========================================================================================================================================================================+")
                        for i in alll:
                            ass=[]
                            ls=list(i)
                            print('|',ls[0],' '*(11-len(ls[0])),'|',ls[1],' '*(9-len(ls[1])),'|',ls[2],' '*(3-len(ls[2])),'|',
                                  ls[3],' '*(8-len(ls[3])),'|',ls[4],' '*(10-len(ls[4])),'|',ls[5],' '*(16-len(ls[5])),'|',ls[6],' '*(16-len(ls[6])),'|',ls[7],' '*(6-len(ls[7])),'|',
                                  ls[8],' '*(17-len(ls[8])),'|',ls[9],' '*(18-len(ls[9])),'|',ls[10],' '*(12-len(ls[10])),'|')
                    else:

                    
                        c1.execute("select* from male where Profession ='{}'".format(prof))
                        data = c1.fetchall()
                        print("\n\n+=========================================================================================================================================================================+")
                        print("|  First Name  | last name  | Age  | Religion  | Caste       | Education         | Appearance        | Height  | Location           | Profession          | Phone Number  |")
                        print("+=========================================================================================================================================================================+")
                        for i in data:
                            ass=[]
                            ls=list(i)
                            print('|',ls[0],' '*(11-len(ls[0])),'|',ls[1],' '*(9-len(ls[1])),'|',ls[2],' '*(3-len(ls[2])),'|',
                                  ls[3],' '*(8-len(ls[3])),'|',ls[4],' '*(10-len(ls[4])),'|',ls[5],' '*(16-len(ls[5])),'|',ls[6],' '*(16-len(ls[6])),'|',ls[7],' '*(6-len(ls[7])),'|',
                                  ls[8],' '*(17-len(ls[8])),'|',ls[9],' '*(18-len(ls[9])),'|',ls[10],' '*(12-len(ls[10])),'|')
                    def sixthchoice():
                        c=input("\n\n\t\t\t\t\t\t Do You Want To View Another Details (y/n): ")
                        if c=='y' or c=='Y':
                            print("\n\n\t\t\t\t\t\t\t\t *****Enter '2' to continue***** ")
                            firstchoice()
                        elif c=='n' or c=='N':
                            main()
                            
                        else:
                            print('\n\n\t\t\t\t\t\t\t\t\t ***Invalid Choice***')
                            sixthchoice()
                                    
                    sixthchoice()





                elif choice3=='2':
                    appearence = (input('''\n\t\t\t\t\t\t Enter the appearance
                                                 Or type 'a' to show all: '''))








                    
                    if appearence.upper()== 'A':
                        showme="select * from female"
                        qq=c1.execute(showme)
                        alll=c1.fetchall()
                        print("\n\n+=========================================================================================================================================================================+")
                        print("| First Name   | last name  | Age  | Religion  | Caste       | Education         | Appearance        | Height  | Location           | Profession          | Phone Number  |")
                        print("+=========================================================================================================================================================================+")
                        for i in alll:
                            ass=[]
                            ls=list(i)
                            print('|',ls[0],' '*(11-len(ls[0])),'|',ls[1],' '*(9-len(ls[1])),'|',ls[2],' '*(3-len(ls[2])),'|',
                                  ls[3],' '*(8-len(ls[3])),'|',ls[4],' '*(10-len(ls[4])),'|',ls[5],' '*(16-len(ls[5])),'|',ls[6],' '*(16-len(ls[6])),'|',ls[7],' '*(6-len(ls[7])),'|',
                                  ls[8],' '*(17-len(ls[8])),'|',ls[9],' '*(18-len(ls[9])),'|',ls[10],' '*(12-len(ls[10])),'|')
                    else:
                        
                        c1.execute("select* from female where appearance='{}'".format(appearence))
                        data = c1.fetchall()
                        print("\n\n+=========================================================================================================================================================================+")
                        print("| First Name   | last name  | Age  | Religion  | Caste       | Education         | Appearance        | Height  | Location           | Profession          | Phone Number  |")
                        print("+=========================================================================================================================================================================+")
                        for i in data:
                            ass=[]
                            ls=list(i)
                            print('|',ls[0],' '*(11-len(ls[0])),'|',ls[1],' '*(9-len(ls[1])),'|',ls[2],' '*(3-len(ls[2])),'|',
                                  ls[3],' '*(8-len(ls[3])),'|',ls[4],' '*(10-len(ls[4])),'|',ls[5],' '*(16-len(ls[5])),'|',ls[6],' '*(16-len(ls[6])),'|',ls[7],' '*(6-len(ls[7])),'|',
                                  ls[8],' '*(17-len(ls[8])),'|',ls[9],' '*(18-len(ls[9])),'|',ls[10],' '*(12-len(ls[10])),'|')
   

                    def seventhchoice():
                        c=input("\n\n\t\t\t\t\t\t Do You Want To View Another Details (y/n): ")
                        if c=='y' or c=='Y':
                            print("\n\n\t\t\t\t\t\t\t\t *****Enter '2' to continue***** ")
                            firstchoice()
                        elif c=='n' or c=='N':
                            main()
                            
                        else:
                            print('\n\n\t\t\t\t\t\t\t\t\t ***Invalid Choice***')
                            seventhchoice()
                                    
                    seventhchoice()
                    
            fifthchoice()
                
        


            

        else:
            print('\n\n\t\t\t\t\t\t\t\t\t\t\t ***Invalid Choice***')
            firstchoice()
    firstchoice()
main()           
