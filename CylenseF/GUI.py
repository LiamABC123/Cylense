import time
import tkinter as tk
import os
from Game import Game


class GUI:
    def __init__(self, game) -> None:
        self.game = game
        self.root = tk.Tk()

        # window size
        self.root.geometry("800x600")

        # title and logo
        self.root.title("Cylense")
        self.root.iconphoto(True, tk.PhotoImage(file=os.path.abspath("logo.png")))

        # make window unresizable
        self.root.resizable(False, False)

        # set background image
        self.bg_image = tk.PhotoImage(file=os.path.abspath("background.png"))
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # calculate position of the window
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = int((self.screen_width - 800) / 2)
        self.y = int((self.screen_height - 600) / 2)

        # set window position
        self.root.geometry("+{}+{}".format(self.x, self.y))
        self.root.protocol("WM_DELETE_WINDOW", game.set_game_state("game_over"))

        # set button position and size
        self.button_width = 142
        self.button_height = 62
        self.button_x = int((800 - self.button_width) / 1.99)
        self.button_y = int((600 - self.button_height) / 2.14)

        self.button_image_normal = tk.PhotoImage(  # hover image switching
            file=os.path.abspath("button_1.png")
        )
        self.button_image_hover = tk.PhotoImage(
            file=os.path.abspath("button_1_hover.png")
        )
        self.button_image_normal_2 = tk.PhotoImage(file=os.path.abspath("button_2.png"))
        self.button_image_hover_2 = tk.PhotoImage(
            file=os.path.abspath("button_2_hover.png")
        )
        self.button_image_normal_3 = tk.PhotoImage(file=os.path.abspath("button_3.png"))
        self.button_image_hover_3 = tk.PhotoImage(
            file=os.path.abspath("button_3_hover.png")
        )
        self.button_image_normal_4 = tk.PhotoImage(
            file=os.path.abspath("attack_button.png")
        )
        self.button_image_hover_4 = tk.PhotoImage(
            file=os.path.abspath("attack_button_hover.png")
        )
        self.button_image_normal_5 = tk.PhotoImage(
            file=os.path.abspath("place_button.png")
        )
        self.button_image_hover_5 = tk.PhotoImage(
            file=os.path.abspath("place_button_hover.png")
        )
        self.button_image_normal_6 = tk.PhotoImage(
            file=os.path.abspath("gamble_button.png")
        )
        self.button_image_hover_6 = tk.PhotoImage(
            file=os.path.abspath("gamble_button_hover.png")
        )
        self.button_image_normal_7 = tk.PhotoImage(
            file=os.path.abspath("draw_button.png")
        )
        self.button_image_hover_7 = tk.PhotoImage(
            file=os.path.abspath("draw_button_hover.png")
        )
        self.button_image_normal_8 = tk.PhotoImage(
            file=os.path.abspath("play_button.png")
        )
        self.button_image_hover_8 = tk.PhotoImage(
            file=os.path.abspath("play_button_hover.png")
        )
        self.button_image_normal_9 = tk.PhotoImage(
            file=os.path.abspath("exit_button.png")
        )
        self.button_image_hover_9 = tk.PhotoImage(
            file=os.path.abspath("exit_button_hover.png")
        )

        self.text_widget = tk.Frame(
            self.root, bg="black", highlightthickness=0, bd=0
        )  # text widget/frame properties

        self.text_widget = tk.Text(
            self.root,
            font=("Lemon Milk Pro Regular", 17),
            bg="#343541",
            fg="white",
            wrap="word",
            bd=0,
            highlightthickness=0,
        )

        self.button = tk.Button(  # button properties
            self.root,
            image=self.button_image_normal,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_2 = tk.Button(
            self.root,
            image=self.button_image_normal_2,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_3 = tk.Button(
            self.root,
            image=self.button_image_normal_3,
            width=self.button_width,
            height=self.button_height,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_4 = tk.Button(
            self.root,
            image=self.button_image_normal_4,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_5 = tk.Button(
            self.root,
            image=self.button_image_normal_5,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_6 = tk.Button(
            self.root,
            image=self.button_image_normal_6,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_7 = tk.Button(
            self.root,
            image=self.button_image_normal_7,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_8 = tk.Button(
            self.root,
            image=self.button_image_normal_8,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )
        self.button_9 = tk.Button(
            self.root,
            image=self.button_image_normal_9,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        self.button_x = int((800 - self.button_width) / 1.99)  # position change
        button_y = int((600 - self.button_height) / 2.14)
        # place the button on the window
        self.button.place(x=self.button_x, y=self.button_y, anchor="nw")

        self.button_2.place(
            x=self.button_x, y=button_y + self.button_height + 10, anchor="nw"
        )

        self.button_3.place(
            x=self.button_x, y=button_y + (2 * self.button_height) + 20, anchor="nw"
        )

        self.button.bind("<Enter>", self.switch_button_image)
        self.button.bind("<Leave>", self.switch_button_image_back)
        self.button.bind("<Button-1>", self.clear_gui_1)

        self.button_2.bind("<Enter>", self.switch_button_image_2)
        self.button_2.bind("<Leave>", self.switch_button_image_back_2)
        self.button_2.bind("<Button-1>", self.clear_gui_2)

        self.button_3.bind("<Enter>", self.switch_button_image_3)
        self.button_3.bind("<Leave>", self.switch_button_image_back_3)
        self.button_3.bind("<Button-1>", self.exit_gui)

        self.button_4.bind("<Enter>", self.switch_button_image_4)
        self.button_4.bind("<Leave>", self.switch_button_image_back_4)
        self.button_4.bind("<Button-1>", lambda event: self.game.playerAttack())

        self.button_5.bind("<Enter>", self.switch_button_image_5)
        self.button_5.bind("<Leave>", self.switch_button_image_back_5)
        self.button_5.bind("<Button-1>", lambda event: self.game.playerPlace())

        self.button_6.bind("<Enter>", self.switch_button_image_6)
        self.button_6.bind("<Leave>", self.switch_button_image_back_6)
        self.button_6.bind("<Button-1>", lambda event: self.game.playerGamble())

        self.button_7.bind("<Enter>", self.switch_button_image_7)
        self.button_7.bind("<Leave>", self.switch_button_image_back_7)
        self.button_7.bind("<Button-1>", lambda event: self.game.playerDraw())

    # define function to switch button image on mouse hover
    def switch_button_image_3(self, event):
        self.button_3.config(image=self.button_image_hover_3)

    def switch_button_image_back_3(self, event):
        self.button_3.config(image=self.button_image_normal_3)

    # define function to switch button image on mouse hover
    def switch_button_image_2(self, event):
        self.button_2.config(image=self.button_image_hover_2)

    def switch_button_image_back_2(self, event):
        self.button_2.config(image=self.button_image_normal_2)

    # define function to switch button image on mouse hover
    def switch_button_image(self, event):
        self.button.config(image=self.button_image_hover)

    def switch_button_image_back(self, event):
        self.button.config(image=self.button_image_normal)

    # define function to switch button image on mouse hover
    def switch_button_image_5(self, event):
        self.button_5.config(image=self.button_image_hover_5)

    def switch_button_image_back_5(self, event):
        self.button_5.config(image=self.button_image_normal_5)

    # define function to switch button image on mouse hover
    def switch_button_image_4(self, event):
        self.button_4.config(image=self.button_image_hover_4)

    def switch_button_image_back_4(self, event):
        self.button_4.config(image=self.button_image_normal_4)

    # define function to switch button image on mouse hover
    def switch_button_image_6(self, event):
        self.button_6.config(image=self.button_image_hover_6)

    def switch_button_image_back_6(self, event):
        self.button_6.config(image=self.button_image_normal_6)

        # define function to switch button image on mouse hover

    def switch_button_image_7(self, event):
        self.button_7.config(image=self.button_image_hover_7)

    def switch_button_image_back_7(self, event):
        self.button_7.config(image=self.button_image_normal_7)

    def start_game_loop(self):
        # run the GUI
        self.root.mainloop()

    def clear_gui_1(self, event):  # action after clicking "play"
        # destroy all buttons
        self.button.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        # change background image
        bg_image = tk.PhotoImage(file="background_ingame.png")
        self.bg_label.config(image=bg_image)
        self.bg_label.image = bg_image

        # reposition the button and place it on the window
        self.button_4.place(x=138, y=469, anchor="nw")

        # reposition the button and place it on the window
        self.button_5.place(x=278, y=469, anchor="nw")

        # reposition the button and place it on the window
        self.button_6.place(x=418, y=469, anchor="nw")

        # reposition the button and place it on the window
        self.button_7.place(x=558, y=469, anchor="nw")
        self.text_widget.pack()
        self.text_widget.place(
            relx=0.5, rely=0.3915, relwidth=0.85, relheight=0.57, anchor="center"
        )
        is_my_turn = self.game.startGame()
        if is_my_turn:
            self.append_text("You may start, as you've drawn a faster hand!")
        else:
            self.append_text("Your opponent starts, as he's drawn a faster hand!")
            self.game.start_opponent_turn()

    def clear_gui_2(self, event):
        self.button.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        bg_image = tk.PhotoImage(file="background_info.png")
        self.bg_label.config(image=bg_image)
        self.bg_label.image = bg_image
        self.text_widget.pack()
        self.text_widget.place(
            relx=0.5, rely=0.3915, relwidth=0.85, relheight=0.57, anchor="center"
        )

    # define function to exit the GUI
    def exit_gui(self, event):
        time.sleep(1)
        self.root.destroy()

    def append_text(self, text):
        self.text_widget.insert(tk.END, text + "\n")
        self.text_widget.see(tk.END)


game = Game()
print(game)
gui = GUI(game)
game.gui = gui
gui.start_game_loop()
