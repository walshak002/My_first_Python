#Question 1
print(".............................")
my_age = 21 #A  variable  called my_age and set it to  your actual age.
pi = 3.14159 #A  variable  called pi and assign it the value 3.14159.
#Create a new variable called magic_number that is the result of: Your my_age multiplied by 3, then add the  pi, and finally take the modulus (%) with 7.index
magic_number = (my_age * 3 + pi) % 7 
print(magic_number) 
print(type(magic_number)) 

#Question 2
print(".............................")
secret_word = "PythonIsAmazing"
print(secret_word[0]) #The first 6 characters of the string.
print(secret_word[1])
print(secret_word[2])
print(secret_word[3])
print(secret_word[4])
print(secret_word[5])

print(secret_word[-7:]) #The last 7 characters using negative indexing.
print(secret_word[6:8]) #The middle word "Is" using slicing.
print(secret_word[::-1]) #The string reversed using slicing.
print(secret_word[1::2]) #Every second character in the string (using step slicing ::2).

#Question 3
print("............................")
secret_word = "PythonIsAmazing"
print(secret_word[:6].upper()) #Convert only the first word ("Python") to uppercase and print it.
print(secret_word[-7:].lower()) #Convert the rest of the string ("IsAmazing") to lowercase and print it.
print(secret_word[:6].upper() +  secret_word[-9:-1].lower()) # Combine the uppercase and lowercase parts into one new string and print it.
