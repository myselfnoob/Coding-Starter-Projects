def perfect_num_checker(num:int) -> bool:
    """
    Perfect number, a positive integer that is equal 
    to the sum of its proper divisors.

    Usage examples:

    >>> perfect_num_checker(6)
    True
    >>> perfect_num_checker(28)
    True
    >>> perfect_num_checker(8128)
    True
    >>> perfect_num_checker(79)
    False
    >>> perfect_num_checker(531)
    False

    """

    temp = 0
    for i in range(1, num):
        if num % i == 0:
            temp += i
    return temp == num

if __name__ == "__main__":
    number = int(input("Enter a number: ").strip())
    print(f"\n\tGiven number is {number} \n\t{perfect_num_checker(number) = }\n")