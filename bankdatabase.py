
import sqlite3

cnxn = sqlite3.connect('KAMU_KAMU.db')
cursor = cnxn.cursor()

class CLIMenu(object):

    def __init__(self, options: list):
        self.options=options

    def PrintCLIMenu(self):
        print("PLEASE ENTER THE NUMBER CORRESPONDING TO YOUR DESIRED COMMAND IN THE PROMPT BELOW :\n ", *self.options,
              sep='\n')
        print()
    def GetUserInput(self):
        return input(">>>: ")

def ViewCustomer():
        CustToView=input("PLEASE ENTER THE NATIONAL IDENTITY CARD NUMBER OF THE CUSTOMER YOU WISH TO VIEW : ")
        cursor.execute("SELECT * FROM customer WHERE Cust_NIC=?",CustToView) # Cust_NIC === customer id
        columns = [column[0] for column in cursor.description]
        print('\t'.join(str(i) for i in columns),end="")
        print('\n')
        for row in cursor.fetchall():
            print ('\t'.join(str(j)for j in row))
        input("\n==========PRESS ENTER KEY TO RETURN TO THE PREVIOUS MENU==========")

def ViewAllCustomers():
    cursor.execute("SELECT * FROM customer")
    columns = [column[0] for column in cursor.description]
    print('\t'.join(str(i) for i in columns), end="")
    print('\n')
    for row in cursor.fetchall():
        print('\t'.join(str(j) for j in row))
    input("\n==========PRESS ENTER KEY TO RETURN TO THE PREVIOUS MENU==========")

def DeleteBank(name):
    cursor.execute("DELETE FROM Bank WHERE Name = ?",(name,))
    cnxn.commit()
    print("REGISTRATION SUCCESSFUL")
    cnxn.commit()


def AddBankDetails():
        HoldBankObject = [input("ID:"), input("Name : "),input("Location: ")]
        Id = HoldBankObject[0]
        Name = HoldBankObject[1]
        Location = HoldBankObject[2]
        cursor.execute("INSERT into Bank (Bankid,Name,Location) VALUES(?,?,?)",(Id,Name,Location))
        cnxn.commit()
        print("REGISTRATION SUCCESSFUL")
        cnxn.commit()


def AddTellertoBank():
        HoldTeller = [input("ID: "),input("Name: ")]
        Tid = HoldTeller[0]
        TName = HoldTeller[1]
        cursor.execute("INSERT into Teller VALUES(?,?)",(Tid,TName))
        cnxn.commit()
        print("REGISTRATION SUCCESSFUL")
        cnxn.commit()

def RegisterCustomer():
        HoldCust = [input("ID: "),input("Name:"),input("Address:"),input("Phone:"),input("Acc_No:")]
        Cid = HoldCust[0]
        Cname = HoldCust[1]
        CAddress = HoldCust[2]
        Cphone = HoldCust[3]
        Caccno = HoldCust[4]
        cursor.execute("INSERT into Customer VALUES(?,?,?,?,?)",(Cid,Cname,CAddress,Cphone,Caccno))
        cnxn.commit()

        while True:
            CustomerMenu = CLIMenu(['\t1.SAVING', '\t2.CHECKING'])
            CustomerMenu.PrintCLIMenu()
            UserInput = CustomerMenu.GetUserInput()
            if UserInput == '1':
                g = input("AccountNo:")
                SValue = 0
                cursor.execute("INSERT into savings VALUES(?,?,?)", (g, Cid, SValue))
                break

            if UserInput == '2':
                d = input("AccountNo:")
                CValue = 0
                cursor.execute("INSERT into checking VALUES(?,?,?)", (d, Cid, CValue))
                break

        print("REGISTRATION SUCCESSFUL")
        cnxn.commit()

class Transaction:

    def __init__(self,acct,amt):
        self.acct=acct
        self.amt=amt

    def Deposit(self):
        cursor.execute("UPDATE savings SET AccountBal=AccountBal+? WHERE id=?",(self.amt,self.acct))
        cnxn.commit()
        print("YOU'VE DEPOSITED %s TO ACCOUNT NUMBER %s" % (self.amt,self.acct))
    def Withdrawal(self):
        cursor.execute("UPDATE savings SET AccountBal=AccountBal-? WHERE id=?",(self.amt,self.acct))
        cnxn.commit()
        print("YOU'VE  WITHDRAWN  %s FROM ACCOUNT NUMBER %s" % (self.amt, self.acct))


if __name__=='__main__':
    while True:
        MainMenu=CLIMenu(['\t1.CREATE BANK'])#,'\t2.ACCESS TRANSACTION PORTAL','\t3.EXIT'])
        MainMenu.PrintCLIMenu()
        UserInput=MainMenu.GetUserInput()
        if UserInput =='1':
            while True:
                CustomerMenu = CLIMenu(['\t1.ADD_BANK', '\t2.VIEW BANK LIST',
                                              '\t3.DELETE BANK','\t4.GO TO PREVIOUS MENU'])
                CustomerMenu.PrintCLIMenu()
                UserInput=CustomerMenu.GetUserInput()
                if UserInput == '1':
                    AddBankDetails()
                    continue
                if UserInput == '2':
                    list =[]
                    cursor.execute("SELECT Name FROM Bank")
                    for row in cursor:
                        list.append(row[0])
                        print(row[0])

                    while True:
                        CustomerMenu = CLIMenu(["\t1."+list[0],"\t2."+list[1]])
                        CustomerMenu.PrintCLIMenu()
                        UserInput = CustomerMenu.GetUserInput()
                        if UserInput == '1':
                           print("="*30)
                           print("WELCOME TO\t",list[0])
                           print("=" * 30)

                           while True:
                               CustomerMenu = CLIMenu(['\t1.OPEN ACCOUNT','\t2.DEPOSIT','\t3.WITHDRAW'])
                               CustomerMenu.PrintCLIMenu()
                               UserInput = CustomerMenu.GetUserInput()
                               if UserInput == '1':
                                   RegisterCustomer()
                                   break

                               if UserInput == '2':
                                   AcctToTransact = input("PLEASE ENTER THE ACCOUNT NUMBER : ")
                                   AmtToTransact = input("PLEASE ENTER THE TRANSACTION AMOUNT : ")
                                   trnsct1 = Transaction(AcctToTransact, AmtToTransact)
                                   trnsct1.Deposit()
                                   print("process successfull")
                                   break

                               if UserInput == '3':
                                   AcctToTransact = input("PLEASE ENTER THE ACCOUNT NUMBER : ")
                                   AmtToTransact = input("PLEASE ENTER THE TRANSACTION AMOUNT : ")
                                   trnsct2 = Transaction(AcctToTransact, AmtToTransact)
                                   trnsct2.Withdrawal()
                                   print("process successfull")
                                   break





                        if UserInput == '2':
                            print("=" * 30)
                            print("WELCOME TO\t", list[1])
                            print("=" * 30)

                            while True:
                                CustomerMenu = CLIMenu(
                                    ['\t1.OPEN ACCOUNT','\t2.DEPOSIT', '\t3.WITHDRAW'])
                                CustomerMenu.PrintCLIMenu()
                                UserInput = CustomerMenu.GetUserInput()
                                if UserInput == '1':
                                    RegisterCustomer()
                                    break

                                if UserInput == '2':
                                    AcctToTransact = input("PLEASE ENTER THE ACCOUNT NUMBER : ")
                                    AmtToTransact = input("PLEASE ENTER THE TRANSACTION AMOUNT : ")
                                    trnsct3 = Transaction(AcctToTransact, AmtToTransact)
                                    trnsct3.Deposit()
                                    print("process successfull")
                                    break

                                if UserInput == '3':
                                    AcctToTransact = input("PLEASE ENTER THE ACCOUNT NUMBER : ")
                                    AmtToTransact = input("PLEASE ENTER THE TRANSACTION AMOUNT : ")
                                    trnsct = Transaction(AcctToTransact, AmtToTransact)
                                    trnsct.Withdrawal()
                                    print("process successfull")
                                    break



                    continue

                if UserInput == '3':
                    site = input("Enter number corresponding to bank eg 1 or 2:")
                    DeleteBank(list[site-1])
                    print("Successfully deleted!!!")

                if UserInput == '4':
                    break


cnxn.close()
quit()
