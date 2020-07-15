queue_code = '''val_holder = [ ]
no_of_vals = input("How many values you want to enter\n")

for i in range(int(no_of_vals)):
    values = float(input('Enter your value'))
    val_holder.append(values)


print(f"Values before dqueue {val_holder}\n")
print(f'Value that you entered first {val_holder.pop(0)}\n')
print(f"Values after dqueue {val_holder}")
'''