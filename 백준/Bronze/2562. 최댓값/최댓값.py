num_list = [int(input())for i in range(9)]
max = max(num_list)
for i in range(9):
    if num_list[i] == max:
        max_index = i+1
print(max)
print(max_index)