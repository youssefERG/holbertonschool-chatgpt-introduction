import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    A factorial is the product of all positive integers less than or equal to n.
    For example: 4! = 4 * 3 * 2 * 1 = 24
    Base case: 0! = 1

    Parameters:
        n (int): A non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.

    Raises:
        RecursionError: If n is negative (infinite recursion).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main execution
if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)