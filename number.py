
numbers = [23, 12, 45, 67, 89, 34, 22, 4, 56, 7, 11, 90]

def find_largest_number(numbers):
    """
    Find the largest number in the list.
    """
    if not numbers:
        return None  # Return None if the list is empty
    largest = min(numbers)  # Use the built-in max function
    return largest


def calculate_sum_of_even_numbers(numbers):
    """
    Calculate the sum of all even numbers in the list.
    """
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum


def get_first_n_smallest_numbers(numbers, n):
    """
    Get the first N smallest numbers from the list.
    """
    if not numbers or n <= 0:
        return []  # Return an empty list if the list is empty or n is non-positive
    sorted_numbers = sorted(numbers)  # Sort the numbers
    smallest_numbers = sorted_numbers[:n]  # Get the first N elements
    return smallest_numbers


def main():
    print("\n--- Number Processor ---")
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

    while True:
        print("\nOptions:")
        print("1. Find the largest number")
        print("2. Calculate the sum of even numbers")
        print("3. Get the first N smallest numbers")
        print("Q. Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == '1':
            largest = find_largest_number(numbers)
            if largest is not None:
                print(f"The largest number is: {largest}")
            else:
                print("The list is empty. Please provide a valid list of numbers.")

        elif choice == '2':
            even_sum = calculate_sum_of_even_numbers(numbers)
            print(f"The sum of all even numbers is: {even_sum}")

        elif choice == '3':
            try:
                n = int(input("Enter the value of N: "))
                if n > len(numbers):
                    print("N is larger than the list size. Please try again.")
                else:
                    smallest_numbers = get_first_n_smallest_numbers(numbers, n)
                    print(f"The first {n} smallest numbers are: {smallest_numbers}")
            except ValueError:
                print("Invalid input. Please enter a valid number for N.")

        elif choice == 'Q':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
