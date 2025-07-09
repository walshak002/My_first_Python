#printThis my firstpython script
import time

print("HELLO")
print("Welcome to Bel_Air Micro_wave")

#print("...........")
#print("Open The Micro-wave")
#print("...........")
#print("On the micro_wave")
#print("1. Put the Rice")

customer = {}
username = input("Please what your Name: \n")
choice = input("What do you like to micro_wave: \n")
print(username, "set a time to start micro_waving your", choice)
time_to_micro_wave = input("Duration: \n")
convert_to_int=float(time_to_micro_wave)

price_to_pay = convert_to_int * 1000
print("You are charge : ₦", price_to_pay, "💸" "only")
customer["amount"] = price_to_pay

#print(username)
#print(choice)
print("Your food🥘 will be ready in {}" .format(convert_to_int,))
print(username, "I will let you know when is ready....")
minutes_in_seconds =5
time.sleep(convert_to_int * minutes_in_seconds)
print("Your food is ready", username)
print(username, "thanks for your patronage! U may have a nice day😇 ")
