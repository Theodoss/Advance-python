def main():
    ways_to_climb(5)

def ways_to_climb(n):
    ways_to_climb_helper(n,n,[])

def ways_to_climb_helper(n,left_n,his_list):
    if left_n == 0:
        print(his_list)
    elif left_n > 0:
        for i in 1, 2:
            left_n = left_n - i
            his_list.append(i)
            ways_to_climb_helper(n, left_n, his_list)
            left_n = left_n + i
            his_list.pop()



if __name__ == '__main__':
    main()