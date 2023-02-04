'''

@CONTEST
Advent of code 2015

@PROBLEM
Day 2 - I Was Told There Would Be No Math

@INPUT_TYPE
Standard input

@OUTPUT_TYPE
Standard output

@PROBLEM_STATEMENT
  
The elves are running low on wrapping paper, and so they need to 
submit an order for more. They have a list of the dimensions 
(length l, width w, and height h) of each present, and only want 
to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), 
which makes calculating the required wrapping paper for each gift a little 
easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
The elves also need a little extra paper for each present: 
the area of the smallest side.

@PROBLEM_EXAMPLE

- A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 
  square feet of wrapping paper plus 6 square feet of slack, 
  for a total of 58 square feet.

- A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 
  square feet of wrapping paper plus 1 square foot of slack, 
  for a total of 43 square feet.

All numbers in the elves' list are in feet. 
How many total square feet of wrapping paper should they order?

@SOLUTION_AUTHOR
hiraganime (codeforces) | BrandonMartinez-jar (github)

@SOLUTION_DATE
31/01/2023

'''

s  = str( input() )

a  = ""
params = []
for i in range( len(s) ):

    if not s[i] == "x":
       a = str( a ) + str( s[i] )

    if s[i] == "x" or i == len(s)-1:
        params.append( int( a ) ) 
        a = ""

res = 2*params[0]*params[1] + 2*params[0]*params[2] + 2*params[1]*params[2]

print(res)