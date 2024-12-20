# 1. 列表 [1,2,3,4,5], 一条语句将此列表逆序输出。
# 给定列表
lst = [1, 2, 3, 4, 5]

# 使用切片操作逆序输出
reversed_lst = lst[::-1]
print(reversed_lst)


# 2. 给定一个列表 [1,2,3,4,4,4,,5,66,66,7,8], 要求去掉重复的元素并输出。
# 给定列表
lst = [1, 2, 3, 4, 4, 4, 5, 66, 66, 7, 8]

# 使用集合去重，然后转回列表
unique_lst = list(set(lst))

# 为了结果更直观，可以排序输出
unique_lst.sort()
print(unique_lst)


# 将列表 [1,3,5,9,12] 和列表 [2,1,4,5,7,8,11,10] 合并，并且变成由小到大的有序列表输出。
# 给定两个列表
lst1 = [1, 3, 5, 9, 12]
lst2 = [2, 1, 4, 5, 7, 8, 11, 10]

# 合并两个列表
merged_lst = lst1 + lst2

# 对合并后的列表排序
merged_lst.sort()
print(merged_lst)




