import sys
import time

#variablen

password = "insert_password"

print("=============")
print("Datenbank")
print("=============")
print()
time.sleep(0.9)
print("Loading...")
time.sleep(1.5)
print()
input_name = input("Enter your name >>")
print()
time.sleep(1.7)
input_password = input("Enter password >>")
time.sleep(2.7)

#validating

if input_password == password:
    print()
    print("Welcome,",input_name,"")

else: 
      print("Invalid Data")
      time.sleep(1)
      exit(0)

