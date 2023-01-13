# Program to check if user input number is prime or not using a function
# def prime_checker(number):
#     count = 0
#     for i in range(1,number):
#         if number%i == 0:
#             count += 1
#     if count < 2:
#         print("Prime")
#     else:
#         print("Not Prime")




# n = int(input("Check this number: "))
# prime_checker(number = n)

# =======================================
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
