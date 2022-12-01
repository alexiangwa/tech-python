name_of_file = input("What's the name of the file?: ")
with open(name_of_file, 'r') as rf:
   # print("\n".join(rf.readlines()))
   #print(rf.read())
   number_of_lines=rf.readlines()
   # print(number_of_lines[0]) #print item at index 0 i.e first item
   # print(type(number_of_lines))
   for each_line in number_of_lines:
      # print(each_line)
      actual_line = each_line.strip("\n")# strip out \n
      number_of_xters = len(actual_line) 
      statement = f"{actual_line}: has {number_of_xters} characters"
      print(statement)
      # print(len(each_line.strip("\n")),each_line.strip("\n"))


