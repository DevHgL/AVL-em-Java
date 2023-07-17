import tkinter as tk
import random

# Dimensões da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Tamanho do bloco e quantidade de blocos na tela
BLOCK_SIZE = 20
BLOCK_COUNT_X = SCREEN_WIDTH // BLOCK_SIZE
BLOCK_COUNT_Y = SCREEN_HEIGHT // BLOCK_SIZE

# Direções do movimento da cobra
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.canvas.pack()

        self.snake = Snake()
        self.food = Food()

        self.score = 0
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack()

        self.game_over_text = None
        self.retry_text = None

        self.master.bind("<KeyPress>", self.on_key_press)
        self.set_fps(12)  # Definindo o framerate inicial

        self.update()

    def on_key_press(self, event):
        if self.snake.is_alive:
            if event.keysym == "Up":
                self.snake.change_direction(UP)
            elif event.keysym == "Down":
                self.snake.change_direction(DOWN)
            elif event.keysym == "Left":
                self.snake.change_direction(LEFT)
            elif event.keysym == "Right":
                self.snake.change_direction(RIGHT)
        else:
            if event.keysym == "space":
                self.restart_game()

    def update(self):
        if self.snake.is_alive:
            self.snake.move()
            self.snake.check_collision()

            if self.snake.check_food_collision(self.food):
                self.snake.grow()
                self.food.move()
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")

            self.draw()
        else:
            self.show_game_over()

        self.master.after(self.delay, self.update)

    def draw(self):
        self.canvas.delete("all")

        for position in self.snake.positions[1:]:
            x = position[0] * BLOCK_SIZE
            y = position[1] * BLOCK_SIZE
            self.canvas.create_rectangle(
                x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill="green"
            )

        head_x, head_y = self.snake.positions[0]
        head_x_px = head_x * BLOCK_SIZE
        head_y_px = head_y * BLOCK_SIZE
        self.canvas.create_rectangle(
            head_x_px, head_y_px, head_x_px + BLOCK_SIZE, head_y_px + BLOCK_SIZE, fill="black"
        )

        x = self.food.position[0] * BLOCK_SIZE
        y = self.food.position[1] * BLOCK_SIZE
        self.canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill="red")

    def show_game_over(self):
        if not self.game_over_text:
            self.game_over_text = self.canvas.create_text(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 20,
                text="GAME OVER",
                font=("Helvetica", 24),
                fill="black",
            )

        if not self.retry_text:
            self.retry_text = self.canvas.create_text(
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 20,
                text="Press SPACE to retry",
                font=("Helvetica", 16),
                fill="black",
            )

    def restart_game(self):
        self.snake = Snake()
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.delete("all")
        self.canvas.delete(self.game_over_text)
        self.canvas.delete(self.retry_text)
        self.game_over_text = None
        self.retry_text = None

    def set_fps(self, fps):
        self.fps = fps
        self.delay = int(1000 / self.fps)


class Snake:
    def __init__(self):
        self.positions = [(BLOCK_COUNT_X // 2, BLOCK_COUNT_Y // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.is_alive = True

    def move(self):
        head_x, head_y = self.positions[0]

        if self.direction == UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == LEFT:
            new_head = (head_x - 1, head_y)
        elif self.direction == RIGHT:
            new_head = (head_x + 1, head_y)

        self.positions.insert(0, new_head)
        self.positions = self.positions[:-1]

    def change_direction(self, direction):
        if self.direction == UP and direction != DOWN:
            self.direction = direction
        elif self.direction == DOWN and direction != UP:
            self.direction = direction
        elif self.direction == LEFT and direction != RIGHT:
            self.direction = direction
        elif self.direction == RIGHT and direction != LEFT:
            self.direction = direction

    def check_collision(self):
        head = self.positions[0]
        if (
            head[0] < 0
            or head[0] >= BLOCK_COUNT_X
            or head[1] < 0
            or head[1] >= BLOCK_COUNT_Y
        ):
            self.is_alive = False
        elif len(self.positions) > len(set(self.positions)):
            self.is_alive = False

    def check_food_collision(self, food):
        if self.positions[0] == food.position:
            return True
        return False

    def grow(self):
        self.positions.append(self.positions[-1])


class Food:
    def __init__(self):
        self.position = (
            random.randint(0, BLOCK_COUNT_X - 1),
            random.randint(0, BLOCK_COUNT_Y - 1),
        )

    def move(self):
        self.position = (
            random.randint(0, BLOCK_COUNT_X - 1),
            random.randint(0, BLOCK_COUNT_Y - 1),
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
