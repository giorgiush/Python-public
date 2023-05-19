import tkinter
from quiz_brain import QuizBrain

class GUI:

    def __init__(self, quizz_brain: QuizBrain):

        self.quiz = quizz_brain
        

        self.window = tkinter.Tk(screenName="QUIZ")
        self.window.minsize(width=400, height=500)
        self.window.config(padx=20, pady=10, bg="#375362")

        self.score = tkinter.Label(text=f"Score: {self.quiz.score}", font=20, bg="#375362", fg="white")
        self.score.grid(row=0, column=1, padx=10, pady=10)

        self.label = tkinter.Label(width=50, height=20, bg="white", wraplength=300)
        self.label.grid(row=1, column=0, columnspan=2)

        true_img = tkinter.PhotoImage(file="./day_34_Quiz_GUI/images/true.png")
        self.true = tkinter.Button(image=true_img, bg="#375362", highlightthickness=0, command = self.true_answer)
        self.true.grid(row=2, column=1)

        false_img = tkinter.PhotoImage(file="./day_34_Quiz_GUI/images/false.png")
        self.false = tkinter.Button(image=false_img, bg="#375362", highlightthickness=0, command = self.false_answer)
        self.false.grid(row=2, column=0)

        self.get_next_question()
  
        

        self.window.mainloop()


    def get_next_question(self):
        self.label.config(text=self.quiz.next_question())

    def true_answer(self):
        correct = self.quiz.check_answer("True")
        self.feedback(correct)

        

    def false_answer(self):
        correct = self.quiz.check_answer("False")
        self.feedback(correct)

        
    def feedback(self, correct):
        if correct:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.label.config(bg="green")
            self.window.after(200, self.color_white)
        else:
            self.label.config(bg="red")
            self.window.after(200, self.color_white)            
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.label.config(text=f"Final score: {self.quiz.score}/10")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def color_white(self):
        self.label.config(bg="white")