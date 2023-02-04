'''

@CONTEST
Advent of code 2015

@PROBLEM
Day 1 - Not Quite Lisp

@INPUT_TYPE
Standard input

@OUTPUT_TYPE
Standard output

@PROBLEM_STATEMENT
  
Any person is trying to deliver presents in a large apartment building, 
but he can't find the right floor - the directions he got are a little confusing. 
He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
  
An opening parenthesis, (, means he should go up one floor, 
and a closing parenthesis, ), means he should go down one floor.
  
The apartment building is very tall, and the basement is very deep; 
he will never find the top or bottom floors.

@PROBLEM_EXAMPLE

- (()) and ()() both result in floor 0.
- ((( and (()(()( both result in floor 3.
- ))((((( also results in floor 3.
- ()) and ))( both result in floor -1 (the first basement level).
- ))) and )())()) both result in floor -3.

 To what floor do the instructions take this person?

@SOLUTION_AUTHOR
hiraganime (codeforces) | BrandonMartinez-jar (github)

@SOLUTION_DATE
30/01/2023

'''

s = input()

count = 0

for i in range( len(s) ):
    count = count + 1 if s[i] == "(" else count - 1

print(count)

