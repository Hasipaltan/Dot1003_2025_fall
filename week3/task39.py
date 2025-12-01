height = int(input(">Spruce height: "))

print(">")

for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(f">{spaces}{stars}")

trunk_spaces = " " * (height - 1)
print(f">{trunk_spaces}*")