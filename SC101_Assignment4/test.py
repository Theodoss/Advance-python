# import re
# #fun2
# name_data = {'John': {{'1940': '690', '1950': '118', '1960': '61', '1970': '754', '1980': '600', '1990': '8', '2000': '26', '2010': '121'}}
# with open("../SC101_Assignment4/data/full/baby-1900.txt", 'r') as f:
#     name_data = None
#     year = None
#     if name_data is None:
#         name_data = {}
#     for line in f.readlines():
#         line = line.strip()
#         line = line.replace(' ', '')
#         line = line.split(",")
#         for i in range(len(line)):
#             if len(line) == 1:
#                 year = line[0]
#             else:
#                 # if name_data is None:
#                 name_data[line[1]] = {year: line[0]}
#                 name_data[line[2]] = {year: line[0]}
#     print(name_data)
#     print(name_data['John'])
#     year = '1900'
#     if '1920' not in name_data['John']:
#         print("xxxx")
#     if year in name_data['John']:
#         print(name_data['John'][str(1900)])
#
#     list = ['1900','1910','1920','1930']
#     print(list[1])

#fun1
    # target = 'jo'
    # for key in name_data:
    #     if target.lower() in key.lower():
    #         print(key)

#fun3
num = 0
for i in range(10):
    print(num)
    if num < 3:
        num +=1
    else:
        num = 0