import tkinter,main,time	


#redraws the grid lines
def draw_grid(canvas_width,cells): 
	# draw grid lines	
	for i in range(cells):
		canvas.create_line(i*(canvas_width/cells),0,i*(canvas_width/cells),canvas_width,i*(canvas_width/cells),0)
		canvas.create_line(0,i*(canvas_width/cells),canvas_width,i*(canvas_width/cells),0,i*(canvas_width/cells))

def place_cell(event):
	x = (event.x - (event.x % (canvas_width/cells)))/(canvas_width/cells)
	y = (event.y - (event.y % (canvas_width/cells)))/(canvas_width/cells)	
	if board[int(x)][int(y)]!=1:		
		canvas.create_rectangle(x*(canvas_width/cells),
		y*(canvas_width/cells),
		x*(canvas_width/cells)+canvas_width/cells,
		y*(canvas_width/cells)+canvas_width/cells,
		fill='black')
		board[int(x)][int(y)] = 1	
	print(x,y)



def delete_cell(event):
	x = (event.x - (event.x % (canvas_width/cells)))/(canvas_width/cells)
	y = (event.y - (event.y % (canvas_width/cells)))/(canvas_width/cells)
	if board[int(x)][int(y)]!=0:
		canvas.create_rectangle(x*(canvas_width/cells),
		y*(canvas_width/cells),
		x*(canvas_width/cells)+canvas_width/cells,
		y*(canvas_width/cells)+canvas_width/cells,
		fill='white')

		board[int(x)][int(y)] = 0 	
	print(x,y)

def play(event):
	global quit
	quit = True


window = tkinter.Tk()
window.title('Conways Game of Life')

canvas_width = 800
canvas = tkinter.Canvas(window,width = canvas_width,height = canvas_width)
canvas.pack()


#number of cells per side
cells = 100 

#loop to draw alive cells
global board
board = main.makeboard(cells) 
canvas.bind("<B1-Motion>",place_cell) #accounts for both motion and clicks 
canvas.bind('<Button-1>',place_cell)
canvas.bind("<B2-Motion>",delete_cell)  
canvas.bind('<Button-2>',delete_cell)
window.bind('<space>',play)

draw_grid(canvas_width,cells)


print(board)
while True:     #pause loop at the begginging 
	window.update()
	if quit==True:
		break



while True:
	canvas.delete('all')	
	draw_grid(canvas_width,cells)
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				canvas.create_rectangle(i*(canvas_width/cells),
				j*(canvas_width/cells),
				i*(canvas_width/cells)+canvas_width/cells,
				j*(canvas_width/cells)+canvas_width/cells,
				fill='black')

	window.update()
	board=main.live_or_die(board,cells)


window.mainloop()
