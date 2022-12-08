#join operation

x="python"
y="_".join(x) # the join function withh give space between
print(y)
print(x)
print("*".join(x)) #will print the word with * inbetween
print("\n".join(x))
print("\t".join(x))
print("\a".join(x))

# center how to centralize your code
my_str="python"
my_new_string="python scripting"
my_str3="string operation"
print(my_str.center(20))
print(f"{my_str.center(20)}\n{my_new_string.center(20)}\n{my_str3.center(20)}")

#zfill operation this will fill the remaining space with zero eg
my_str="python"
print(my_str.zfill(10)) # it will count length of the string and the left over will be filled with zeros = 0000python

