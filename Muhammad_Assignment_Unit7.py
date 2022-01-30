#------------------------------------------------------------------------------
# Author: Muhammad Hasanat             Course:CS1101(Programming Fundamentals)
# Muhammad_Assignment_Unit7
#
# this script includes the implementation of histogram(s), has_duplicates(s),
# missing_letters(s) functions and the main program.
#------------------------------------------------------------------------------

#global variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]


# From Section 11.2 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham,
# Massachusetts: Green Tree Press.
# histogram(s): this function return dictionary object which is crated inside the function 
# using the parameter string. The dictionary object includes string letters as keys and number 
# of repitation as values.
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

# Part1: has_duplicates(s) function(s): this function return Ture if the
# passing parameter string contains character repitation else False
#-----------------------------------------------------------------------
def has_duplicates(s):
    dictable = histogram(s)
    for x in dictable:
        if dictable[x] > 1:
            return True
    return False

# Part1: main program: using has_duplicates(s) function this section of
# the main program show appropriate message on the screen.
#------------------------------------------------------------------------
print("\nCS1101: Assignment Unit 7: Part 1:")
print("----------------------------------")

for x in test_dups:                    # looping through test_dups string list
    if has_duplicates(x):
        print(x, "has duplicates" )    # while repetitive item found
    else:
        print(x, "has no duplicates" ) # while no repetitive item found

# Part2: missing_letters(s) function: this function returns a string object of 
# the missing letters in the passing parameter string comparing with the global 
# variable alphabet string("abcdefghijklmnopqrstuvwxyz")
#------------------------------------------------------------------------------
def missing_letters(s): 
    dictable = histogram(s)
    missinglist= []  # declaring list object for holding missing letters
    str = ""
    for letter in alphabet:        # using the global variable alphabet
        if letter not in dictable.keys():  
            missinglist.append(letter)
    missinglist.sort()  # sorting missing letters list object
    for c in missinglist:
        str = str + c # creating the missing letters string using letters list object
    return str
    
# Part2: main program: this section of the main program loop through the test_miss string 
# list and prints an appropriate message on behalf of each test_miss list item
#----------------------------------------------------------------------------------------
print("\nCS1101: Assignment Unit 7: Part 2:")
print("----------------------------------")

for x in test_miss:                   # looping through test_miss string list
    if len(missing_letters(x)) == 0:  # when the string includes all the available letters
        print(x, "uses all the letters" )
    else:
        print(x, "is missing letters", missing_letters(x)) # retrieving and showing all the missing letters