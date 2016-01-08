"""
Backward and forward
====================

The sign outside reads: Name no one man.

"Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician, has a revelation. "Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!"

To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer base b, at least 2, in which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) n = 0
Output:
    (int) 2

Inputs:
    (int) n = 42
Output:
    (int) 4
"""

def convert_number_to_base(number, target_base):
    """
    :return: string representation of base_ten_number converted into target_base
    """
    digits = []

    if number == 0:
        return '0'

    while number > 0:
        digits.insert(0, str(number % target_base))
        number = number // target_base

    return ''.join(digits)

def check_palindrome(string):
    """
    :return: boolean dependent upon whether input string is a palindrome
    """
    return string == string[::-1]

def answer(n):
    """
    :return: the lowest base in which n is a palindrome
    """
    base = 2
    while True:
        if check_palindrome(convert_number_to_base(n, base)):
            return base
        base += 1