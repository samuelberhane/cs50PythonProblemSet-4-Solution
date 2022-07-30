import random
from unittest import result
def main():
    level = get_level()
    score = scores(level)
    print("Score:",score)


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level == 1 or level == 2 or level == 3:
                break
            else:
                pass
        except:
            pass
    return level



def generate_integer(level):
    if level == 1:
        first_num = random.randint(0,9)
        second_num = random.randint(0,9)
    elif level == 2:
        first_num = random.randint(10,99)
        second_num = random.randint(10,99)
    else:
        first_num = random.randint(100,999)
        second_num = random.randint(100,999)
    return first_num,second_num

def count_tries(first_num,second_num):
    try_count = 1
    while try_count <= 3:
        result = input(f"{first_num} + {second_num} = ")
        try:
            result = int(result)
            if result == (first_num + second_num):
                return True
            else:
                print("EEE")
                try_count += 1
        except:
            print("EEE")
            try_count += 1

    print(f"{first_num} + {second_num} = {first_num + second_num}")


def scores(level):
    round = 1
    score = 0
    while round <= 10:
        num1, num2 = generate_integer(level)
        if count_tries(num1,num2) == True:
            score += 1
        round += 1
    return score


if __name__ == "__main__":
    main()