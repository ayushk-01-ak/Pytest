# loop
# for loop

# num = [0,1, 2, 3, 4, 5]
# for i in num:
#     print(i)

# s ="Hello World" 
# for i in s:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# while loop
# i=0
# while i<10:
#     print(i)
#     i+=1

# write a program to print the first 10 natural numbers using a for loop and a while loop.
# Using a for loop
# for i in range(1, 11):
#     print(i)

#using while loop
# i=1
# while i<11:
#     print(i)
#     i+=1



count = 0
for i in range(1, 11):
    for j in range(1, 11):
        print (i,j)
        count +=1

print(count)