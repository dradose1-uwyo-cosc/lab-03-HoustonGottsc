# Houston P. Gottsch
# UWYO COSC 1010
# 9/25/24
# Lab 03 
# Lab Section: 15
# Sources, people worked with, help given to: Colter Makowski
# your
# comments
# here



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
stateswithelements = ["Wyoming","Colorado","Montana"]



#print the entire list
print(stateswithelements)

#now print the first element in the list
print(stateswithelements[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(stateswithelements[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{stateswithelements[1]} is south of {stateswithelements[0]}, matching the casing provided")



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
stateswithelements.append("Washington")
stateswithelements.append("Oregon")
stateswithelements.append("California")
print(stateswithelements)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
stateswithelements[-2] = "Maine"
print(stateswithelements)

#Insert the state Texas to be the third element in the list, again printing your list
stateswithelements.insert(2,"Texas")
print(stateswithelements)

#Using the `del` statement remove the fourth item from the list, print your list 
del stateswithelements[3]
print(stateswithelements)
#Remove Texas using its value, print the list
stateswithelements.remove("Texas")
print(stateswithelements)
print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(sorted(stateswithelements))
print(stateswithelements)

#Permanently sort your list in reverse order, printing it out
stateswithelements.sort(reverse=True)
print(stateswithelements)

#Using the reverse method reverse the list and print it
stateswithelements.reverse()
print(stateswithelements)
