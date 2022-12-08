my_name="alexia"
my_new_name='python developer'
my_info="""i am an aws cloud engineer 
and iam very grateful"""
print(f"my name is: {my_name}\nmy new name is: {my_new_name}\nmy info is: {my_info}" )

my_str=""
my_new_str=" "
print(f'{bool(my_str)}')
print(f'{bool(my_new_str)}')  #has space in between the " "

#indexing
my_fav_scripting="python"
print(f'{my_fav_scripting}') #or
print(my_fav_scripting)
print(my_fav_scripting[0]) #will print p only indexing [0,1,2,3,4,5 ...n]
print(my_fav_scripting[-1]) # will give u the last character of the word which is "n" no need to count the index value
print(my_fav_scripting[0:5]) # count from 0 to 5
my_name="alexia"
my_new_name='python developer'
my_info="""i am an aws cloud engineer 
and iam very grateful"""
print(f"my name is: {my_name}\nmy new name is: {my_new_name}\nmy info is: {my_info}" )

my_str=""
my_new_str=" "
print(f'{bool(my_str)}')
print(f'{bool(my_new_str)}')  #has space in between the " "

#indexing
my_fav_scripting="python"
print(f'{my_fav_scripting[0]}') #or
print(my_fav_scripting)
print(my_fav_scripting[0]) #will print p only indexing [0,1,2,3,4,5 ...n]
print(my_fav_scripting[-1]) # will give u the last character of the word which is "n" no need to count the index value
print(my_fav_scripting[0:5]) # count from 0 to 

#slicing
print(my_fav_scripting[0:]) #print from 0 to last character its call SLICING operation
print(my_fav_scripting[:5]) #still slicing
str_0_4=my_fav_scripting[0:5]
print(str_0_4)


#delete
del my_fav_scripting #or
my_fav_scripting="python tutorials" #complete new line
print(my_fav_scripting)

#find the length of a string
my_str_len=len(my_fav_scripting)
print(f'length of a given string is: {my_str_len}') #or
print(f'length of a given string is: {len(my_fav_scripting)}')

#concatenante add and substrate
my_str1="python"
my_str2="scripting"
my_str3=my_str1+" "+my_str2
print(my_str3)
my_str3=my_str1+" "+my_str2+" "+"tutorials" #add a variable
print(my_str3)
