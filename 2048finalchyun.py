#Name: Kevin Chyun
#Date: 11/14/17
#Project Name: 32 Game
#Project Description: This game will operate like the game 2048. The goal of the game is to make one of the nine cells to become 32. As you make more cells become 32, it will keep tell you that you won the game. Once you reach that, you will win the game. And the game will offer you to have a choice of keep playing until one cell becomes 2048. However, you will lose the game if all the cells are filled and you made the move and you make an inappropriate move. Please enjoy the game. 
#sources:
#https://stackoverflow.com/questions/34845779/python-game-2048-out-of-list-index
#I adopted some parts from previous projects such as minesweeper for the board.
#Inspired from http://www.thetaranights.com/make-a-2048-game-in-python/ 
#Inspired from https://codereview.stackexchange.com/questions/91441/functional-programming-in-python-2048-merge-functions

import random #I imported the random function.

class Cell(object): #I created a class for the cells. 
	def __init__(self, cell_name): #This is similar to what I have 
		self.cell_name = cell_name #This will give the cell name. 
		self.cell_value = "    " #This will be the input for the value of the cell. 
		self.random_cell_number = 0
	
class State: #This is the class for the state of the game. 
	def __init__(self):
		self.high_score = 0
		self.curr_score = 0
		self.moved = False #This is for whether the cells moved or not.
		self.playing = True #This is for game operation.
		self.empty_cells = 9 #There are 9 empty cells when the game begins. 
		self.lost = False 
		self.board = [ #This is how the cell will look like. I got inspired by the minesweeper board that I have created before. 
			[Cell("A1"), Cell("B1"), Cell("C1")],
			[Cell("A2"), Cell("B2"), Cell("C2")],
			[Cell("A3"), Cell("B3"), Cell("C3")]
			]
		
		#These are the location of the board.
		self.A1 = self.board[0][0] 
		self.A2 = self.board[1][0]
		self.A3 = self.board[2][0]
		self.B1 = self.board[0][1]
		self.B2 = self.board[1][1]
		self.B3 = self.board[2][1]
		self.C1 = self.board[0][2]
		self.C2 = self.board[1][2]
		self.C3 = self.board[2][2]
	
	#The function below is to print in terminal area. 
	def adjust_length (self,value):
		length = len(value)
		if length == 4:
			return value
		elif length== 3:
			return value + " "
		elif length == 2:
			return " " + value + " "
		elif length == 1:
			return "  " + value + " "
		
	#The function below is to print in terminal area.
	def __str__(self):
		board =(" -------------------------------------- "+ "\n")
		for i in range(3):
			v1 = self.adjust_length(str(self.board[i][0].cell_value))
			v2 = self.adjust_length(str(self.board[i][1].cell_value))
			v3 = self.adjust_length(str(self.board[i][2].cell_value))
			
			board += (
					"|            |            |            |" + "\n" +
					"|    "+v1+"    |    "+v2+"    |    "+v3+"    |" + "\n" +
					"|            |            |            |" + "\n" +
					" -------------------------------------- " + "\n")
		
		board += "Your current score: " + str(self.curr_score) +".\n Your high score: " + str(self.high_score) + ".\n"
		return board
		
	#This function is to check whether there is an empty cell or not. 
	def check_empty_cell(self):
		self.empty_cells = 0
		for i in range(3):
			for j in range(3):
				self.board[i][j].random_cell_number = 0
				if self.board[i][j].cell_value == "    ":
					self.empty_cells = self.empty_cells + 1
					self.board[i][j].random_cell_number = self.empty_cells
					
		return self.empty_cells
	
	def generate_number(self): #This will generate a random number on the board after every move that is made. 
		if self.empty_cells != 0:
			two_or_four = 2*(random.randint(0,1)+1)
			random_cell = random.randint(0,self.empty_cells-1)+1
			for i in range(3):
				for j in range(3):
					if self.board[i][j].random_cell_number == random_cell:
						self.board[i][j].cell_value = two_or_four
	#State of the game. 
	def init_state(self):
		self.curr_score = 0 #The player will start with the score of 0.
		self.moved = False #The player did not make any movement at the start of the game.
		self.playing = True #The game will be operated.
		self.empty_cells = 9
		self.lost = False
		
		for i in range(3):
			for j in range(3):
				self.board[i][j].cell_value = "    "
		
		for i in range(2):
			self.check_empty_cell() #Operate function check_empty_cells
			self.generate_number() #Operate function generate_number
		
		return self
	#This is when the player won the game. 
	def check_win_state(self):
		for i in range(3):
			for j in range(3):
				if self.board[i][j].cell_value == 32:
					print("You win! You can continue playing. Or if you want to restart, you can press r. If you want to quit the game, press q.")
	
	#This is the function to check the losing state of the game. 
	def check_lose_state(self):
		places_to_move = 4 #There are total of 4 ways to move. You can either move up, down, left, and right.
		
		if self.B1.cell_value != (self.A1.cell_value and self.B2.cell_value and self.C1.cell_value):
			places_to_move = places_to_move - 1
		
		elif self.A2.cell_value != (self.A1.cell_value and self.B2.cell_value and self.A3.cell_value):
			places_to_move = places_to_move - 1
			
		elif self.C2.cell_value != (self.C1.cell_value and self.B2.cell_value and self.C3.cell_value):
			places_to_move = places_to_move - 1
			
		elif self.B3.cell_value != (self.A3.cell_value and self.B2.cell_value and self.C3.cell_value):
			places_to_move = places_to_move - 1
		
		#If the user cannot make any move anymore, the player will lose. Refer the movements to the if statements above. 
		if places_to_move == 0:
			self.lost = True

		if self.moved == False: #If the grids cannot be moved, then the user will lose the game. 
			self.lost = True
			
		print("No more places to move to. Game Over. Restarting. Your score was: " + str(self.curr_score) + ".") #This will be printed once the cells cannot be moved. 
	
	#This will be the helper function for the game to operate. It will be in charge of the movement of the game. 
	def helper(self, c1, c2, c3):
		if c1.cell_value == "    " :
			# Second Cell is Empty
			if c2.cell_value == "    " :
				if c3.cell_value != "    " :
					c1.cell_value = c3.cell_value
					c3.cell_value = "    "
					self.moved = True
			# This code is when second Cell is not Empty
			else :
				# This code is when the third Cell is not empty
				if c3.cell_value != "    " :
					# Third Cell is not empty and has same value as Second Cell
					if c3.cell_value == c2.cell_value :
						c1.cell_value = c2.cell_value * 2
						c2.cell_value = "    "
						c3.cell_value = "    "
						self.curr_score = self.curr_score + c1.cell_value
						self.moved = True
					# This code is when the third Cell is not empty but has different value as Second Cell
					else :
						c1.cell_value = c2.cell_value
						c2.cell_value = c3.cell_value
						c3.cell_value = "    "
						self.moved = True 

				# Third Cell is empty
				else :
					c1.cell_value = c2.cell_value
					c2.cell_value = "    "
					self.moved = True
					
		# First Cell is not Empty
		else :
			# Second Cell is not empty
			if c2.cell_value != "    " :
				# Third Cell is empty
				if c3.cell_value == "    " :
					# Third Cell is empty and First Cell and Second Cell have same values
					if c2.cell_value == c1.cell_value :
						c1.cell_value = c1.cell_value * 2
						c2.cell_value = "    "
						self.curr_score = self.curr_score + c1.cell_value
						self.moved = True
				# Third Cell is not empty
				else :
					# Third Cell is not empty and First Cell and Second Cell have same values
					if c2.cell_value == c1.cell_value :
						c1.cell_value = c1.cell_value * 2
						c2.cell_value = c3.cell_value
						c3.cell_value = "    "
						self.curr_score = self.curr_score + c1.cell_value
						self.moved = True
					 # Third Cell is not empty and First Cell and Second Cell have different values
					elif c2.cell_value != c1.cell_value :
						# Second Cell and Third Cell have same values
						if c3.cell_value == c2.cell_value :
							c2.cell_value = c2.cell_value * 2
							c3.cell_value = "    "
							self.curr_score = self.curr_score + c2.cell_value
							self.moved = True
			# Second Cell is empty
			else :
				# Third Cell is not empty
				if c3.cell_value != "    " :
					# Third Cell and First Cell have same values
					if c3.cell_value == c1.cell_value :
						c1.cell_value = c1.cell_value * 2
						c3.cell_value = "    "
						self.curr_score = self.curr_score + c1.cell_value
						self.moved = True
					# Third Cell and First Cell have different values
					else :
						c2.cell_value = c3.cell_value
						c3.cell_value = "    "
						self.moved = True
		#if the score I am getting is greater than the previous high score, then the high score will change to my current score.
		if (self.curr_score > self.high_score):
			self.high_score = self.curr_score
	
	#This function will make the cells to shift up. 
	def up(self):
		self.moved = False
		
		self.helper(self.A1,self.A2,self.A3) #This is with the help of the helper function. 
		self.helper(self.B1,self.B2,self.B3) #This is with the help of the helper function. 
		self.helper(self.C1,self.C2,self.C3) #This is with the help of the helper function. 
		
	#This will make the cells to shift down. 
	def down(self):
		self.moved = False
		
		self.helper(self.A3,self.A2,self.A1) #This is with the help of the helper function. 
		self.helper(self.B3,self.B2,self.B1) #This is with the help of the helper function. 
		self.helper(self.C3,self.C2,self.C1) #This is with the help of the helper function. 
	
	#This will make the cells to shift left. 	
	def left(self):
		self.moved = False
		
		self.helper(self.A1,self.B1,self.C1) #This is with the help of the helper function. 
		self.helper(self.A2,self.B2,self.C2) #This is with the help of the helper function. 
		self.helper(self.A3,self.B3,self.C3) #This is with the help of the helper function. 
	
	#This will make the cells to shift right.	
	def right(self):
		self.moved = False
		
		self.helper(self.C1,self.B1,self.A1) #This is with the help of the helper function. 
		self.helper(self.C2,self.B2,self.A2) #This is with the help of the helper function. 
		self.helper(self.C3,self.B3,self.A3) #This is with the help of the helper function. 
		
	#This function will allow the user to move the tiles. For instance, if the user types "up" or "w", then the user will be able to shift the cells up. 
	def exec_command(self):
		command = str(input("Enter a command: ")).lower() #This will print what command the user had inputted. 
		while True:
			if command == "help":
				print("Possible Commands:\n(up or w),\n(down or s),\n(left or a),\n(right or d),\n(restart or r),\n(quit or q).\n")
				break
			
			#This will make the user to be able to shift cells by typing these commands. 
			elif ((command == "up") or (command == "down") or (command == "left") or (command == "right") or
				  (command == "w") or (command == "s") or (command == "a") or (command == "d")):
			#If the user clicks "up" or "w", the grids will shift up.
				if ((command == "up") or (command == "w")):
					self.up()
			#If the user clicks "down" or "w", the grids will shift down.
				elif (command == "down") or (command == "s") :
					self.down()
			#If the user clicks "left" or "a", the grids will shift left.
				elif (command == "left") or (command == "a") :
					self.left()
			#If the user clicks "right" or "d", the grids will shift right. 
				elif (command == "right") or (command == "d") :
					self.right()
				#This will generate number after the move is made. 
				if self.check_empty_cell() != 0 and self.moved == True:
					self.generate_number()
				elif self.check_empty_cell() == 0:
					self.check_lose_state()
					
				self.check_win_state()
				print(self)
				break
			
			elif ((command == "restart") or (command == "r")):
				self.init_state()
				print("Restarting the game. Your score was: " + str(self.curr_score) + ".")
				print(self)
				break
			
			elif ((command == "quit") or (command == "q")):
				self.playing = False
				break
				
			else:
				command = str(input("Wrong Command. You can type in 'help' to view the possible commands.\nEnter a command: "))
		
#This will be the main function. This wil run the game. 
def main():
	st = State.init_state(State())
	print(st)
	print("Possible Commands:\n(up or w),\n(down or s),\n(left or a),\n(right or d),\n(restart or r),\n(quit or q).\nYou can type in 'help' to view the possible commands again.\n")
	while (st.playing == True):
		State.exec_command(st)
		if (st.lost == True):
			State.init_state(st)
		
	print("Your final high score is: " + str(st.high_score) + ". Thank you for playing.")
	
if __name__ == '__main__':
	main()
		
		
	
	
