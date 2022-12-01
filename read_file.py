with open("test.txt", 'r') as rf:
   # print("\n".join(rf.readlines()))
   #print(rf.read())
   number_of_lines=rf.readlines()
   print(type(number_of_lines))
   for each_line in number_of_lines:
        #print(each_line)
        print(len(each_line.strip("\n")),each_line.strip("\n"))


