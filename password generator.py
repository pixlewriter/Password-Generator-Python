from random import choice
from random import randint as random_number
import string

numberlist = ["0","1","2","3","4","5","6","7","8","9"]
symbollist = ["!", "@", "#","$","%","^","&","*","(",")","[","]","{","}","'", '"', ";", ":","?","/",">","<",
",",".","`","~","_","-","+","="]
letters = string.ascii_letters
letterlist = []
for i in range(len(letters)):
    letterlist.append(letters[i])

a_random_number = choice(numberlist)
random_symbol = choice(symbollist)
random_letter = choice(letterlist)

password_list = []
list = []
generate_list = {}
password = ""

print("what will you include in your password?")
numberlist_answer = input("numbers(1,2,3,etc.) y/n? ")
symbollist_answer = input("symbol(@,~,&,etc.) y/n? ")
letterlist_answer = input("letters(a,A,Z,etc.) y/n? ")

len_of_password = input("what is the len of your password? ")

if numberlist_answer.lower() == "y":
    list.append([numberlist])
else: 
    list.append(None)



if symbollist_answer.lower() == "y":
    list.append([symbollist])
else: 
    list.append(None)



if letterlist_answer.lower() == "y":
    list.append([letterlist])
else: 
    list.append(None)


for i in range(3):
    if not list[i] == None:
        password_list += list[i]
#print(password_list)

#print(range(int(len_of_password)))
for number in range(int(len_of_password)):
    length = range(len(password_list))
    specific_list = choice(length)
    #y
    # print(specific_list)
    password += str((choice(password_list[specific_list][choice(range(len(password_list[specific_list])))])))

something = "#"*int(len_of_password)

print(f"\nthis is your password\n\n{something}\n{password}\n{something}")