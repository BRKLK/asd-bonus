def main():
    inp = input()
    n = len(inp)
    stack = [inp[0]]

    for i in range(1, n):
        if (len(stack) == 0) or (stack[-1] != inp[i]):
            stack.append(inp[i])
        else:
            stack.pop()

    return (stack == [])

if __name__ == "__main__":
    print(main())
