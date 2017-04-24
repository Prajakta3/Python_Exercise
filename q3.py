#Question-3 Define a function that can accept two strings as input and print the string with maximum length in console.
#If two strings have the same length, then the function should print al l strings line by line.


str1 = raw_input("Enter First string:")
str2 = raw_input("Enter Second string:")

def Comparision(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 > l2:
        print "Length of %s is greater" % str1
    elif l2 > l1:
        print "Length of %s is greater" % str2
    else:
        print "Length of %s and %s are equal" % (str1,str2)

Comparision(str1, str2)