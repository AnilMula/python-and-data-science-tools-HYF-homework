# Write a Python script to check whether a given key already exists in a dictionary

def checkKeyExist(dict,newKey,newValue):
    # function takes 3 arguments a dictionary, new key and value
    dictKeys = [] #an empty list to hold keys

    # get keys from dictionnary and add to list
    for key in car.keys():
        dictKeys.append(key)

    if newKey in dictKeys:
        return f"key {newKey} already exist"
    else:
        dict[newKey] = newValue
        return dict

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(checkKeyExist(car, "brand", "q"))