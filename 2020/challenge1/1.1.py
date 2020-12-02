import itertools

# create an empty array
numbers_array = []

# make sure the list of numbers given by the challenge are in a file called 1.1.numbers.txt
# open the file and add the numbers to the array
with open("1.1.numbers.txt") as filehandle:
    numbers_array = [current_number.strip() for current_number in filehandle.readlines()]
print(numbers_array)

# set the array to int
integer_array = list(map(int, numbers_array))
print(integer_array)

# set the target to 2020
target = 2020

# look for the 2 numbers that combined equal the target
for numbers in itertools.combinations(integer_array,2):
    if sum(numbers) == target:
        
        # print the index in the array for those numbers
        print([integer_array.index(number) for number in numbers])
        
        # add the number by the index as integer to an array called number_index
        number_index = list(map(int, (integer_array.index(number) for number in numbers)))
        
        # print the content of the array index
        print(number_index)
        
        # print the numbers with that index
        print (numbers)
        
        # variable called result (has to be 1, because if you multiply by 0 everything is 0
        result = 1
        
        # for every item i in the array number multiply it with the item
        for i in numbers:
            result *=i
            
            # print the result
            print(result)

## Sources:
# https://stackoverflow.com/questions/49761846/how-to-sum-two-numbers-in-a-list
# https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
# https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
# https://stackoverflow.com/questions/46699420/python-for-loop-multiplication
