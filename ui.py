from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        correct_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=correct_img, highlightthickness=0, command=self.true_clicked)
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_clicked)

        self.score = 0
        self.score_board = Label(text=f"Score: 0", font=("Arial", "12"), bg=THEME_COLOR, fg="white")

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.config(highlightthickness=0, bg="white")

        self.correct_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.score_board.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The quiz is over")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_clicked(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_clicked(self) -> bool:
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)


