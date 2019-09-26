def toString(List):
    """This function convert a list to string"""
    return ''.join(List)

def print_to_n(n):
    """This function prints all numbers from 1 to n in growing order"""
    if n >= 1:
        print_to_n(n - 1)
        print(str(n))
    else: # Base case where I went over all the numbers  until n
        return


def print_reversed(n):
    """This function prints all numbers from n to 1 in decreasing order"""
    if n >= 1:
        print(str(n))
        print_reversed(n - 1)



def has_divisor_smaller_than(n, i):
    """This function a number has smaller divisor than a given number"""
    if i == 1 or i==0:
    # Case 1 where inputs is irelevant or the only divisor is 1
        return False
    elif n % i == 0:
    # Base case 2 where we found a divisor which is not 1
        return True
    return has_divisor_smaller_than(n, i - 1)


def is_prime(n):
    """This function checks of a number is prime """
    if n<2:
        return False

    i=int(n**0.5)

    if has_divisor_smaller_than(n, i) == False:
        return True
    return False


def factorial(n):
    """This calculates the factorial of a number"""
    if n == 1:
    # Base case where we get to factorial 1 which equal 1
        return 1
    return n * factorial(n - 1)


def exp_n_x(n, x):
    """This function calculates the value of e^n  as  n goes to infinity"""
    if n == 0:
        return 1
    return (x ** n) / factorial(n) + exp_n_x(n - 1, x)




def play_hanoi(hanoi, n, src, dest, temp):
    """This function solves the hanoi towers game in minimum steps using graphic class"""
    if n<1:
        # Base case when there no more discs to move
        return
    elif n == 1:
        hanoi.move(src, dest)
        return
    play_hanoi(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)



def print_sequences(char_list,n):
    """ The main recursive method to print all possible words in length of n  of chars from a given list """
    if n==0:
        return
    k=n # Set the length of a word
    n = len(set(char_list)) # Set the number of chars
    print_sequences_rec(char_list, "", n, k)



def print_sequences_rec(char_list, prefix, n, k):
    """This function prints all possible words with chars from a given list """

    if (k == 0):
        # Base case: k is 0, we got a  combination of length k so we print it
        print(prefix)
        return

    for i in range(n):
        # One by one add all characters from list
        newPrefix = prefix + char_list[i]
        print_sequences_rec(char_list, newPrefix, n, k - 1)





def print_no_repetition_sequences(char_list, n):
    """ The main recursive method to print all possible strings in length of n  with chars from a list  no reptitions"""
    if n==0:
        return

    print_no_reptition_sequences_rec(char_list, "", n)



def print_no_reptition_sequences_rec(char_list, prefix, n):
    """ This function prints all possible strings in length of n  with chars from a list  no reptitions"""


    if (n == 0):
        # Base case: k is 0, we got a  combination of length k so we print it
        print(prefix)
        return

    for i, char in enumerate(char_list):

        # One by one add all characters from list
        new_prefix=prefix+char
        print_no_reptition_sequences_rec(char_list[:i]+char_list[i+1:],new_prefix, n-1)



def parentheses(n):
    """The main recursive function to  return list of properly opened and closed combinations of n pair of parentheses"""
    str=[""]*2*n
    results_lst=[]
    if(n > 0):
        parentheses_rec(str, 0, n, 0, 0, results_lst)
    return results_lst


def parentheses_rec(str, pos, n, open, close, results_lst):
    """This function built a list of all properly opened and closed combinations of n pair of parentheses"""
    if (close == n):
        # Base case when  we reach  the length of the word
        x=""
        for i in str:
            x+=i
        results_lst.append(x)
        return
    else:
        if (open > close):
            str[pos] = ')'
            parentheses_rec(str, pos + 1, n, open, close + 1, results_lst)
        if (open < n):
            str[pos] = '('
            parentheses_rec(str, pos + 1, n, open + 1, close, results_lst)



def up_and_right(n,k):
    """This function prints all possible paths from (0,0) to the point (n,k) in terms of  only ups and rights """
    if k==0 and n==0:
        # The number of paths from 0,0 to 0,0 is not defined
        return None
    if n<0 or k<0:
        # Not defined since we start from 0,0 and can only move up and right
        return None
    up_and_right_rec(n, k,"")



def up_and_right_rec(n, k,prefix=''):
    """The main recursive function to print all possible paths from p(0,0) to p(n,k) in terms of  only ups and rights"""

    if n == 0 and k == 0:
        # Base case when we got to the point in some combination
        print(prefix)
        return

    elif  n== 0:
        # If we moved right enough, so from now we should only move up
        up_and_right_rec(n, k-1, prefix+'u')
        return


    elif k==0 :
        # If we moved up enough, so from now we should only move right
        up_and_right_rec(n-1, k, prefix+'r')
        return

    # Ordinary case , just continue to move in any possible direction
    up_and_right_rec(n, k - 1, prefix +'u')
    up_and_right_rec(n-1, k, prefix +'r')



def flood_fill(image, start):
    """This function  changes every "." which is right after the start point or to  another "." in one of four
    directions(up down left or right)
     characters to "*"""
    x,y=start
    floodFill_rec(image, x, y, '.', '*')



def floodFill_rec(image, x, y, empty_char, full_char):
    """  The main recursive function Starting at point(x , y)  changes any "." when located in above valid places
      to "*"."""

    imageWidth = len(image)
    imageHeight = len(image[0])



    if image[x][y] != empty_char:
        # Base case. If the current (x, y) character is not the ".",
        # then do nothing.
        return

    # Change the character at image[x][y] to "*"
    image[x][y] = full_char

    # Recursive calls

    floodFill_rec(image, x - 1, y, empty_char, full_char) # left

    floodFill_rec(image, x, y - 1, empty_char, full_char) # up

    floodFill_rec(image, x + 1, y, empty_char, full_char) # right

    floodFill_rec(image, x, y + 1, empty_char, full_char) # down


