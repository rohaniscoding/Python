def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

start_range = int(input("Enter the Starting Range: "))
end_range = int(input("Enter the Ending Range: "))

print("The Prime Numbers in the range", start_range, "and", end_range, "are:")
for num in range(start_range, end_range + 1):
    if is_prime(num):
        print(num)
