"""
File: class_reviews.py
Name: stanCode example answer
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = '-1'


def main():
    """
    This program will ask user to input the class number and score, and compute the
    maximum, minimum, and average among all the scores.
    """
    count_001 = 0
    count_101 = 0
    sum_001 = 0
    sum_101 = 0
    max_001 = -float('inf')
    max_101 = -float('inf')
    min_001 = float('inf')
    min_101 = float('inf')

    class_number = input('Which class? ').upper()
    if class_number == EXIT:
        print('No class scores were entered')
    else:
        while True:
            if class_number == 'SC001':
                score = int(input('Score: '))
                if score > max_001:
                    max_001 = score
                if score < min_001:
                    min_001 = score
                sum_001 += score
                count_001 += 1
            elif class_number == 'SC101':
                score = int(input('Score: '))
                if score > max_101:
                    max_101 = score
                if score < min_101:
                    min_101 = score
                sum_101 += score
                count_101 += 1

            class_number = input('Which class? ').upper()
            if class_number == EXIT:
                break

        print('=============SC001=============')
        if count_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(sum_001 / count_001))
        print('=============SC101=============')
        if count_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(sum_101 / count_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
