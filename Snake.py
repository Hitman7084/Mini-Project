import tkinter as tk
import random

class Snake:
    def __init__(self, master):
        self.master = master
        master.title("Snake")

        # Set up the game canvas
        self.canvas = tk.Canvas(master, width=400, height=400, bg='black')
        self.canvas.pack()

        # Create the snake and food
        self.snake = [(200, 200), (190, 200), (180, 200)]
        self.food = self.create_food()

        # Set up the game loop
        self.direction = 'Right'
        self.game_over = False
        self.delay = 500
        self.score = 0
        self.label = tk.Label(master, text=f"Score: {self.score}")
        self.label.pack()

        # Bind arrow keys to change direction
        master.bind('<Up>', lambda event: self.change_direction('Up'))
        master.bind('<Down>', lambda event: self.change_direction('Down'))
        master.bind('<Left>', lambda event: self.change_direction('Left'))
        master.bind('<Right>', lambda event: self.change_direction('Right'))

        # Start the game loop
        self.game_loop()

    def create_food(self):
        # Create a new piece of food at a random location on the canvas
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        food = self.canvas.create_oval(x, y, x+20, y+20, fill='red')
        return food
    def draw_snake(self):
        self.square_size = 20
        self.canvas.delete('snake')

        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size,
                                            fill='white', tags='snake')
            else:
                self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size,
                                            fill='green', tags='snake')


    def move_snake(self):
        # Move the snake one step in the current direction
        head = self.snake[0]
        if self.direction == 'Up':
            new_head = (head[0], head[1]-20)
        elif self.direction == 'Down':
            new_head = (head[0], head[1]+20)
        elif self.direction == 'Left':
            new_head = (head[0]-20, head[1])
        elif self.direction == 'Right':
            new_head = (head[0]+20, head[1])
        self.snake.insert(0, new_head)
        self.canvas.delete(self.snake[-1])
        self.snake.pop()

    def check_collision(self):
        # Check for collision with the walls or the snake's body
        head = self.snake[0]
        if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
            self.game_over = True
        for segment in self.snake[1:]:
            if head == segment:
                self.game_over = True

    def check_food(self):
        # Check if the snake has eaten the food
        if self.snake[0] == self.canvas.coords(self.food):
            self.canvas.delete(self.food)
            self.food = self.create_food()
            self.score += 10
            self.label.config(text=f"Score: {self.score}")

    def change_direction(self, direction):
        # Change the direction of the snake
        if direction == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif direction == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif direction == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif direction == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def game_loop(self):
        # Main game loop
        if not self.game_over:
            self.draw_snake()
            self.move_snake()
            self.check_collision()
            self.check_food()
            if not self.game_over:
                self.master.after(self.delay, self.game_loop)
            else:
                self.canvas.create_text(200, 200, text="Game Over!", fill='white', font=('Helvetica', 30))

# Create the game window
root = tk.Tk()

# Start the game
snake = Snake(root)

# Run the game window
root.mainloop()