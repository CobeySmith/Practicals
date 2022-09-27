"""Files"""

# Question 1
name = input("Name: ")
outfile = open("name.txt", "w")
outfile.write(name)
outfile.close()

# Question 2
infile = open("name.txt", "r")
name = infile.readline()
print(f"Your name is {name}")
infile.close()

# Question 3
infile = open("numbers.txt", "r")
first_number = int(infile.readline())
second_number = int(infile.readline())
infile.close()
total = first_number + second_number
print(f"The total is: {total}")

# Question 4
infile = open("numbers.txt", "r")
total = 0
for line in infile:
    number = int(line)
    total += number
infile.close()
print(f"The total is: {total}")


