from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as file_key:
        file_key.write(key)
write_key()"""



def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as file:
        for line in file.readlines():
            user, passwd = line.split("|")
            print("User:" , user , "Password:" , fer.decrypt(passwd.encode()).decode())

def add():
    user = input("Account name:")
    pwd = input("Password:")
    with open("password.txt" , "a")as file:
        file.write(user + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    user_input = input("Would to like to add a new password or view existing ones (view,add) , press q to quit?")
    if user_input == "view":
        view()
    elif user_input == "add":
        add()
    elif user_input == "q":
        quit()
    else:
        print("That choice doesnt exists" + user_input)
