#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
target = "apple"

count = 0
for x in words:
    if x == target:
        count +=1

print(f"The word {target} is {count} times in the list")