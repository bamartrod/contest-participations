'''

@CONTEST
Codeforces Round 849 (Div. 4)

@PROBLEM
C - Prepend and Append

@TIME_LIMIT_PER_TEST
1 second

@MEMORY_LIMIT_PER_TEST
256 megabytes

@INPUT_TYPE
Standard input

@OUTPUT_TYPE
Standard output

@PROBLEM_STATEMENT
Timur initially had a binary string s (possibly of length 0). 
He performed the following operation several (possibly zero) times:

Add 0 to one end of the string and 1 to the other end of the string. 
For example, starting from the string 1011, you can obtain either 010111 or 110110.

You are given Timur's final string. What is the length of the shortest possible string 
he could have started with? A binary string is a string (possibly the empty string) 
whose characters are either 0 or 1.

@INPUT

- The first line of the input contains an integer t (1<=t<=100), 
  the number of testcases.

- The first line of each test case contains an integer n (1<=n<=2000), 
  the length of Timur's final string. 

- The second line of each test case contains a string s of length n 
  consisting of characters 0 or 1, denoting the final string.

@OUTPUT

- For each test case, output a single nonnegative integer, 
  the shortest possible length of Timur's original string. 
  Note that Timur's original string could have been empty, 
  in which case you should output 0.

@SOLUTION_AUTHOR
hiraganime (codeforces) | BrandonMartinez-jar (github)

@SOLUTION_LANGUAGE
Python

@SOLUTION_DATE
03/02/2023

'''

t = int( input() )

if 1 <= t and t <= 100:

    for i in range( t ):

        n = int( input() )

        if 1 <= n and n <= 2000:

            s = str(input())

            res = 0;

            megacontinuar = True

            for j in range(round(n/2)):

                continuar = False

                if s[j] != s[n-1-j]:
                    continuar = True
                else:
                    megacontinuar = False

                if continuar and megacontinuar:
                    res = res + 1

            print(n - res*2)
