import random , string
def pass_gen(n):
    lib=[]
    
    l= (input("Include Lettsers Y/N : ")).lower()=='y'
    d= (input("Include digits:Y/N: ")).lower()=='y' 
    s= (input("Include Lettsers:Y/N: " )).lower()=='y'
     
 
    if l:
        lib.append(string.ascii_lowercase)
        lib.append(string.ascii_uppercase)
    if d:
        lib.append(string.digits)
    if s:
        lib.append(string.punctuation)
    
    # print(lib)
    if not lib:
        return "Select at least one option"

    elif n < len(lib):
        return f"Password should be atleast ", {  len(lib) } , " characters long"



    passwordd_set=""  
    for i in range(len(lib)): 
        passwordd_set+=lib[i]




    passwordd=[]  
    for i in range(len(lib)):  
        passwordd.append(random.choice(lib[i]))  

    for i in range(n-len(lib)):  
        passwordd.append(random.choice(passwordd_set))     
 
    random.shuffle(passwordd)
    return "".join(passwordd)  
 


n=int(input("Enter password length: "))
if n<=0 :
    print("Invalid Input")
else:
    print("Password: " , pass_gen(n))

