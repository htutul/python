#------------------------------------------------------------------------------------
# Author: Muhammad Hasanat                    Course:CS1101(Programming Fundamentals)
# Muhammad_Learning_Journal_Unit7
#
#
# the following script contains the function calenderdictionary(keylist), invert_dict(d)
# and the main program.
#---------------------------------------------------------------------------------------

# calenderdictionary(keylist): this function creates a calender dictionary using the  
# name of the month in year, and returns a dictionary object based on the value of the 
# passing parameter list.
#-------------------------------------------------------------------------------------
def calenderdictionary(keylist):
    # declaring the months of the year dictionary object
    monthsofyear = {1:"Janurary",2:"February",3:"March",4:"April", 5:"May",6:"June",
                        7:"July",8:"August",9:"September", 10:"October",11:"November", 12:"December"}
    requestedmonthlist = dict()  # declaring dic object
    for key in monthsofyear:
        if key in keylist:       # finding the appropriate match
            requestedmonthlist.update({key:monthsofyear.get(key)}) # adding the item to the dictionary
    return requestedmonthlist     # returning the dictionary object


# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham,
# Massachusetts: Green Tree Press.
# invert_dict(d): this function invert the passing parameter dictionary, by exchaning 
# the value of keyes and values of the each dictionary items.
#-------------------------------------------------------------------------------------
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]        # getting dictioary item value in val matching the key
        inverse[val] = key  # inversing the dictionary items value
    return inverse          # returning the inverted dictionary


# main program: this section of the program test the functionality of the function
# calenderdictionary(keylist) & invert_dict(d) by passing appropriate argument.
# ----------------------------------------------------------------------------------
monthkeys= [1,2,3,4,5,6]     # declaring the months key list 
              # testign the calenderdictionary(keylist) function
print("Printing the original calenderdictionary values for passing argument keys: ")
              # printing the original dictionary items using calenderdictionary(keylist) function
print(calenderdictionary(monthkeys))  
            # testing the invert_dict(d) function.
print("\nPrinting the inverted calenderdictionary: ")
            # printing the inverted dictionary items using invert_dict(d) function
print(invert_dict(calenderdictionary(monthkeys))) 

#end of the program!
    