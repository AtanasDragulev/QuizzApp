from tkinter import *
from tkinter import messagebox
from engine import Engine
import settings

THEME_COLOR = "royalblue"


class Settings:

    def __init__(self):
        self.settings = Tk()
        self.settings.title("Settings")
        self.settings.config(padx=20, pady=20)
        self.label = Label(self.settings, width=40, text="Change game settings")
        self.label.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

        self.label_category = Label(self.settings, text="Category")
        self.label_category.grid(row=1, column=0)
        self.category = Listbox(self.settings, width=30, exportselection=False)
        for cat in range(9, 33):
            self.category.insert(cat, settings.TRIVIA_CATEGORIES[cat])
        self.category.selection_set(settings.CATEGORY - 9)
        print(settings.CATEGORY)
        self.category.grid(row=2, column=0, rowspan=4, padx=10)

        self.label_amount = Label(self.settings, width=16, text="How many questions")
        self.label_amount.grid(row=1, column=2, sticky="ew")
        self.amount = Entry(self.settings, width=10)
        self.amount.insert(0, settings.QUESTIONS)
        self.amount.grid(row=2, column=2, sticky="ew")

        self.label_difficulty = Label(self.settings, text="  Question \n difficulty")
        self.label_difficulty.grid(row=3, column=2)
        self.difficulty = Listbox(self.settings, height=3, exportselection=False)
        self.difficulty.insert("end", *["easy", "medium", "hard"])
        self.difficulty.select_set(settings.DIFFICULTY)
        self.difficulty.grid(row=4, column=2)

        self.btn_save = Button(self.settings, text="SAVE", command=self.btn_save)
        self.btn_save.grid(row=6, column=0, columnspan=3, sticky="ew", pady=15)

        self.settings.mainloop()

    def btn_save(self):
        questions = self.amount.get()
        if len(questions) == 0:
            questions = 10
        difficulty = self.difficulty.curselection()[0]
        category = self.category.curselection()[0] + 9
        settings.save_settings(questions, difficulty, category)
        messagebox.showinfo(message="Please restart application")
        self.settings.destroy()


def change_settings():
    Settings()


class Interface:

    def __init__(self, quiz_engine: Engine):

        self.quiz = quiz_engine
        self.options = []
        self.answer = ""
        self.window = Tk()
        self.window.title("Just Another Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label()
        self.score_label.config(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16))
        self.score_label.grid(row=0, column=3, sticky="se")

        self.canvas = Canvas(width=600, height=300, bg="white")
        background_img = PhotoImage(file="./images/background.png")
        self.background = self.canvas.create_image(40, 40, image=background_img)
        self.q_text = self.canvas.create_text(300, 145,
                                              width=400,
                                              text="question",
                                              font=("Arial", 20, "italic"),
                                              justify="center")
        self.canvas.grid(row=1, column=0, columnspan=4, pady=40)

        self.btn_settings = Button(width=15, text="Settings", command=change_settings)
        self.btn_settings.grid(row=0, column=0, sticky="w")
        self.btn_one = Button(width=35, height=5, wraplength=160, command=lambda: self.check_answer(0))
        self.btn_one.grid(row=2, column=0, columnspan=2, sticky="w")
        self.btn_two = Button(width=35, height=5, wraplength=160, command=lambda: self.check_answer(1))
        self.btn_two.grid(row=2, column=3, columnspan=2, sticky="w")
        self.btn_three = Button(width=35, height=5, wraplength=160, command=lambda: self.check_answer(2))
        self.btn_three.grid(row=4, column=0, pady=30, columnspan=2, sticky="w")
        self.btn_four = Button(width=35, height=5, wraplength=160, command=lambda: self.check_answer(3))
        self.btn_four.grid(row=4, column=3, pady=30, columnspan=2, sticky="w")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Checks if there are questions left and loads new one"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_data = self.quiz.next_question()
            question_text = question_data[0]
            self.options = question_data[1]
            self.answer = question_data[2]
            self.canvas.itemconfig(self.q_text, text=question_text)
            self.btn_one.config(text=self.options[0], state="normal")
            self.btn_two.config(text=self.options[1], state="normal")
            self.btn_three.config(text=self.options[2], state="normal")
            self.btn_four.config(text=self.options[3], state="normal")
        else:
            end = "You've completed the quiz\n" \
                  f"Your guessed: {self.quiz.score}/{len(self.quiz.question_list)}"
            self.canvas.itemconfig(self.q_text, text=end)

    def give_feedback(self, is_right):
        """Changes the background green/red and refreshes score"""
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def check_answer(self, button):
        """Locks the buttons and sends the answer to be checked"""
        self.btn_one.config(state="disabled")
        self.btn_two.config(state="disabled")
        self.btn_three.config(state="disabled")
        self.btn_four.config(state="disabled")
        self.give_feedback(self.quiz.check_answer(button))
