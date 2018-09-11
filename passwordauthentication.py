password = "Hellopass"

for a in range(3):
    psw = input("Enter Password: ")
    b = 2
    if(psw == password):
        print("Access Granted!")
        break
    else:
        print("Access Denied!\nChances left: " , b-a)
        continue
