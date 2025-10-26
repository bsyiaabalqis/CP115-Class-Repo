attempts_used = 0
login_successful = False 

# TODO: Your code here
while attempts_used <3:
    password = input("Enter your password:")
    attempts_used +=1
    
    if password == "python123":
        login_successful = True 
        break 

    print(f"Wrong password. {3 - attempts_used} attempts remaining.")
print(f"Login successful.")
print(attempts_used)
