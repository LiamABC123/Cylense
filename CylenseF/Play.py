import time
import tkinter as tk


def create_gui():
    root = tk.Tk()

    # window size
    root.geometry("800x600")

    # title and logo
    root.title("Cylense")
    root.iconphoto(True, tk.PhotoImage(file="logo.png"))

    # make window unresizable
    root.resizable(False, False)

    # set background image
    bg_image = tk.PhotoImage(file="C:/Users/ex0ar/Desktop/CylenseF/background.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # calculate position of the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - 800) / 2)
    y = int((screen_height - 600) / 2)

    # set window position
    root.geometry("+{}+{}".format(x, y))

    # define button properties
    button_width = 142
    button_height = 62
    button_x = int(
        (800 - button_width) / 1.99
    )  # change this value to move the button left or right              higher = left
    button_y = int(
        (600 - button_height) / 2.14
    )  # change this value to move the button up or down                  higher = up

    # create photo objects for the button images
    button_image_normal = tk.PhotoImage(file="button_1.png")
    button_image_hover = tk.PhotoImage(file="button_1_hover.png")

    # create a button with the normal image
    button = tk.Button(
        root,
        image=button_image_normal,
        width=button_width,
        height=button_height,
        bd=0,
        relief="sunken",
        highlightthickness=0,
        activebackground="white",
    )

    # define function to switch button image on mouse hover
    def switch_button_image(event):
        button.config(image=button_image_hover)

    def switch_button_image_back(event):
        button.config(image=button_image_normal)

    def clear_gui_1(event):  # action after clicking "play"
        # destroy all buttons
        button.destroy()
        button_2.destroy()
        button_3.destroy()
        # change background image
        bg_image = tk.PhotoImage(file="background_ingame.png")
        bg_label.config(image=bg_image)
        bg_label.image = bg_image
        # create photo objects for the button images
        button_image_normal_4 = tk.PhotoImage(file="attack_button.png")
        button_image_hover_4 = tk.PhotoImage(file="attack_button_hover.png")

        # create a button with the normal image and resize it
        button_4 = tk.Button(
            root,
            image=button_image_normal_4,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # reposition the button and place it on the window
        button_4.place(x=138, y=469, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_4(event):
            button_4.config(image=button_image_hover_4)

        def switch_button_image_back_4(event):
            button_4.config(image=button_image_normal_4)

        # bind the button hover events to switch_button_image function
        button_4.bind("<Enter>", switch_button_image_4)
        button_4.bind("<Leave>", switch_button_image_back_4)

        button_image_normal_5 = tk.PhotoImage(file="place_button.png")
        button_image_hover_5 = tk.PhotoImage(file="place_button_hover.png")

        # create a button with the normal image and resize it
        button_5 = tk.Button(
            root,
            image=button_image_normal_5,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # reposition the button and place it on the window
        button_5.place(x=278, y=469, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_5(event):
            button_5.config(image=button_image_hover_5)

        def switch_button_image_back_5(event):
            button_5.config(image=button_image_normal_5)

        # bind the button hover events to switch_button_image function
        button_5.bind("<Enter>", switch_button_image_5)
        button_5.bind("<Leave>", switch_button_image_back_5)

        # define function to exit the GUI
        def exit_gui(event):
            time.sleep(1)
            root.destroy()

        button_5.bind("<Button-1>", exit_gui)

        button_image_normal_6 = tk.PhotoImage(file="gamble_button.png")
        button_image_hover_6 = tk.PhotoImage(file="gamble_button_hover.png")

        # create a button with the normal image and resize it
        button_6 = tk.Button(
            root,
            image=button_image_normal_6,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # reposition the button and place it on the window
        button_6.place(x=418, y=469, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_6(event):
            button_6.config(image=button_image_hover_6)

        def switch_button_image_back_6(event):
            button_6.config(image=button_image_normal_6)

        # bind the button hover events to switch_button_image function
        button_6.bind("<Enter>", switch_button_image_6)
        button_6.bind("<Leave>", switch_button_image_back_6)

        # define function to exit the GUI
        def exit_gui(event):
            time.sleep(1)
            root.destroy()

        # bind the button click event to exit_gui function
        button_6.bind("<Button-1>", exit_gui)

        button_image_normal_7 = tk.PhotoImage(file="draw_button.png")
        button_image_hover_7 = tk.PhotoImage(file="draw_button_hover.png")

        # create a button with the normal image and resize it
        button_7 = tk.Button(
            root,
            image=button_image_normal_7,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # reposition the button and place it on the window
        button_7.place(x=558, y=469, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_7(event):
            button_7.config(image=button_image_hover_7)

        def switch_button_image_back_7(event):
            button_7.config(image=button_image_normal_7)

        # bind the button hover events to switch_button_image function
        button_7.bind("<Enter>", switch_button_image_7)
        button_7.bind("<Leave>", switch_button_image_back_7)

        # define function to exit the GUI
        def exit_gui(event):
            time.sleep(1)
            root.destroy()

        # bind the button click event to exit_gui function
        button_7.bind("<Button-1>", exit_gui)

    def clear_gui_2(event):
        # destroy all buttons
        button.destroy()
        button_2.destroy()
        button_3.destroy()
        bg_image = tk.PhotoImage(file="background_info.png")
        bg_label.config(image=bg_image)
        bg_label.image = bg_image
        text_frame = tk.Frame(root, bg="#343541", highlightthickness=0, bd=0)
        text_frame.place(
            relx=0.5, rely=0.3915, relwidth=0.85, relheight=0.57, anchor="center"
        )
        text_widget = tk.Text(
            text_frame,
            font=("Lemon Milk Pro Regular", 17),
            bg="#343541",
            fg="white",
            wrap="word",
            bd=0,
            highlightthickness=0,
        )
        text_widget.insert(
            "end",
            "Welcome to Cylense! In this game, you'll be facing off against a bot with your own deck of 25 cards. At the start of each game, you and your opponent will draw 5 cards from your deck. During your turn, you'll have the option to place a monster card onto your field, attack with a monster on your field, gamble for a chance at a positive or negative outcome, or draw a new card. Be careful not to let your hand get too full, as you can only have a maximum of 7 cards at a time. When attacking, the difference between your monster's ATTACK stat and the opposing monster's DEFENSE stat determines how much damage you or your opponent will take. Each player starts with 10000 lifepoints, and the goal is to whittle your opponent's lifepoints down to zero before they do the same to you. Good luck, and have fun playing!",
        )
        text_widget.config(state="disabled")
        text_widget.pack(fill="both", expand=True)

        button_image_normal_8 = tk.PhotoImage(file="play_button.png")
        button_image_hover_8 = tk.PhotoImage(file="play_button_hover.png")

        # create a button with the normal image and resize it
        button_8 = tk.Button(
            root,
            image=button_image_normal_8,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # reposition the button and place it on the window
        button_8.place(x=69, y=464, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_8(event):
            button_8.config(image=button_image_hover_8)

        def switch_button_image_back_8(event):
            button_8.config(image=button_image_normal_8)

        # bind the button hover events to switch_button_image function
        button_8.bind("<Enter>", switch_button_image_8)
        button_8.bind("<Leave>", switch_button_image_back_8)
        # define function to exit the GUI
        # bind the button click event to exit_gui function

        button_8.bind("<Button-1>", clear_gui_1)

        button_image_normal_9 = tk.PhotoImage(file="exit_button.png")
        button_image_hover_9 = tk.PhotoImage(file="exit_button_hover.png")

        # create a button with the normal image and resize it
        button_9 = tk.Button(
            root,
            image=button_image_normal_9,
            width=100,
            height=103,
            bd=0,
            relief="sunken",
            highlightthickness=0,
            activebackground="white",
        )

        # reposition the button and place it on the window
        button_9.place(x=625, y=464, anchor="nw")

        # define function to switch button image on mouse hover
        def switch_button_image_9(event):
            button_9.config(image=button_image_hover_9)

        def switch_button_image_back_9(event):
            button_9.config(image=button_image_normal_9)

        # bind the button hover events to switch_button_image function
        button_9.bind("<Enter>", switch_button_image_9)
        button_9.bind("<Leave>", switch_button_image_back_9)

        # define function to exit the GUI
        def exit_gui(event):
            time.sleep(1)
            root.destroy()

        # bind the button click event to exit_gui function
        button_9.bind("<Button-1>", exit_gui)

    # bind the button hover events to switch_button_image function
    button.bind("<Enter>", switch_button_image)
    button.bind("<Leave>", switch_button_image_back)

    # bind the button click event to clear_gui function
    button.bind("<Button-1>", clear_gui_1)

    # place the button on the window
    button.place(x=button_x, y=button_y, anchor="nw")

    # create photo objects for the button images
    button_image_normal_2 = tk.PhotoImage(file="button_2.png")
    button_image_hover_2 = tk.PhotoImage(file="button_2_hover.png")

    # create a button with the normal image
    button_2 = tk.Button(
        root,
        image=button_image_normal_2,
        width=button_width,
        height=button_height,
        bd=0,
        relief="sunken",
        highlightthickness=0,
        activebackground="white",
    )

    # define function to switch button image on mouse hover
    def switch_button_image_2(event):
        button_2.config(image=button_image_hover_2)

    def switch_button_image_back_2(event):
        button_2.config(image=button_image_normal_2)

    # bind the button hover events to switch_button_image function
    button_2.bind("<Enter>", switch_button_image_2)
    button_2.bind("<Leave>", switch_button_image_back_2)
    button_2.bind("<Button-1>", clear_gui_2)

    # place the button on the window below the first button
    button_2.place(x=button_x, y=button_y + button_height + 10, anchor="nw")
    # create photo objects for the button images
    button_image_normal_3 = tk.PhotoImage(file="button_3.png")
    button_image_hover_3 = tk.PhotoImage(file="button_3_hover.png")

    # create a button with the normal image
    button_3 = tk.Button(
        root,
        image=button_image_normal_3,
        width=button_width,
        height=button_height,
        bd=0,
        relief="sunken",
        highlightthickness=0,
        activebackground="white",
    )

    # define function to switch button image on mouse hover
    def switch_button_image_3(event):
        button_3.config(image=button_image_hover_3)

    def switch_button_image_back_3(event):
        button_3.config(image=button_image_normal_3)

    # bind the button hover events to switch_button_image function
    button_3.bind("<Enter>", switch_button_image_3)
    button_3.bind("<Leave>", switch_button_image_back_3)

    # place the button on the window below the second button
    button_3.place(x=button_x, y=button_y + (2 * button_height) + 20, anchor="nw")

    # define function to exit the GUI
    def exit_gui(event):
        time.sleep(1)
        root.destroy()

    # bind the button click event to exit_gui function
    button_3.bind("<Button-1>", exit_gui)

    # run the GUI
    root.mainloop()


create_gui()
