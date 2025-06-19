#!/usr/bin/env python3
students = {"Tanya": 35, "Roger": 56, "Priyanka": 78, "Dana": 66}
name = input("Enter the student's name:")

if name in students:
    print("{}'s marks:{}".format(name, students[name]))
else:
    print("Student not found")
