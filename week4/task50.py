input1 = input("Please enter string: ")
where = input("Please enter search item: ")

where = input1.find(where)

if where != -1:
    print(f"found it at {where}")
else:
    print("not found")