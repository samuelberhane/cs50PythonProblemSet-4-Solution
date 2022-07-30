import random
while True:
    num = input('Level: ')
    try:
        int_num = int(num)
        if int_num < 0:
            pass
        else:
            break
    except:
        pass

while True:
    guess = input('Guess: ')
    try:
        int_guess = int(guess)
        random_number = random.randint(1,int_num)
        if int_guess == random_number:
            print('Just right!')
            break
        elif (int_guess < random_number) and (1 <= int_guess <= int_num):
            print('Too small!')
            continue
        elif (int_guess > random_number) and (1 <= int_guess <= int_num):
            print('Too large!')
            continue
    except:
        pass