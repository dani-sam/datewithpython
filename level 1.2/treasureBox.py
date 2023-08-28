row1 = ["⬛️","⬛️","⬛️"]
row2 = ["⬛️","⬛️","⬛️"]
row3 = ["⬛️","⬛️","⬛️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input('where do u want to put the treasure? ')
col_pos = int(position[0]) - int(1)
row_pos = int(position[1]) - int(1)
map[row_pos][col_pos] = "X" 
print(f"{row1}\n{row2}\n{row3}")
