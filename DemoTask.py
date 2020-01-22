import re

# Inputs that can be given to the console: [1,1,2,2,2,2,3,3,2,2,4,5]; [11,22,33,11,222,11,222] [2,@,@,1,2,%,^,EGR,1111,111,2,^,&]; !!,@,1,2,%,^,EGR,1111,111,2,^,&
# [11.11,22,33,11,222,11,222, 11.11]
# [11.aa,22,33,11,222,11,222, 11.aa]
# [-11.01,22,33,11,-222,11,222, 11,11.02,11.02,-8, 8,-222]
# get input from console, and strip all the non-numeric characters
def get_console_input():
    in_console = input().strip()
    in_console = re.sub('[^-0-9.]',' ',in_console)  # remove all non-numeric characters => a string
    in_console_lst = in_console.split(' ')  # transform in_console to string by splitting it after ' '

    #eliminate unnecessary ''
    console_lst_numbers= []
    for i in range(0,len(in_console_lst)):
        if in_console_lst[i] != '':
            console_lst_numbers.append(in_console_lst[i])

    return console_lst_numbers


# find duplicates and write a dictionary that contains the contains: key: value of duplicate; value - number of times the duplicate was found
def find_duplicates(list_in_numbers):
    dup_dict = {}

    for i in range(0,len(list_in_numbers)):
        dup_count = 0
        for j in range(0,len(list_in_numbers)):
            if list_in_numbers[i] == list_in_numbers[j]:
                dup_count = dup_count + 1
                dup_value = list_in_numbers[j]
        if dup_count >1:
            dup_dict[dup_value] = dup_count
    return dup_dict


# calculate the sum of the duplicates
def sum_of_duplicates(duplicates_dict):
    sum_of_dup = 0
    for i in duplicates_dict.keys():
        sum_of_dup = sum_of_dup + float(i)
    return sum_of_dup



print("Please enter a number a list of numbers - the program will find the duplicates and calculate the sum of the duplicates")
console_in_lst = get_console_input()

if console_in_lst == []:
    print("No numbers where inserted, the sum and duplicates dictionary will be empty, please try agian")
elif len(console_in_lst) == 1:
    print("Only one number was inserted, the sum and duplicates dictionary will be empty, please try agian")



print("User input was converted to a list of numbers:",console_in_lst)

duplicates_found = find_duplicates(console_in_lst)
print("Dictionary of duplicates found is:",duplicates_found)

print("Sum of duplicates found is:",sum_of_duplicates(duplicates_found))
