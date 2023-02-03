'''

@CONTEST
Codeforces Round 849 (Div. 4)

@PROBLEM
A - Codeforces Checking

@TIME_LIMIT_PER_TEST
1 second

@MEMORY_LIMIT_PER_TEST
256 megabytes

@INPUT_TYPE
Standard input

@OUTPUT_TYPE
Standard output

@PROBLEM_STATEMENT
Given a lowercase Latin character (letter), 
check if it appears in the string codeforces

@INPUT

- The first line of the input contains an integer t (1<=t<=26), 
  the number of test cases.

- The only line of each test case contains a character c, 
  a single lowercase Latin character (letter).

@OUTPUT

- For each test case, output "YES" (without quotes)
  if c satisfies the condition, and "NO" (without quotes) otherwise.

- You can output the answer in any case (for example, the strings 
  "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

@SOLUTION_AUTHOR
hiraganime (codeforces) | BrandonMartinez-jar (github)

@SOLUTION_LANGUAGE
Python

@SOLUTION_DATE
03/02/2023

'''

t = int( input() )

if 1 <= t and t <= 26:

    for i in range(0, t):
        a = str( input() )
        continuar = False
        array = ("c", "o", "d", "e", "f", "o", "r", "c", "e", "s")
        for i in array : 
            if i == a: 
                continuar = True
        print( "YES" if continuar else "NO" )
