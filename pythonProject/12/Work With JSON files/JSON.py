############################## Writing JSON With Python ###############################
#######################################################################################
#######################################################################################

# Python supports the JSON format through the built-in module named json.
# The json module is specifically designed for reading and writing strings formatted as JSON

# One of the most common actions when working with JSON in Python is to convert a Python dictionary into a JSON object.
# To get an impression of how this works, hop over to your Python REPL and follow along with the code below:


############################## .dumps() ###############################
# import json
# food_ratings = {"organic dog food": 2, "human food": 10}
# result = json.dumps(food_ratings)
# print(type(result))

# It’s important to understand that when you use .dumps(), you get a Python string in return.
# In other words, you don’t create any kind of JSON data type. The result is similar to what you’d get if you used Python’s built-in str() function:

# After importing the json module, you can use .dumps() to convert a Python dictionary to a JSON-formatted string, which represents a JSON object.

############################## Serialize Other Python Data Types to JSON ###############################


# The json module allows you to convert common Python data types to JSON. Here’s an overview of all Python data types and values that you can convert to JSON values:
#
# Python	--> JSON
# dict	--> object
# list	--> array
# tuple	--> array
# str	--> string
# int	--> number
# float	--> number
# True	--> true
# False	--> false
# None	--> null

# Note that different Python data types like lists and tuples serialize to the same JSON array data type.
# This can cause problems when you convert JSON data back to Python, as the data type may not be the same as before.

# You can’t use dictionaries, lists, or tuples as JSON keys. For dictionaries and lists,
# this rule makes sense as they’re not hashable. But even when a tuple is hashable and allowed as a key in a dictionary,
# you’ll get a TypeError when you try to use a tuple as a JSON key:

#available_nums = {(1, 2): True, 3: False}
#son.dumps(available_nums)
# Traceback (most recent call last):
#   ...
# TypeError: keys must be str, int, float, bool or None, not tuple

# By providing the skipkeys argument, you can prevent getting a TypeError when creating JSON data with unsupported Python keys:

#json.dumps(available_nums, skipkeys=True)
# '{"3": false}'


############################## Write a JSON File With Python ###############################
#######################################################################################
#######################################################################################

# To write Python data into an external JSON file, you use json.dump(). This is a similar function to the one you saw earlier, but without the s at the end of its name:

# import json
#
# dog_data = {
#   "name": "Frieda",
#   "is_dog": True,
#   "hobbies": ["eating", "sleeping", "barking",],
#   "age": 8,
#   "address": {
#     "work": None,
#     "home": ("Berlin", "Germany",),
#   },
#   "friends": [
#     {
#       "name": "Philipp",
#       "hobbies": ["eating", "sleeping", "reading",],
#     },
#     {
#       "name": "Mitch",
#       "hobbies": ["running", "snacking",],
#     },
#   ],
# }
#
# with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\dog_info.json", mode="w", encoding="utf-8") as write_file:
#     json.dump(dog_data, write_file)
#
# The json.dump() function has two required arguments:
#
# --> The object you want to write
# --> The file you want to write into
#
# Other than that, there are a bunch of optional parameters for json.dump().
# The optional parameters of json.dump() are the same as for json.dumps(). You’ll investigate some of them later in this tutorial when you prettify and minify JSON files.


############################## Reading JSON With Python ###############################
#######################################################################################
#######################################################################################

# In parallel to json.dumps() and json.dump(), the json library provides two functions to deserialize JSON data into a Python object:
#
# json.loads(): To deserialize a string, bytes, or byte array instances
# json.load(): To deserialize a text file or a binary file

############################## Convert JSON Objects to a Python Dictionary ##############################

# import json
# dog_registry = {1: {"name": "Frieda"}}
# dog_json = json.dumps(dog_registry)


# By passing dog_registry into json.dumps(), you’re creating a string with a JSON object that you save in dog_json.
# If you want to convert dog_json back to a Python dictionary, then you can use json.loads():

# new_dog_registry = json.loads(dog_json)
# print(type(new_dog_registry))
# print(new_dog_registry)

############################## Deserialize JSON Data Types ############################
#######################################################################################
#######################################################################################


# import json
#
# with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\Work With JSON files\hello_frieda.json", 'r') as opened_file:
#     result = opened_file.read()
#
# dict_file = json.loads(result)
# print(dict_file)
#
#
# with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\Work With JSON files\new_text.py", 'x+') as new_file:
#     new_file.write(str(dict_file))
