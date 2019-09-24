# 切片操作示例
# 从http://www.python.org中提取域名
# url = input('Please enter the URL:')
# domain = url[11:-4]
# print("Domain name:" + domain)
# 更大的步长
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[8:-8:1]) # 切片包含起点到终点的所有元素
print(numbers[0:10:4]) # 步长为2时，从起点到终点每隔一个元素提取一个元素
print(numbers[3:6:3])  # 步长为3的，每隔两个元素提取一个元素,(不包含索引为6的数值)
print(numbers[::4])    # 每隔三个元素提取一个
print(numbers[8:3:-1]) # 步长为负数时，倒序输出
print(numbers[5::-2])  # 索引为5的前面的值，倒叙输出
print(numbers[:5:-2])  # 索引为5的后面的值，倒叙输出(步长为负数时，第一个索引必须比第二个索引的值大)
