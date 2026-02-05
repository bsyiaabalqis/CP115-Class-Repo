#BATRISYIA BALQIS BINTI ZALLAMI 
#A program that accepts 5 integer input values from the user and stored in a list 

def sorting_numbers():
    numbers=[]

#loop for 5 numbers to be stored in a list
    for i in range(1,6): 
        number=int(input(f"Enter number {i}: "))
        numbers.append(number)

    #sort the numbers in ascending order
    numbers.sort()
    return (f"Numbers in ascending order: {numbers} \nSum of all numbers: {sum(numbers)} \nLargest number: {max(numbers)}")
print (sorting_numbers())
print ("=== Code Execution Succesfull ===")