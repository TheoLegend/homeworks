def find_rightmost_set_bit(n):
    """
    Returns the value of the rightmost set bit in n.
    If n is 0, returns 0 since there are no set bits.
    """
    return n & -n

# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))
        result = find_rightmost_set_bit(num)
        print(f"Rightmost set bit of {num} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")
