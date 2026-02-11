#!/usr/bin/env python

first_num = input("Enter the first number: ")
second_num = input("Enter the second numner: ")

result = int(first_num) * int(second_num)

if int(result) > 0:
    print(f"{first_num} x {second_num} = {result}")
    print("This result is positive")
elif int(result) < 0:
    print(f"{first_num} x {second_num} = {result}")
    print("This result is negative")
else :
    print("This result is zero")