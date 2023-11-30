!/usr/bin/python3
import sys

number_of_arguments = len(sys.argv)

if number_of_arguments == 1:
    print(f"Number of argument(s): {number_of_arguments} argument:")
else:
    print(f"Number of argument(s): {number_of_arguments} arguments:")

if number_of_arguments > 1:
    print(".", end="")

print("")

for i in range(1, number_of_arguments):
    print(f"{i}: {sys.argv[i]}")
