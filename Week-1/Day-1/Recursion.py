def sum_digits(n):
    if n == 0:              
        return 0
    return n % 10 + sum_digits(n // 10)

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == reverse_number(n)

def analyze_number():
    num = int(input("Enter a number: "))

    print("Sum of digits:", sum_digits(num))
    print("Number of digits:", count_digits(num))
    print("Reversed number:", reverse_number(num))

    if is_palindrome(num):
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")

analyze_number()