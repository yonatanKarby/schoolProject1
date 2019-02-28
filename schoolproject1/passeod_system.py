def hashFunc(password):
    password_hash=0
    local_hash=0.0
    for i in range(len(password)):
        local_hash=ord(password[i])
        password_hash+=local_hash
    password_hash=pow(password_hash,3)
    password_hash=password_hash/27.3
    if(password_hash==10578929.706959706):
        return True
    else:
        return False
user_passwod=input("enter your password: ")
password_OK=hashFunc(user_passwod)
counter=5
while((password_OK== False)and(counter>=0)):
    user_passwod=input("you enter wrong password! enter new one: ")
    password_OK=hashFunc(user_passwod)
    counter=counter-1
if(password_OK):
    print("you are in")
