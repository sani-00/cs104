for number in range(1,101):
    if (number % 3 == 0 or number % 10 == 3 or number // 10 == 3) and (number % 5 == 0 or number % 10 == 5 or number // 10 == 5):  
        print("FizzBuzz")
    elif number % 3 == 0 or number % 10 == 3 or number // 10 == 3:
        print("Fizz")
    elif number % 5 == 0 or number % 10 == 5 or number // 10 == 5:
        print("Buzz") 
    else:
        print(number)
        
