blocks = int(input("Enter the number of blocks: "))

height = 0
total_blocks = 0

while total_blocks + height < blocks:
    height += 1
    total_blocks += height

print("The height of the pyramid:", height)
