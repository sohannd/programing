import os
import subprocess
if os.name == "nt":
    subprocess.run("cls",shell=True)
database = {"SOHAN ND" : {"username":"SOHAN ND",
                          "password":8891,
                          "balance" :0
                          }}
while True:
    
    import time

   
    print("\n")
    print("__________________________________________________________")
    print("__________________M I N I    B A N K______________________")
    print("__________________________________________________________")

    type_ = input("SIGNUP/LOGIN:")
    if type_ == "SIGNUP" or type_ == "Signup" or type_ == "signup":
        new_acc = input("CREATE ACCOUNT: ")
        new_acc_passwd = int(input("Set a numerical Password: "))
        database[new_acc] = {
            "username":new_acc,
            "password":new_acc_passwd,
            "balance":0}
        time.sleep(1.8)
        print("__________________________________________________________")
        print("_______________Account Created Successfull________________")
        print("__________________________________________________________")
        print("USERNAME : ",database[login_name]["username"])
        print("password : ",database[login_name]["password"])
        print("Balance  : ",database[login_name]["balance"])
        print("__________________________________________________________")
        print("\n")
        time.sleep(1)


    elif type_ == "LOGIN" or type_ == "Login" or type_ == "login":
        login_name = input("Enter user name : ")
        login_passwd = int(input("PASSWORD: "))
        if login_name in database and database[login_name]["password"] == login_passwd:

            print("__________________________________________________________")
            print("___________________login Successfull______________________")
            print("__________________________________________________________")
            print("USERNAME : ",database[login_name]["username"])
            print("password : ",database[login_name]["password"])
            print("Balance  : ",database[login_name]["balance"])
        
        else:
            pass
    else:
        print("Enter correctly")
        break

    
    database[login_name]["balance"] = 0
    add_money = input("Do you want to deposit OR withdraw ? : ")
    if add_money == "Deposit" or add_money == "deposit" or add_money == "DEPOSIT":
        while True:
            depo_money =int(input("Enter how much you eant to deposit : "))
            database[login_name]["balance"] += depo_money
            print("Current Balance: ",database[login_name]["balance"])
            tryagain_1 = input("Deposit Again? (y/n)")
            if tryagain_1 !="y":
                break
    else:
        break

    tryagain = input("try again from LOGIN ??(y/n):")
    if tryagain !="y":
        break

