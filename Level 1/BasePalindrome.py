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