#------------------------------------------------------------------------------------
# Author: Muhammad Hasanat                    Course:CS1101(Programming Fundamentals)
# Muhammad_Learning_Journal_Unit6_Part1.py
#
#
# this script turns a string of words into a list and then delete 3 items from the list
# and then sort the list, and after that it adds 3 new items in the list and then
# turns the list back into long string. This scripts generates output message on the 
# screen after each of the operation to display the appropriate outputs.
#-------------------------------------------------------------------------------------


# declaring and defining the food string
foods = "Sandwitch Burger Pasta Noodles Rice Egg Meat Fish Steak kabab Sweets Kimchi"
print("Input String: \n:", foods)

foodlist = []            # Defining an empty food list
foodlist=foods.split()   # turning sting into a list of words using split

print("\nfoodlist values which is created with the input string:")
print(foodlist)

print("List values before deleteing items:\n", foodlist)
# deleting Noodles Rice Egg from the foodlist
print("\nfoodlist values after removing Noodles, Rice and Egg from the list: ")
foodlist.pop(3)           # deleting 4th item on the foodlist using pop()
print(foodlist)
foodlist.remove('Rice')   # deleting 7th item on the foodlist using remove()
print(foodlist)
del foodlist[3]           # deleting 7th item on the foodlist using del operator
print(foodlist)

foodlist.sort()           # sorting the list
print("\nfoodlist values after sorting the list: ")
print(foodlist)           # printing the sorted list values

print("Foodlist values before adding 3 items: \n", foodlist)
print("\nfoodlist values after adding Checken, Mutton, and Beef in the foodlist:")
foodlist.append("Chicken")                # adding "Chicken" in the foodlist using append
print(foodlist)
foodlist.extend("Mutton".split())         # adding "Mutton" in the foodlist using extend
print(foodlist)
foodlist.insert(len(foodlist),"Beef")     # adding "Beef" in the foodlist using insert
print(foodlist)

print("\nString value afer truning foodlist into a string:")
newfoodliststring=" "
newfoodliststring = newfoodliststring.join(foodlist)   # adding the list items into newfoodliststring using
print(newfoodliststring)                               # string join method and printing it on the screen

#end of program!





    