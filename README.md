README
This program finds duplicates in a given array, add the duplicates and the number of repetitions in a dictionary ex: {'2':3} - 
value 2 was found 3 times, and calculates the sum of the duplicates

PREREQUESITES: 
- have installed Python 3; can be found at: https://www.python.org/downloads/
- for Windows make sure to add Python to enviroment variables

INSTALLATION:

1.Clone the project from the git repository

2.Open CMD, and navigate to the directory where the python DemoTask.py file is located

3.Run the command: python DemoTask.py

4.Enter numbers from command line
ex of inputs that can be given: [1,2,2,3,4,4,4,5]
[2,@,@,1,2,%,^,EGR,1111,111,2,^,&]
1 2 2 3 3
1 @ # $ 5 5 5 5
1,2,2,2,2,100, 1000, 1000

5.The output for [2,@,@,1,2,%,^,EGR,1111,111,2,^,&], should be:
User input was converted to a list of numbers: ['2', '1', '2', '1111', '111', '2']
Dictionary of duplicates found is: {'2': 3}
Sum of duplicates found is: 3
