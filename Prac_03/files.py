"""Files"""

# Question 1
# name = input("Name: ")
# outfile = open("name.txt", "w")
# outfile.write(name)
# outfile.close()
#
# # Question 2
# infile = open("name.txt", "r")
# name = infile.readline()
# print(f"Your name is {name}")
# infile.close()
#
# # Question 3
# infile = open("numbers.txt", "r")
# first_number = int(infile.readline())
# second_number = int(infile.readline())
# infile.close()
# total = first_number + second_number
# print(f"The total is: {total}")

# Question 4
infile = open("numbers.txt", "r")
error_line_numbers = []
total = 0
for line_number, line in enumerate(infile, 1):
    try:
        number = float(line)
        total += number
    except ValueError as error:
        error_line_numbers.append(line_number)
infile.close()
error_line_numbers = ", ".join([str(number) for number in error_line_numbers])
print(f"These lines have errors: {error_line_numbers}")
print(f"The total is: {total}")


