import random
import string
import pandas as pd
import os

available_files = os.listdir()
if ('passwordstore.csv' not in available_files):
    df = pd.DataFrame({'websites': [], 'usernames': [], 'passwords': []})
    df.to_csv('passwordstore.csv', index=False)


def password_generator():
    len = int(input("\nEnter length of passsword : "))
    repeat = int(input("how many passwords do you need : "))
    for i in range(repeat):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        first = lower + upper + "_"
        all = lower + upper + num + symbols
        temp1 = random.sample(first, 1)
        temp2 = random.sample(all, len - 1)
        password = temp1 + temp2
        password = "".join(password)
        print(password)


def password_store():
    df = pd.read_csv("passwordstore.csv")
    n = int(input("\nEnter number of passwords you want to store:"))
    for x in range(n):
        website = input("\nEnter website name : ")
        username = input("Enter username : ")
        password = input("Enter the password : ")
        df.loc[len(df.index)] = [website, username, password]
    df.to_csv('passwordstore.csv', index=False)
    print("Password saved successfully!!")


def password_search():
    name = str(input("\nEnter Username/Website name : "))
    df = pd.read_csv("passwordstore.csv")
    websites = df['websites'].to_list()
    usernames = df['usernames'].to_list()
    passwords = df['passwords'].to_list()
    for i in range(len(websites)):
        if (websites[i] == name):
            print(f'Your corresponding password for is found in Website {websites[i]}. It is {passwords[i]}')
            return
        if (usernames[i] == name):
            print(f'Your corresponding password for is found in Username {usernames[i]}. It is {passwords[i]}')
            return
    print(f'The Username/Website "{name}" is not found in the database.')


choice = int(input("1. Password Generator\n2. Password Store\n3. Password Search\nEnter Choice : "))
if choice == 1:
    password_generator()
elif choice == 2:
    password_store()
elif choice == 3:
    password_search()
else:
    print("Invalid Input!!")

