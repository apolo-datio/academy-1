# Question 1
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:  
1: Sort based on name;  
2: Then sort based on age;  
3: Then sort by score.  
The priority is that name > age > score.  
If the following tuples are given as input to the program:  
Tom,19,80  
John,20,90  
Jony,17,91  
Jony,17,93  
Json,21,85  
Then, the output of the program should be:  
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]  

## Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.  
We use itemgetter to enable multiple sort keys.

# Question 2
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:  
UP 5  
DOWN 3  
LEFT 3  
RIGHT 2  
¡­  
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.  
Example:  
If the following tuples are given as input to the program:  
UP 5  
DOWN 3  
LEFT 3  
RIGHT 2  
Then, the output of the program should be:  
2  

## Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

# Question 3
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.   
Suppose the following input is supplied to the program:  
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.  
Then, the output should be:  
2:2  
3.:1  
3?:1  
New:1  
Python:5  
Read:1  
and:1  
between:1  
choosing:1  
or:2  
to:1  

## Hints
In case of input data being supplied to the question, it should be assumed to be a console input.  

