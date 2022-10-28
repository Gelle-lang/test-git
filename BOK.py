
#choice = int(input('choose a number'))
def fizz_buzz(choice):
    if choice%3 == 0 and choice % 5== 0:
        print('FizzBuzz')
    elif choice%3 == 0 and  choice % 5 != 0:
        print('Fizz')
    elif choice%3  != 0 and choice % 5== 0:
        print('Buzz')
    else:
        print(choice)

#fizz_buzz(choice)
print(-10/3, -10//3, int(-10/3))