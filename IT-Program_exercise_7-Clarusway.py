# Exercise 1:
# gen_itt = 10
#
# total_sum = 0
#
# for x_line_itt in range(gen_itt + 1):
#     total_sum += x_line_itt
#     print(total_sum)

# Exercise 2:
# gen_itt = 10
# var_numb = 5
#
# for numb in range(gen_itt + 1):
#     table_numb = numb * var_numb
#     print(f"The table of 5 in: {numb} x {var_numb} = {table_numb}")

# Exercise 3:
# range_itt_start = 2950
# range_itt_exc = 5211
# for digit in range(range_itt_start, range_itt_exc):
#     if digit % 13 == 0 and digit % 9 == 0:
#         print(digit)

# Exercise 4:
# var_numb = 1354
# odd_digits = []
# even_digits = []
#
# for digit in str(var_numb):
#     digit = int(digit)
#     even_digit = digit % 2 == 0
#     odd_digit = digit % 2 != 0
#     if odd_digit:
#         odd_digits.append(digit)
#         print(f"Odd numbers are: {digit}")
#     if even_digit:
#         even_digits.append(digit)
#         print(f"Even numbers are: {digit}")
#
# print(f"This number has {len(odd_digits)} odd digits "
#       f"and {len(even_digits)} even digits. ")

# Exercise 5:
# user_input = input("Create a password (4-6 alphabetic characters): ")
#
# while len(user_input) < 4 or len(user_input) > 6 or not user_input.isalpha():
#     print("That does not fulfill the requirements, try again")
#     user_input = input("Create a password (4-6 alphabetic characters): ")
#
# user_input_2 = input("Enter your password: ")
#
# while user_input_2 != user_input:
#     print("Passwords do not match. Try again.")
#     user_input_2 = input("Enter your password: ")
# else:
#     print("Password confirmed.")
























