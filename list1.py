total = 0
count = 0

list = [1, 2, None, 3, 'sad', 4, 'null', '', 5.5,]
# list = [None, 'sad', 'null', '']

for i in list:
    if type(i) == int or type(i) == float:
        print('i is a number: ', i, '   type: ', type(i))
        total = total + i
        count = count + 1
    else:
        print('i is not numeric: ', i, '   type: ', type(i))

print('List: ', list)

if count > 0:
    average = total/count
    print('count: ', count, '   average: ', average, '   total', total)
else:
    print ('no numeric values: ', count, '   List:', list)