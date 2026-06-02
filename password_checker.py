
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print(" P-A-S-S-W-O-R-D  |  C-H-E-C-K-E-R")
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")


symbols_ = set("!@#$%^&*()_+-=")
symbols_count = 0
user_passwd = input("Enter Your Password: ")
if len(user_passwd) > 8:
    if user_passwd.isalpha() == False:
        if user_passwd.isdigit() == False:
            for char in user_passwd:
                if char in symbols_:
                    symbols_count += 1
            #print(f"Symbols count:{symbols_count}")
            if symbols_count <= 1:
                print("Add more Symbols")
            else:
                print("Your password is Strong")
        else:
            print("please add alphabents and symbols")
    else:
        print("Please add numerics and symbols")
else:
    print("WEAK PASSWORD, password must more than 8 char")

print(f"Entered Password:{user_passwd}")
