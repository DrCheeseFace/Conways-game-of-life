#conway's game of life  
#Tharun Tilakumara 2019/1/19 


import random,time

#functions

def live_or_die(board,side_length):   #create temp_board return temp_board
	temp_board=[[0 for i in range(side_length)]for j in range(side_length)]
	
	for i in range(side_length):
		for j in range(side_length):
			alive_cells=0
			if i !=0: #to avoid looping back around the list with i-1 at index 0	
				try:
					alive_cells+= board[i-1][j]
				except:
					pass
				try:
					alive_cells+= board[i-1][j-1]
				except:
					pass
				try:
					 alive_cells+=board[i-1][j+1]
				except:
					pass
			
			try:
				alive_cells+=board[i][j+1]
			except:
				pass
			try:
				alive_cells+=board[i][j-1]
			except:
				pass
			try:
				alive_cells+=board[i+1][j+1]
			except:
				pass
			try:
				alive_cells+=board[i+1][j]
			except:
				pass
			try:
				alive_cells+=board[i+1][j-1]
			except:
				pass
			
			if board[i][j]==1:
				if alive_cells<2:
					temp_board[i][j]=0
				elif alive_cells>3:
					temp_board[i][j]=0
				else:
					temp_board[i][j]=1
			else:
				if alive_cells==3:
					temp_board[i][j]=1
				
	return temp_board
	

def print_board(board):
	for i in board:
		print(i)

	print()





#initialize game board
def initialize(side_length):

	#create game board
	board=[[random.randint(0,1) for i in range(side_length)]for j in range(side_length)] 
	return board
	#test board
#	board=[[0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,1,1,1,0,0,0,0],
#	       [0,0,0,1,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0],
#	       [0,0,0,0,0,0,0,0,0,0]]

	#print_board(board)
	
#	while True:
#		board=live_or_die(board,side_length)
#		print_board(board)
#		time.sleep(2)




