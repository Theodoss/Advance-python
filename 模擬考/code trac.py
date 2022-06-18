def code_tracing():
    a = [10]
    b = 101
    c = {123:456, 789:101}

    if a[0]:
        print(b+c[123])
    else:
        print('false')

    print(bool(a))
    mystery(b, a, a[0], c)

def mystery(b,a_0, a, c):
    b +=1
    a_0[0] +=1
    a -= 1
    c[123] = 101

if __name__ =='__main__':
    code_tracing()