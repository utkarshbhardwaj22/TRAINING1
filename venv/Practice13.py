"""
Operations in sequences:

Sequence: Multi Value Container
 same type of data: homo
 different type of data: hetro

1. Contatenation
2. Repetition
3. Membership testing
4. Indexing
5. Slicing

"""
students = ["utkarsh", "dinesh", "harpreet", "deepak"]

#1. Concatenation

more_students= students + ["rahul", "abhishek"]

print("More students:",more_students)
print()

#2 . Repetition

repeated_students= students*2
print("Repeated students:",repeated_students)
print()

#3. Membership Testing | in and not in

print("utkarsh" in students)
print("utkarsh" not in students)
print()

#4. Indexing
print(students[0])
print(students[-1])
print()

#5. Slicing

print(students[0:3])  # from 0 to less one than 3 i.e. 2
print(students[3:])
print(students[-3:-1])