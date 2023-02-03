'''

@CONTEST
Codeforces Round 849 (Div. 4)

@PROBLEM
B - Following Directions

@TIME_LIMIT_PER_TEST
1 second

@MEMORY_LIMIT_PER_TEST
256 megabytes

@INPUT_TYPE
Standard input

@OUTPUT_TYPE
Standard output

@PROBLEM_STATEMENT
Alperen is standing at the point (0,0). He is given a string s of length n
and performs n moves. The i-th move is as follows:
- if s[i] = L, then move one unit left;
- if s[i] = R, then move one unit right;
- if s[i] = U, then move one unit up;
- if s[i] = D, then move one unit down;

There is a candy at (1,1) (that is, one unit above and one unit to the right 
of Alperen's starting point). You need to determine if Alperen ever passes the candy.

@INPUT

- The first line of the input contains an integer t(1<=t<=1000), 
  the number of testcases. 

- The first line of each test case, contains an integer t(1<=t<=50), 
  the number of testcases. 

- The second line of each test case contains a string s of length n 
  consisting of characters L, R, D, and U, denoting the moves Alperen makes.

@OUTPUT

- For each test case, output "YES" (without quotes) if Alperen passes the candy, 
  and "NO" (without quotes) otherwise.

- You can output the answer in any case (for example, the strings "yEs", 
  "yes", "Yes" and "YES" will be recognized as a positive answer).

@SOLUTION_AUTHOR
hiraganime (codeforces) | BrandonMartinez-jar (github)

@SOLUTION_LANGUAGE
Python

@SOLUTION_DATE
03/02/2023

'''

t = int( input() )

if 1 <= t and t <= 1000:

    for i in range( t ):

        n = int( input() )

        if 1 <= n and n <= 50:

            caso = str(input())
            x = 0
            y = 0
            candy = False

            for j in range(n):
                if caso[j] == "R":
                    x = x + 1
                if caso[j] == "L":
                    x = x + -1
                if caso[j] == "U":
                    y = y + 1
                if caso[j] == "D":
                    y = y + -1

                if x == 1 and y == 1 : 
                    candy = True

            print("YES" if candy else "NO")
