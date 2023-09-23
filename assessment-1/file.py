def getdata():
    print ("\n\t\t WELCOME TO FRUIT MARKET")
    m=print("\n\t\t 1) Manager")
    c=print("\t\t 2) Customer")
    r=int(input("\n select your role :"))
    if r==1:
        print("\n\t\tFRUIT MARKET MANAGER ")
        add_f=print("\n\t\t1) ADD FRUIT STOCK")
        view_f=print("\t\t2) VIEW FRUIT STOCK")
        updt_f=print("\t\t3) UPDATE FRUIT STOCK")
        choice_f=int(input("\n Enter your choice :"))
        fstock={}
        keys=['Name','QTY','Price']

        if choice_f==1:
            print("ADD FRUIT STOCK")
            #n=int(input("Enter no fruit want to add in stock :"))
            a=0
            while True:
                for i in range(len(keys)):
                    v=input(f"Enter value of {keys[i]}:")
                    fstock[keys[i]]=v
                print(fstock)
                more=input("Do you want to perform more operation : press 'y' for 'yes' and press 'n' for 'no' :")
                if more == 'y':  
                    continue
                elif more == 'n': 
                    break
                else:
                    print("yes  or   noooo")
        elif choice_f==2:
            print("VIEW FRUIT STOCK")
            print(fstock)
        elif choice_f==3:
            print("UPDATE FRUIT STOCK")
    elif r==2:
        print("\n\t\thello customer ")
            
    else:
        print("\n\t\tplase select 1 or 2")
getdata( )