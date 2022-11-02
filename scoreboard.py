from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.refresh_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.hideturtle()
