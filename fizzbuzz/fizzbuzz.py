for cisla in range(1, 31):
    if cisla % 3 == 0 and cisla % 5 == 0:
        print("FizzBuzz")
    elif cisla % 3 == 0:
        print("Fizz")
    elif cisla % 5 == 0:
        print("Buzz")
    else:
        print(cisla)
