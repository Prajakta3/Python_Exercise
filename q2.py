#Question-2 Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#This is Prajakta
#Software Engineer
#Then, the output should be:
#THIS IS PRAJAKTA
#SOFTWARE ENGINEER


n = int(raw_input("How many lines?")) #Number of Lines to be printed

seq_line = [] #Empty List

#For Loop for getting the input from the user
for one_line in range(n):
    input = raw_input("Enter Your Line: ")
    seq_line.append(input.upper())  #Convert the user input into Upper Case and add in the empty list

#For Loop for printing the line
for line_capital in seq_line:
    print "Your Line is - %s" % line_capital