# Python3 code to demonstrate  
# swap of key and value 
   
# initializing dictionary 
old_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
 
new_dict = dict([(value, key) for key, value in old_dict.items()])
   
# Printing original dictionary 
print ("Original dictionary is : ")
print(old_dict) 
 
print()
 
# Printing new dictionary after swapping keys and values
print ("Dictionary after swapping is :  ") 
print("keys: values")
for i in new_dict:
    print(i, " :  ", new_dict[i])