def main():
    n = int(input("Input a number: "))
    result = sum(n)
    print(result)
    
def sum(n):
    sum = 0
    for i in range(1, n + 1):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum += i

    return sum
  
if __name__== "__main__":
    main()