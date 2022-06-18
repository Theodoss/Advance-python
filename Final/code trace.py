def code_tracing():
    sc = [1,2,3]
    if sc.pop() == 3.0:
        print('1',sc)
    else:
        print('2', sc)

    cs =['hi']
    mystery(sc,cs)
    print('3',sc,cs)

def mystery(cs,sc):
    if len(cs):
        print('5',sc)
    else:
        print('6', sc)
    cs = sc

code_tracing()