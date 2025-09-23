# recurrence_relations.py

def print_recurrences():
    print("\n--- Recursive Functions and Their Recurrence Relations ---\n")

    # 1. Factorial
    print("1. Factorial")
    print("   T(n) = T(n-1) + O(1),   T(0) = O(1)\n")

    # 2. Fibonacci
    print("2. Fibonacci")
    print("   T(n) = T(n-1) + T(n-2) + O(1),   T(0)=T(1)=O(1)\n")

    # 3. Binary Search
    print("3. Binary Search")
    print("   T(n) = T(n/2) + O(1),   T(1) = O(1)\n")

    # 4. Merge Sort
    print("4. Merge Sort")
    print("   T(n) = 2T(n/2) + O(n),   T(1) = O(1)\n")

    # 5. Quick Sort
    print("5. Quick Sort")
    print("   Average Case: T(n) = 2T(n/2) + O(n)")
    print("   Worst Case:   T(n) = T(n-1) + O(n)\n")

    # 6. Tower of Hanoi
    print("6. Tower of Hanoi")
    print("   T(n) = 2T(n-1) + O(1),   T(1) = O(1)\n")

    # 7. Exponentiation (Power Function)
    print("7. Power (x^n)")
    print("   T(n) = T(n/2) + O(1),   T(0) = O(1)\n")

    print("--- End ---")


# Run only when executed directly
if __name__ == "__main__":
    print_recurrences()
