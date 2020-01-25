# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

class Divisible(object):
    # def __init__(self, nr1, nr2):
    #     self.nr1 = nr1
    #     self.nr2 = nr2

    def findDivisibleNumbers(self, limit1, limit2):
        list_numbers = []
        for i in range(limit1, limit2):
            if (i % 7 == 0) & (i % 5 != 0):
                list_numbers.append(str(i))
        return list_numbers

    def printNumbers(self, limit1, limit2):
        numbers_list = self.findDivisibleNumbers(limit1, limit2)
        print(','.join(numbers_list))



# DivisibleNumbers = Divisible(2000, 3200)
DivisibleNumbers = Divisible()
DivisibleNumbers.printNumbers(2000, 3200)













