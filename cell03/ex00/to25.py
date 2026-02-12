#!/usr/bin/env python

num = input("Enter a number iess than 25: ")

if int(num) <= 25:
    for i in range(int(num),26):
        print(f"Inside the loop, my variable is {i}")
else:
    print("Error")