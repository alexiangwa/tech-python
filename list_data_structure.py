#list
my_list =[]
my_list1=[3,7,9,0,"python",5.6,]

#note that you can also convert a list to a boolean
print(bool(my_list))

#bool(empty_list)-->false
#bool(noon-empty_list)-->true
#when counting list indexes from right to left (0,1,2,3,4,5...n) from left to right  (-1.-2,-3....n)
print(my_list1,type(my_list1))
print(my_list1[3])
print(my_list1[5])
print(my_list1[-2])

#write a syntax to deplay only the y in pthon from a list
print(my_list1[3][1]) #[1] is the index position of y in python

#another way of writing your list from start to finish 
print(my_list1[:]) #or
print(my_list1)
print(my_list1[1:]) # will print from index 1 to last



