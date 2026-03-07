import random

MIN=1
MAX=100

a=random.randint(MIN,MAX)
b=-1
min_num=MIN
max_num=MAX
while b!=a:
    try:
        b=int(input("give me a number: "))
    except ValueError:
        print("please enter a number")
        continue
    if b<min_num or b>max_num:
        print("wrong number")
        continue
    else:
        if b == a:
            print("Great! You are right!")
            break
        elif b < a:
            min_num = b
            print(f'the answer is between {min_num} and {max_num}')
        else:
            max_num = b
            print(f'the answer is between {min_num} and {max_num}')
