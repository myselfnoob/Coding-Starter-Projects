import math

def is_krishnamurthy_number(num:int) -> bool:

    """
    Krishnamurthy number is a number which is equal to 
    the sum of the factorials of its digits
    For example: 145 is a Krishnamurthy number 
    because 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

    """

    answer = 0
    temp = str(num)
    for i in temp:
        answer += math.factorial(int(i))
    return num == answer

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"{is_krishnamurthy_number(number)= }")
