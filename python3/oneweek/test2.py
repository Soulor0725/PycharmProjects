#整数序列求和。用户输入一个正整数 N，计算从 1 到 N(包含 1 和 N)相加之后的结果。

n = input("请输入整数N:")

sum = 0
for i in range(int(n)):
	sum+=i;
print("1到N求和结果：",sum)