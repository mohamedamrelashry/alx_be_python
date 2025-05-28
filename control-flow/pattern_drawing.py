number = int(input("Enter the size of the pattern:"))
iteration = 1
while number >= iteration : 
    for x in range(0,number):
        print("*",end  ="")
    print("")
    iteration+=1
