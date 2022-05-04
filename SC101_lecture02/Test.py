# for i in (-1,0,1):
#     for j in (-1,0,1):
#         print(f'x+{i}, y-{j}')
#
# print(f'------------------------')
# for i in (-1,2,1):
#     for j in ((-1,2,1)):
#         print(f'x+{i}, y-{j}')
#
# print(f'------------------------')
# for i in (-1,0):
#     print(i)
# print(f'------------------------')
# for i in (-1,2):
#     print(i)

class test(object):
    def __init__(self,num):
        self.d = {}
        self.num = num
        for i in range(num):
            self.d['x' + str(i)] = i
    def run(self):
        for i in range(self.num):
            a = self.d['x' + str(i)]
            print(a)

asd = test(10)
asd.run()

# d= {}
# num = 10
# for i in range(num):
#     d['x'+str(i)] =i
# print(d.keys())
# print(d['x0'])
#
# for i in range(num):
#     print(d['x'+str(i)])
#
# print(d['x3'])