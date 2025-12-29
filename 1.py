n = int(input())
inp = input()
stack = [inp[0]]

for i in range(1, n):
	if (len(stack) == 0) or (stack[-1] != inp[i]):
		stack.append(inp[i])
	else:
		stack.pop()

print(1 if stack == [] else 0)
