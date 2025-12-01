input1 = input("Your Input: ")

width = 17
padding = width - len(input1)

left = ">" * (padding // 2 + padding % 2)
right = "<" * (padding // 2)

print(f"{left}{input1}{right}|")