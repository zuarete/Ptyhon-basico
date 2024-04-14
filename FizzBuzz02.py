def fizzbuzz(n):
    a=""
    if n % 3 == 0 and n % 5 == 0:
        a="FizzBuzz"
    else:
        if n% 3 == 0:
            a="Fizz"
        else:
            if n % 5 == 0:
                a="Buzz"
            else:
                a=n 
    return a


a=int(input("Informe o número : "))
print(fizzbuzz(a))