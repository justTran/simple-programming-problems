def main():
    n = int(input("Please enter a number: "))
    selection = input("Do you want the 1. product or the 2. sum? (Enter 1 for product or 2 for sum) ")

    if (selection == '1'):
        result = product(n)

    elif (selection == '2'):
        result = sum(n)

    else:
        print("Invalid answer.")
        return None

    print(result)

def product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i

    return product

def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum
  
if __name__== "__main__":
    main()