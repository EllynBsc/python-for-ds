words = ['cat', 'wolf', 'beetle']

# for loop on a list:
# for element in words:
#     print(element.upper())
    
# List comprehension:
# final_list = [element.upper() for element in words]
# print(final_list)

# index with for loop(with enumerate):
# for index,element in enumerate(words):
#     print(index, element)

# For loop On a dict:(with .items()):
# instruments = {'paul': 'bass', 'ringo': 'drums'}

# print(instruments.items()) 
# #[('paul', 'bass'), ('ringo', 'drums')])
# # a list of tuples of first the keys, and then the values
# for key, value in instruments.items():
#     print(key, value)


#name_of_dict.items() for dictionnaries
#.enumerate(name_of_list) for list with index
i = 0
while i <= 4:
    print(i)
    # i = i + 1