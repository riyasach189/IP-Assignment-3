#COMPLETED

"""
Print the pattern given below using recursion - no loops are allowed. 
You are given a value n - print a diamond which will have 2n-1 rows, and 2n columns, 
as shown in the figure. (In the top row print n+n stars, in the next (n-1) stars on left and 
right and 2 blanks in the middle, and so on till you have 1 star each on left and right; then you 
reverse this).

5
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *

Suggestion: Have two recursive functions - one to print the top half, and other to print the bottom half.
"""

#Assumption: there is a space after every *

n = int(input("Enter n: "))

def star_print_fwd(n,temp):

    if temp==0:
        return temp
    
    else:
        print("* "*temp + "  "*2*(n-temp) + "* "*temp)
        star_print_fwd(n,temp-1)

    return None

def star_print_bkd(n,temp):
    
    if temp>n:
        return temp
    
    else:
        print("* "*temp + "  "*2*(n-temp) + "* "*temp)
        star_print_bkd(n,temp+1)

    return None

star_print_fwd(n,n)
star_print_bkd(n,2)