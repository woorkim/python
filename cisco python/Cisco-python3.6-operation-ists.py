
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']
vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

print()
colors = ['red', 'green', 'orange']
copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

print()
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
print()

my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]
del my_list[:]
print(my_list)  # deletes the list content, outputs: []
print()

my_list = ["A", "B", 1, 2]
print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False
print()

#Q1
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]
print(list_3)
print()

#Q2
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2
print(list_3)
print()

#Q3
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2 
del list_1[0]
del list_2[:]
print(list_3)
print()

#Q4
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
del list_1[0]
del list_2[0]
print(list_3)
print()

#5 Insert in or not in instead of ??? so that the code outputs the expected result.
my_list = [1, 2, "in", True, "ABC"]
print(1 ??? my_list)  # outputs True
print("A" ??? my_list)  # outputs True
print(3 ??? my_list)  # outputs True
print(False ??? my_list)  # outputs False
