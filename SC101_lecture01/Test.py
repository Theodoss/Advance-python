ab_v = 10
cd_v = 20
ef_v = 30
gh_v = 40

ab = 100
cd = 200
ef = 300
gh = 400

list = [ab, cd, ef, gh]

for i in range(len(list)):
    locals()[str(i)+'_v'] = list[i]
    print(locals()[str(i)]+'_v')


    # for j in list:
    #     i = i_vx
    #     print (i, j)

# number1 = 1
# number2 = 2
# number3 = 3
# number4 = 4
# number5 = 5
# number6 = 6
# number7 = 7
# number8 = 8
# number9 = 9
# number10 = 10
#
# for i in range(1,10):
#     locals()['number'+str(i)] = i
#     show =locals()['number' + str(i)]
#     print(show)
#     print('Print In Once: ', locals()['number'+str(i)])