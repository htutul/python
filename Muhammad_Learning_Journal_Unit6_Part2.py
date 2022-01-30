#------------------------------------------------------------------------------------
# Author: Muhammad Hasanat                    Course:CS1101(Programming Fundamentals)
# Muhammad_Learning_Journal_Unit6_Part2.py
#------------------------------------------------------------------------------------


#Example: of Nested list
#-------------------------------------------------------------------------------------
availability = ["Yes", "No"]                     # values list item
producttype = ["Grocery","Clothing","Electronics"]   # values list item

product = [] # defining nested list item
products = [product]      # declaring the nested list

addmore = True  # loop flag
count = 0       # counter

while addmore:
    product = ["", "", ""]     # defining a list item product
    products.insert(count,product) # inserting the item and then updating it provided information
    products[count][0] = "Name: "+ input("Please enter the product Name: ")
    products[count][1] = "Producttype: " + producttype[int(input("Enter 1 for Grocery, 2 for Clothing ,3 for Electronics: "))-1]
    products[count][2] = "Available: " + availability[int(input("Enter Availability 0 for Yes, 1 for No: "))]
    if input("Do you want to add more products(y/n): ") == ("n" or "N"):
        addmore = False
        break
    else:
        count += 1
    
count = 0
while count < len(products):
    print(products[count])
    count +=1

#-------------------------------------------------------------------------------
#Example: of * operator
#-------------------------------------------------------------------------------
weekhours = [24] * 7               # generating a week hours list
print(weekhours)

#-------------------------------------------------------------------------------
# Examples: of List slices
#------------------------------------------------------------------------------
monthsofyear = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
halfoftheyear = monthsofyear[:6]
lasthalfoftheyear = monthsofyear[6:]

print(halfoftheyear)
print(lasthalfoftheyear)

#-------------------------------------------------------------------------------
#Example: of the “+=” operator
#-------------------------------------------------------------------------------
totalweekhours=0
for hours in weekhours:
    totalweekhours += hours
print("Total number hours in a week:", totalweekhours)
print("Number of hours in a week with sum function:", sum(weekhours))


#-------------------------------------------------------------------------------
# Example: of a list filter
#-------------------------------------------------------------------------------
count=0
for month in monthsofyear:
    monthsofyear[count] = month.upper()
    count +=1
print(monthsofyear)

#-------------------------------------------------------------------------------
#Example: of a legal list operation, but does the "wrong" thing
#-------------------------------------------------------------------------------
itemlist = []
item = "Warning! Test1"

itemlist.append([item])    # legal list operation, but does the "wrong" thing
                           # output value contains the brackets
print("\nlegal list operation itemlist.append([item]), but produces wrong output:")
print("print(itemlist) produces: ",itemlist)

item = "Warning! Test2"
itemlist = itemlist.append(item)   # legal list operation, but does the "wrong" thing
                                   # printing itemlist which is pointing to None
print("\nlegal list operation itemlist = itemlist.append(item), but produces wrong output:")                
print("print(itemlist) produces: ",itemlist)

