
def cover(board, side=0, top=0, left=0, lab=1):
	side = side if side else len(board)
	sub_side = side//2

	offset = (0, -1), (side-1, 0)

	#将大的棋盘拆成4个子棋盘,每个棋盘都有一个缺角
	for out_y, in_y in offset:
		for out_x, in_x in offset:
			if not board[top+out_y][left+out_x]:
				board[top+sub_side+in_y][left+sub_side+in_x] = lab

	lab += 1

	#递归处理4个子棋盘
	if sub_side > 1:
		for dy in (0, sub_side):
			for dx in (0, sub_side):
				lab = cover(board, sub_side, top+dy, left+dx, lab)
	return lab
	
if __name__ == '__main__':
	LEN = 8
	board = [[0]*LEN for _ in range(LEN)]
	board[0][0] = -1
	cover(board)
	for row in board:
		print("%4d"*LEN%(tuple(row)))