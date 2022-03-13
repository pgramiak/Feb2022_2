#
# sort1.py
#
#  list = [4, 20, 7, 101, 13, 3] => [3, 4, 7, 13, 20,,101]
#
unsorted_list = [15, 20, 7, 101, 13, 3, 4]
sorted_list = []

while unsorted_list:
    minimum = unsorted_list[0]
    for item in unsorted_list:
        print('MINIMUM: ', minimum, 'ITEM: ', item)
        if item < minimum:
            minimum = item
            print('===>  MINIMUM: ', minimum, 'ITEM: ', item)
    sorted_list.append(minimum)
    print('       Updated Sorted List: ', sorted_list)
    unsorted_list.remove(minimum)

print(sorted_list)