# Afruza's Starting Point(Home): 0-th point, which is her home
# Mall's Location(X)
# Moving Time: Afruza can move one point(either left or right) in one second

# Task: Afruza needs to go from her house (0-th point) to the mall(X-th point) and then come back home.

X = int(input())

#Calculating the minumum time for the round trip
time_needed = 2 * abs(X)

print(time_needed)


#to solve this problem, we need to calculate the minumum amount of time Malike needs to reach floor(n)
#consider both the elevator and stairs 

#n - the destination floor(where Malika wants to go)
#m - the current floor where the elevator is located 
#t1 - the time it takes for the elevator to move one floor up or one floor down
#t2 - the time it takes for Malika to move one floor using stairs

# first, the elevator needs to come to Malika's floor from m to 1.
# The time taken is abs(m-1)*t1

# then, the elevator will take Malika from floor 1 to floor n. 
# The time taken for this is abs(n-1)*t1
# total elevator time = abs(m-1)*t1+abs(n-1)*t1
# the time is taken is simply abs(n-1)*t2

#Input values 
n, m, t1, t2 = map(int, input().split())

#Time using the elevator 
elevator_time = abs(m-1) * t1 + abs(n-1) * t1 

#Time using the stairs
stairs_time = abs(n-1) *t2

#Output the mininum time
print(min(elevator_time, stairs_time))




#The task is to find the name with the highest beauty, and if there are multiple names with the same beauty, 
#return the one that appears first in the input list.

#Input reading 
n = int(input()) #number of names 
beautiful_letters = set(input()) #the set of beautiful letters

#Initialize variables to track the most beautiful name
most_beautiful_name = ""
max_beauty = -1

#Iterate through each name
for _ in range(n):
    name = input() #current name
    beauty = sum(1 for letter in name if letter beautiful_letters) # count beautiful letters in the name

if beauty > max_beauty:
    max_beauty = beauty
    most_beautiful_name = name 

#Output the most beautiful name
print(most_beautiful_name)


# the next task is to find the maximum power among all pairs(i, j), where i ≠ j in the array
# the power of a pair is determined based on whether the numbers in the pair are powers of 2

# approach

# 1)parse the input 
# 2)for each statement, check if it is a power of 2
# 3)if it is, calculate the power(exponent).
# 4)track the maximum power
# 5)output the maximum power

import math

#function to determine if a number is a power of 2 and return it's exponent

def power_of_2(n):
    if n > 0 and (n & (n - 1)) == 0:
        return int(math.log2(n)) # return the exponent d 
    return -1 #return if it's not a power of 2

#input reading 
n = int(input()) #number of elements
a = list(map(int, input().split())) # the array of integers 

#variable to track the maximum power
max_power = -1

#loop through each element and calculate its power 
for num in a:
    power = power_of_2(num)
    if power > max_power:
        max_power = power

#Output the maximum power 
print(max_power)