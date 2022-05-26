"""
File: priority_queue_list.py
Name:
----------------------------------
This program shows how to build a priority queue by
using Python list. We will be discussing 3 different
conditions while appending:
1) Prepend
2) Append
3) Append in between
"""

# This constant controls when to stop the user input
EXIT = ''


def main():
    priority_queue = []

    print('--------------------------------')
    # TODO:
    while True:
        name = input('Patient: ')
        if name == 'EXIT':
            break
        priority = int(input('Priority: '))
        data = (name, priority)
        if len(priority_queue) == 0:
            # First data
            priority_queue.append(data)
        else:
            # Prepend
            if priority < priority_queue[0][1]:
                priority_queue.insert(0,data)
            # Append
            if priority >= priority_queue[len(priority_queue)-1][1]:
                priority_queue.append(data)
            # In Between
            else:
                for i in range(len(priority_queue)-1):
                    # if priority < priority_queue[i][1]:
                    #     priority_queue.insert(i+1,data)
                    if priority_queue[i][1] <= priority < priority_queue[i+1][1]:
                        priority_queue.insert(i+1,data)
                        # break


    print('--------------------------------')

    print(priority_queue)


if __name__ == '__main__':
    main()
