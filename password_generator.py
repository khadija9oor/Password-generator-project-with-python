#import the necessary modules!
import random
import string

print('hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp = random.sample(all,length)

#create the password 
password = "".join(temp)

#print the password
print(password)



#-----------------------------------------------------------------------------------
import secrets
import string

#The string module provides string constants that we can use to define the alphabet. 
#now we are going to  use ascii_letter , digits and punctuation for  gernate password

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

#Finally, let’s concatenate the above string constants to get the alphabet.

alphabet = letters + digits + special_chars

#Let’s store the length of the password in the variable, password_length.

password_length = 12

while True:
    password = ''
    for i in range(password_length):
      password += ''.join(secrets.choice(alphabet))
    
    if (any(char in special_chars for char in password) and sum(char in digits for char in password)>=2):
        break

print(password)
