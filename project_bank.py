import mysql.connector
from datetime import date

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythonlearn'
)

print("Connected to the database")
cur = con.cursor()
dt = date.today

print("Press 1 to create account")
print("Press 2 to create Withdrwa")
print("Press 3 to create Deposit")
print("Press 4 to create Fundtransfer")
print("Press 5 to create Balance Enqiry")
print("Press 6 to create Pin Changed")
print("Press 7 to create Account Summery")
x=int(input("Enter Your Choice"))
if x==1:
    s="select * from account"
    cur.execute(s)
    x=0
    for row in cur:
        x=x+1
    ac="SBI"
    if x>0:
        x=x+101
        ac=ac+str(x)
    else:
        ac="SBI101"
    p=input("Enter Pin")
    n=input("Enter Name")
    f=input("Enter Fname")
    e=input("Enter Email")
    ph=input("Enter Phone")
    g=input("Enter gender")
    c=input("Enter country")
    st=input("Enter State")
    ct=input("Enter CIty")
    a=input("Enter Amount")
    q="insert into account values('"+ac+"','"+p+"','"+n+"','"+f+"','"+e+"','"+ph+"','"+g+"','"+c+"','"+st+"','"+ct+"','"+a+"')"
    cur.execute(q)
    con.commit()

    print("Account Open Succefully with  Account number is = ",ac)
elif x==2:
    ac=input("Enter Account")
    pin=input("Enter Pin")
    s="select * from account where acno='"+ac+"' and pin='"+pin+"'"
    cur.execute(s)
    camt=0
    x=0
    for row in cur:
        x=x+1
        camt=int(row[10])
    if x>0:
        amt=int(input("Enter Amount to witdraw"))
        if camt>=amt:
            camt=camt-amt
            s="update account set amount='"+str(camt)+"' where acno='"+ac+"'"
            cur.execute(s)
            con.commit()
            s="insert into mytrans(acno,amount,dt,ds)values('"+ac+"','"+str(amt)+"','"+str(dt)+"','Withdraw')"
            cur.execute(s)
            con.commit()
            print("After withdraw ",amt," Your Current balance is  = ",camt)
        else:
            print("Insufficient balance")
    else:
        print("Invalid Account or Pin") 
elif x==3:
    ac=input("Enter Account")
    pin=input("Enter Pin")
    s="select * from account where acno='"+ac+"' and pin='"+pin+"'"
    cur.execute(s)
    camt=0
    x=0
    for row in cur:
        x=x+1
        camt=int(row[10])
    if x>0:
        amt=int(input("Enter Amount to witdraw"))
        camt=camt+amt
        s="update account set amount='"+str(camt)+"' where acno='"+ac+"'"
        cur.execute(s)
        con.commit()
        s="insert into mytrans(acno,amount,dt,ds)values('"+ac+"','"+str(amt)+"','"+str(dt)+"','Deposit')"
        cur.execute(s)
        con.commit()
        print("After Deposit ",amt," Your Current balance is  = ",camt)
    else:
        print("Invalid Account or Pin") 

elif x==4:
    ac=input("Enter Account")
    pin=input("Enter Pin")
    s="select * from account where acno='"+ac+"' and pin='"+pin+"'"
    cur.execute(s)
    camt=0
    x=0
    for row in cur:
        x=x+1
        camt=int(row[10])
    if x>0:
        amt=int(input("Enter Amount to Transfer"))
        if camt>=amt:
            tac=input("Enter Account to Transfer")
            q="select * from account where acno='"+tac+"'"
            cur.execute(q)
            t=0
            tamt=0
            for row in cur:
                t=t+1
                tamt=int(row[10])
            if t>0:
                camt=camt-amt
                s="update account set amount='"+str(camt)+"' where acno='"+ac+"'"
                cur.execute(s)
                con.commit()
                tamt=tamt+amt
                s="update account set amount='"+str(tamt)+"' where acno='"+tac+"'"
                cur.execute(s)
                con.commit()
                s="insert into mytrans(acno,amount,dt,ds)values('"+ac+"','"+str(amt)+"','"+str(dt)+"','Transfer')"
                cur.execute(s)
                con.commit()
                s="insert into mytrans(acno,amount,dt,ds)values('"+tac+"','"+str(amt)+"','"+str(dt)+"','Recieve')"
                cur.execute(s)
                con.commit()

                print("After Transfer ",amt," Your Current balance is  = ",camt)
            else:
                print("Invaid Benificiry Account")
        else:
            print("Insufficient balance")
    else:
        print("Invalid Account or Pin") 
elif x==5:
    ac=input("Enter Account")
    pin=input("Enter Pin")
    s="select * from account where acno='"+ac+"' and pin='"+pin+"'"
    cur.execute(s)
    camt=0
    x=0
    for row in cur:
        x=x+1
        camt=int(row[10])
    if x>0:
        
        print(" Your Current balance is  = ",camt)
    else:
        print("Invalid Account or Pin") 
elif x==6:
    ac=input("Enter Account")
    pin=input("Enter Pin")
    s="select * from account where acno='"+ac+"' and pin='"+pin+"'"
    cur.execute(s)
   
    x=0
    for row in cur:
        x=x+1
        
    if x>0:
        np=input("Enter New Pin")
        s="update account set pin='"+np+"' where acno='"+ac+"'"
        cur.execute(s)
        con.commit()
        print(" Pin Changed Succefully ")
    else:
        print("Invalid Account or Pin") 

elif x==7:
    ac=input("Enter Account")
    pin=input("Enter Pin")
    s="select * from account where acno='"+ac+"' and pin='"+pin+"'"
    cur.execute(s)
    x=0
    for row in cur:
        x=x+1
    if x>0:
        s="select * from mytrans where acno='"+ac+"'"
        cur.execute(s)
        print("TID\tAccount\tAMount\tDt\tDS")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
    else:
        print("Invalid Account or Pin") 

