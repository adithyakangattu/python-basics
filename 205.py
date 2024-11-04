#write a python program that :

#intilizes a variable j with the value 0

#uses a while loop to iterate as long as j is less than 5
# in each iteration increases the value of j by 1

#if j is equal to 2 use the continue statement to skip the
#rest of the loop's body and continue to the next iteration

# print the value of j for all other iteration ?

j = 0
while j <= 5:
     j += 1
     if j == 2:
         continue
     print(j)
