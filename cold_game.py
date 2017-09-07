import random


def print_intro():
    print('''
             ,-.____,-.
                  /   ..   \\
                 /_        _\\
                |'o'      'o'|
               / ____________ \\
             , ,'    `--'    '. .
            _| |              | |_
          /  ' '              ' '  \\
         (    `,',__________.','    )
          \_    ` ._______, '     _/
             |                  |
             |    ,-.    ,-.    |
              \      ).,(      /
               \___/    \___/
    ''')
    print("\nTo defeat the great Space Hippopotamus you have to win a cold hot warm game!\n")


def choose_random_number():
    first_numb = random.randint(1, 9)

    second_numb = random.randint(0, 9)
    while second_numb == first_numb:
        second_numb = random.randint(0, 9)

    third_numb = random.randint(0, 9)
    while third_numb == first_numb or third_numb == second_numb:
        third_numb = random.randint(0, 9)

    correct_number = [first_numb, second_numb, third_numb]
    return correct_number


def get_user_guess():
    user_guess = None
    while user_guess is None or len(str(user_guess)) != 3:
        try:
            user_guess = int(input())
        except ValueError:
            user_guess = None
    user_guess = str(user_guess)
    user_guess_list = [int(item) for item in user_guess]
    return user_guess_list


def compare_user_guess_with_correct_answer(user_guess, correct_answer):
    cold_warm_hot = []
    for i, item in enumerate(user_guess):
        if item in correct_answer:
            if user_guess[i] == correct_answer[i]:
                cold_warm_hot.append("Hot")
            else:
                cold_warm_hot.append("Warm")
    cold_warm_hot.sort()
    if not cold_warm_hot:
        cold_warm_hot.append("Cold")
    return cold_warm_hot


def check_win(cold_warm_hot):
    return cold_warm_hot == ['Hot'] * 3


def game():

    print_intro()
    guess_num = 1
    correct_answer = choose_random_number()

    while guess_num <= 10:
        print("Guess #" + str(guess_num) + ' : ', end='')
        user_guess = get_user_guess()
        guess_num += 1

        cold_warm_hot = compare_user_guess_with_correct_answer(user_guess, correct_answer)
        print(' '.join(cold_warm_hot))

        if check_win(cold_warm_hot):
            break

    return check_win(cold_warm_hot)


if __name__ == '__main__':
    game()
