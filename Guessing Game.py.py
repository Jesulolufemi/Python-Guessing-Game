# QUESTION 1
# def perfect_numbers(numbers):
#     sum_of_divisors = sum(i for i in range(1, numbers) if numbers % i == 0)
#     return sum_of_divisors == numbers
# while True:
#     user_input = int(input("Please enter a number to check: "))
#     if perfect_numbers(user_input):
#         print(f"{user_input} is perfect")
#     else:
#         print(f"{user_input} is not perfect")
# perfect_numbers()


#QUESTION 2
# def classification_of_range(upper_limit):
#     for num in range(2, upper_limit + 1):
#         sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
#         classification = "Perfect" if sum_of_divisors == num else ("Abundant" if sum_of_divisors > num else "Deficient")
#         print(f"{num} is {classification}")
# classification_of_range(upper_limit = int(input("What is the upper number for the range: ")))

# QUESTION 3
# import random
# def hi_low():
#     hidden_number = random.randint(0, 100)
#     print("Yuppie! Welcome to the hi-low guessing game!")
#     print("Guess the hidden number between 0 and 100.")
#     while True:
#         user_input = int(input("Enter your guess (or a number outside the range to end game): "))
#         if 0 <= user_input <= 100:
#             if user_input == hidden_number:
#                 print(f"Congratulations! You guessed the hidden number {hidden_number}!")
#                 break
#             elif user_input < hidden_number:
#                 print("Too low! Try a higher number.")
#             else:
#                 print("Too high! Try a lower number.")
#         else:
#             print("You just ended the game. The hidden number was:", hidden_number)
# hi_low()

# QUESTION 4
# def hailstone_sequence(initial_number):
#     sequence = [initial_number]
#     while initial_number != 1:
#         if initial_number % 2 == 0:
#             initial_number //= 2
#         else:
#             initial_number = 3 * initial_number + 1
#         sequence.append(initial_number)
#     print(sequence)
# hailstone_sequence(initial_number=int(input("Enter the initial number for the hailstone sequence: ")))

