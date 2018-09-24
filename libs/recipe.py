"""
1.12 Shaped Recipe Generator
by enwash

todo:
forge oredict support
metadata
"""
import time
import os
from os.path import join as pjoin
def main():
    print("1.12 JSON Recipe Generator\nby enwash\n")
    numItems = int(input("How many items in your recipe? (plaintext):\n"))
    itemDict = {}
    charReps = []
    itemData = {}
    for i in range (1, numItems + 1):
        print("Item number " + str(i))
        item = input("What is the id of this item? (i.e. minecraft:red_flower)\n")
        char = input("What letter should this item be represented by?\n")
        if (input("Does this item have any metadata? (y/n)\n") == "y"):
            itemData[char] = int(input("What is the metadata of this item? (integer)\n"))
        else:
            itemData[char] = -1
        itemDict[char] = item
        charReps.append(char)
    rowList = []
    rowsEnabled = [True, True, True]
    rowList.append(input("----------\nEnter the first row (i.e. ABA, A A)\nLeave blank for none.\n"))
    rowList.append(input("----------\nEnter the second row (i.e. ABA, A A)\nLeave blank for none.\n"))
    rowList.append(input("----------\nEnter the third row (i.e. ABA, A A)\nLeave blank for none.\n"))
    for row in range (3):
        if (rowList[row] == ""):
            rowsEnabled[row] = False
    result = input("Enter the id of the resulting item. (i.e. minecraft:diamond)\n")

    pattern = ""
    for i in range (3):
        if (rowsEnabled[i]):
            rowList[i] = '\t\t"' + rowList[i] + '"'
            if i < len(rowList) - 1:
                rowList[i] += ","
            rowList[i] += '\n'
            pattern += rowList[i]
    key = ""
    for i in range(numItems):
        char = charReps[i]
        if (itemData[char] == -1):
            key += '\t"' + char + '": {\n\t\t\t"item": "' + itemDict[char] + '"\n\t\t}'
        else:
            key += '\t"' + char + '": {\n\t\t\t"item": "' + itemDict[char] + '"\n\t\t\t"data": ' + str(itemData[char]) + '\n\t\t}'
        if (i < numItems - 1):
            key += ','
        key += '\n'
    fDir = pjoin(os.getcwd(), "__OUTPUT__", "recipes")
    if (not os.path.exists(fDir)):
        os.makedirs(fDir)
    recipe = open(pjoin(fDir, result.split(":")[1]) + ".json", "w")
    recipe.write('{\n\t"type": "minecraft:crafting_shaped",\n\t"pattern": [\n' + pattern + '],\n\t"key": {\n' + key + '\n\t},' + '\n\t"result": "' + result + '"\n\t}\n}')
    recipe.close()
    print("Recipe created at " + pjoin(fDir, result.split(":")[1]) + ".json")
    time.sleep(1)
