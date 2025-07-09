'''
Prompt a user for his detail
1. User fullname
2. User age
3. User height
4. User IsMarried
5. Hobbies
Note: it should also show which data type is it.....

Any Question
'''

print("HELLO")

username = input("Please what is your Full Name: \n")
userage = int(input("Enter yourr Age: \n"))
height = float(input("What your height?: \n"))
marital_status = bool(input("Are you married true/false: \n"))
hobbies = input("Enter your Hobbies: \n")

click = input("Click Enter to see User Details \n")

print(f"Welcome, {username}")
print(f"Your Age is : {userage}")
print(f"You height is : {height}")
print(f"Your marital_status: {marital_status}")
print(f"Your Hobbies are : {hobbies}")

print(type(username))
print(type(userage))
print(type(height))
print(type(marital_status))



