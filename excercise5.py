# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
def fibonacci(numbers):
    f2 = 0
    f1 = 1
    for x in range(numbers):
        if x == 0:
            print(f"term:{x} / number:{f2}")
        elif x == 1:
            print(f"term:{x} / number:{f1}")
        else:
            sum = f1 + f2
            print(f"term:{x} / number:{sum}")
            f2 = f1
            f1 = sum
fibonacci(51)
