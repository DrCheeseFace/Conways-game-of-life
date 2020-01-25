import tkinter,main,time	


#deletes all objects on screen and redraws the grid lines
def delete_all_objects():
	
	canvas.delete('all')

	# draw grid lines	
	for i in range(cells):
		canvas.create_line(i*(canvas_width/cells),0,i*(canvas_width/cells),canvas_width,i*(canvas_width/cells),0)
		canvas.create_line(0,i*(canvas_width/cells),canvas_width,i*(canvas_width/cells),0,i*(canvas_width/cells))



window = tkinter.Tk()
window.title('Conways Game of Life')

canvas_width=800
canvas = tkinter.Canvas(window,width = canvas_width,height = canvas_width)
canvas.pack()


#number of cells per side
cells=100

#loop to draw alive cells 
board=main.initialize(cells)
	




#checking every cell and drawing alive or dead cell
while True:
	delete_all_objects()
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
