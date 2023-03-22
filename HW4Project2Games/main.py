"""
name: Derek D'Arcy
Description: This program is the gui for project 2 which will have RPS and TICTACTOE
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import os
import time


'''
Purple Illusion - #beadfe
Dreamy Candy Forest - #b4a2f1
Magic Carpet - #897dc7
Seven Seas - #446073
Continental Waters - #9bc5cc
Quick-Freeze - #c3dfe4
Wave Splash - #c7e2e7

'''


class Controller_Class:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)

        self.bold_font = ("Arial", 20, "bold")
        self.large_font = ("Arial", 16)
        self.normal_font = ("Arial", 12)

        self.purple_illusion = "#beadfe"
        self.dream_forest = "#b4a2f1"
        self.magic_carpet = "#897dc7"
        self.seven_seas = "#446073"
        self.continental_waters = "#9bc5cc"
        self.quick_freeze = "#c3dfe4"
        self.wave_splash = "#c7e2e7"


class Page_Container(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F, geometry in zip((Welcome, RPS_Settings, RPS_One_Choose, RPS_Two_Choose, RPS_Output, TTT_Settings, TTT_Board), ('300x300', '400x400', '300x300', '400x400', '', '250x300', '400x400')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)

            self.frames[page_name] = (frame, geometry)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Welcome")
        self.title("Minigame Corner")

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame, geometry = self.frames[cont]
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()


class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(bg=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create button and labels
        title_label = Label(self, text="Mini Game Corner", font=self.control.large_font, fg=self.control.seven_seas,
                            background=self.control.purple_illusion, width=15)
        rps_button = Button(self, text="Rock Paper Scissors", font=self.control.normal_font, borderwidth=5,
                            width=20, height=5, background=self.control.quick_freeze, command=lambda: controller.show_frame("RPS_Settings"))
        ttt_button = Button(self, text="Tic-Tac-Toe", borderwidth=5, background=self.control.quick_freeze,
                            font=self.control.normal_font, width=20, height=5, command=lambda: controller.show_frame("TTT_Settings"))

        # add button and labels to frame with grid
        title_label.grid(row=0, column=0,  padx=5, pady=5, sticky=NSEW)
        rps_button.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)
        ttt_button.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)


class RPS_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        self.config(bg=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        top_row = tk.Frame(self)
        top_row.config(background=self.control.purple_illusion)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(3, 3)

        # create button and labels
        button_home_page = Button(top_row, image=home_photo_sub, padx=40, pady=10, background=self.control.purple_illusion,
                                  relief=GROOVE, borderwidth=2, command=lambda: controller.show_frame("Welcome"))
        button_home_page.image = home_photo_sub  # type: ignore # keep a reference
        button_home_page.pack(side="left")
        rps_label = Label(top_row, text="Rock-Paper-Scissors", font=self.control.bold_font, width=18, background=self.control.purple_illusion, borderwidth=5)
        rps_label.pack(side="left")

        # create buttons
        one_player_button = Button(self, text="One Player", font=("Arial", 24), width=15, borderwidth=5,
                                   background=self.control.continental_waters, relief=SUNKEN, command=lambda: one_player_button_press())
        two_player_button = Button(self, text="Two Player", font=("Arial", 24), width=15, borderwidth=5,
                                   background=self.control.seven_seas, relief=RAISED, command=lambda: two_player_button_press())
        ready_button = Button(self, text="Play!", font=("Arial", 24), width=15, borderwidth=5, background=self.control.magic_carpet, command=lambda: ready_button_press())

        # add to grids
        top_row.grid(column=0, row=0)
        one_player_button.grid(column=0, row=1)
        two_player_button.grid(column=0, row=2)
        ready_button.grid(column=0, row=3)

        global rps_players
        rps_players = 1

        def one_player_button_press():
            global rps_players
            rps_players = 1
            one_player_button.config(relief=SUNKEN, background=self.control.continental_waters)
            two_player_button.config(relief=RAISED, background=self.control.seven_seas)

        def two_player_button_press():
            global rps_players
            rps_players = 2
            one_player_button.config(relief=RAISED, background=self.control.seven_seas)
            two_player_button.config(relief=SUNKEN, background=self.control.continental_waters)

        def ready_button_press():
            if (rps_players == 1):
                controller.show_frame("RPS_One_Choose")
            elif (rps_players == 2):
                controller.show_frame("RPS_Two_Choose")


class RPS_One_Choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.config(background=self.control.purple_illusion)

        choose_label = Label(self, text="Make your choice!", font=self.control.bold_font,
                             foreground=self.control.seven_seas, background=self.control.purple_illusion, padx=5, pady=5)
        rock_button = Button(self, text="Rock", relief=SUNKEN, background=self.control.continental_waters, command=lambda: rock_button_press())
        paper_button = Button(self, text="Paper", relief=RAISED, background=self.control.seven_seas, command=lambda: paper_button_press())
        scissor_button = Button(self, text="Scissor", relief=RAISED, background=self.control.seven_seas, command=lambda: scissor_button_press())
        shoot_button = Button(self, text="Shoot!", relief=RAISED, background=self.control.magic_carpet, command=lambda: shoot_button_press())

        choose_label.grid(column=0, row=0, sticky=NSEW)
        rock_button.grid(column=0, row=1, sticky=NSEW)
        paper_button.grid(column=0, row=2, sticky=NSEW)
        scissor_button.grid(column=0, row=3, sticky=NSEW)
        shoot_button.grid(column=0, row=4, sticky=NSEW)

        global player_one_choice
        player_one_choice = 0

        def rock_button_press():
            global player_one_choice
            player_one_choice = 1
            rock_button.config(relief=SUNKEN, background=self.control.continental_waters)
            paper_button.config(relief=RAISED, background=self.control.seven_seas)
            scissor_button.config(relief=RAISED, background=self.control.seven_seas)

        def paper_button_press():
            global player_one_choice
            player_one_choice = 2
            rock_button.config(relief=RAISED, background=self.control.seven_seas)
            paper_button.config(relief=SUNKEN, background=self.control.continental_waters)
            scissor_button.config(relief=RAISED, background=self.control.seven_seas)

        def scissor_button_press():
            global player_one_choice
            player_one_choice = 3
            rock_button.config(relief=RAISED, background=self.control.seven_seas)
            paper_button.config(relief=RAISED, background=self.control.seven_seas)
            scissor_button.config(relief=SUNKEN, background=self.control.continental_waters)

        def shoot_button_press():
            global player_two_choice
            player_two_choice = random.randint(1, 3)
            controller.show_frame("RPS_Output")


class RPS_Two_Choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class RPS_Output(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        animation = tk.Frame(self)
        animation.config(background=self.control.purple_illusion)
        result_page = tk.Frame(self)

        animation.grid(row=0, column=0)
        result_page.grid(row=0, column=0, sticky='NESW')

        animation.grid()
        result_page.grid_remove()

        # This part is the animation part
        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.config(background=self.control.purple_illusion)

        # images
        rps_gif_path = os.path.join(self.control.absolute_path, 'images/infiniteRPS.gif')
        rps_gif = PhotoImage(file=rps_gif_path)
        rps_gif_sub = rps_gif.subsample(3, 3)

        display = Label(animation, image=rps_gif_sub, relief=FLAT, padx=10, pady=20, borderwidth=0)
        display.image = rps_gif_sub  # type: ignore # keep a reference

        display.grid(column=0, row=0)

        result = Button(animation, text="See Result", background=self.control.purple_illusion,
                        fg=self.control.seven_seas, command=lambda: update_results())
        result.grid(column=0, row=1)

        frameList = []
        frame_index = 0

        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(frame_index)
                frame = tk.PhotoImage(file=rps_gif_path, format=part)
            except:
                last_frame = frame_index - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            frameList.append(frame)
            frame_index += 1        # Next frame index

        def animate(frame_number):
            if frame_number > last_frame:
                frame_number = 0
            display.config(image=frameList[frame_number])
            animation.after(175, animate, frame_number+1)

        animate(0)

        # End of animation part

        # helps with dynamic resizing
        result_page.grid_rowconfigure(0, weight=1)
        result_page.grid_columnconfigure(0, weight=1)
        result_page.grid_rowconfigure(1, weight=1)
        result_page.grid_columnconfigure(1, weight=1)
        result_page.grid_rowconfigure(2, weight=1)
        result_page.grid_columnconfigure(2, weight=1)
        result_page.grid_rowconfigure(3, weight=1)
        result_page.grid_columnconfigure(3, weight=1)
        result_page.grid_rowconfigure(4, weight=1)

        self.config(background=self.control.purple_illusion)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(5, 5)

        restart_img_path = os.path.join(self.control.absolute_path, 'images/restart.png')
        restart_photo = PhotoImage(file=restart_img_path)
        restart_photo_sub = restart_photo.subsample(5, 5)

        left_rock_path = os.path.join(self.control.absolute_path, 'images/leftRockHand.png')
        left_rock_photo = PhotoImage(file=left_rock_path)
        left_rock_photo_sub = left_rock_photo.subsample(2, 2)

        right_rock_path = os.path.join(self.control.absolute_path, 'images/rightRockHand.png')
        right_rock_photo = PhotoImage(file=right_rock_path)
        right_rock_photo_sub = right_rock_photo.subsample(2, 2)

        left_paper_path = os.path.join(self.control.absolute_path, 'images/leftPaperHand.png')
        left_paper_photo = PhotoImage(file=left_paper_path)
        left_paper_photo_sub = left_paper_photo.subsample(2, 2)

        right_paper_path = os.path.join(self.control.absolute_path, 'images/rightPaperHand.png')
        right_paper_photo = PhotoImage(file=right_paper_path)
        right_paper_photo_sub = right_paper_photo.subsample(2, 2)

        left_scissor_path = os.path.join(self.control.absolute_path, 'images/leftScissorHand.png')
        left_scissor_photo = PhotoImage(file=left_scissor_path)
        left_scissor_photo_sub = left_scissor_photo.subsample(2, 2)

        right_scissor_path = os.path.join(self.control.absolute_path, 'images/rightScissorHand.png')
        right_scissor_photo = PhotoImage(file=right_scissor_path)
        right_scissor_photo_sub = right_scissor_photo.subsample(2, 2)

        # create buttons and labels
        p1_chose_label = Label(result_page, text="Player 1 Chose: ", background=self.control.purple_illusion)
        p1_picture = Label(result_page, image=left_rock_photo_sub, background=self.control.purple_illusion)
        p1_picture.image = left_rock_photo_sub  # type: ignore

        p2_chose_label = Label(result_page, text="Player 2 Chose: ", background=self.control.purple_illusion)
        p2_picture = Label(result_page, image=right_rock_photo_sub, background=self.control.purple_illusion)
        p2_picture.image = right_rock_photo_sub  # type: ignore

        winner_text_label = Label(result_page, text="Winner: ", background=self.control.purple_illusion)
        winner_box = Label(result_page, text="Player 1!", background=self.control.purple_illusion)

        home_button = Button(result_page, image=home_photo_sub, background=self.control.purple_illusion, command=lambda: home_button_press())
        home_button.image = home_photo_sub  # type: ignore # keep a reference
        play_again_button = Button(result_page, image=restart_photo_sub, background=self.control.purple_illusion, command=lambda: restart_button_press())
        play_again_button.image = restart_photo_sub  # type: ignore # keep a reference

        # layout to grid
        p1_chose_label.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        p1_picture.grid(row=1, column=0, columnspan=2, rowspan=2, sticky=NSEW)

        p2_chose_label.grid(row=0, column=2, columnspan=2, sticky=NSEW)
        p2_picture.grid(row=1, column=2, columnspan=2, rowspan=2, sticky=NSEW)

        winner_text_label.grid(row=3, column=0, columnspan=3, sticky=NSEW)
        winner_box.grid(row=4, column=0, columnspan=3, sticky=NSEW)

        home_button.grid(row=3, column=3, sticky=NSEW)
        play_again_button.grid(row=4, column=3, sticky=NSEW)

        def home_button_press():
            controller.show_frame("Welcome")
            result_page.grid_forget()
            animation.grid()

        def restart_button_press():
            controller.show_frame("RPS_Settings")
            result_page.grid_forget()
            animation.grid()

        def update_results():
            animation.grid_remove()
            result_page.grid()
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            if (player_one_choice == 1):
                p1_picture.config(image=left_rock_photo_sub)
                p1_picture.image = left_rock_photo_sub  # type: ignore
            elif (player_one_choice == 2):
                p1_picture.config(image=left_paper_photo_sub)
                p1_picture.image = left_paper_photo_sub  # type: ignore
            elif (player_one_choice == 3):
                p1_picture.config(image=left_scissor_photo_sub)
                p1_picture.image = left_scissor_photo_sub  # type: ignore

            if (player_two_choice == 1):
                p2_picture.config(image=right_rock_photo_sub)
                p2_picture.image = right_rock_photo_sub  # type: ignore
                if (player_one_choice == 1):
                    winner_box.config(text="Tie")
                elif (player_one_choice == 2):
                    winner_box.config(text="Player 1 Wins!")
                else:
                    winner_box.config(text="Player 2 Wins!")
            elif (player_two_choice == 2):
                p2_picture.config(image=right_paper_photo_sub)
                p2_picture.image = right_paper_photo_sub  # type: ignore
                if (player_one_choice == 1):
                    winner_box.config(text="Player 2 Wins!")
                elif (player_one_choice == 2):
                    winner_box.config(text="Tie")
                else:
                    winner_box.config(text="Player 1 Wins!")
            elif (player_two_choice == 3):
                p2_picture.config(image=right_scissor_photo_sub)
                p2_picture.image = right_scissor_photo_sub  # type: ignore
                if (player_one_choice == 1):
                    winner_box.config(text="Player 1 Wins!")
                elif (player_one_choice == 2):
                    winner_box.config(text="Player 2 Wins!")
                else:
                    winner_box.config(text="Tie")


class TTT_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5, background=self.control.purple_illusion)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        easy_hard = tk.Frame(self)

        # images
        home_img_path = os.path.join(self.control.absolute_path, 'images/home.png')
        home_photo = PhotoImage(file=home_img_path)
        home_photo_sub = home_photo.subsample(5, 5)

        title = Label(self, text="Tic-Tac-Toe", font=self.control.bold_font, background=self.control.purple_illusion)
        home_button = Button(self, image=home_photo_sub, background=self.control.purple_illusion, command=lambda: home_button_press())
        home_button.image = home_photo_sub  # type: ignore # keep a reference
        two_player = Button(self, text="Two Players", relief=SUNKEN, font=self.control.large_font, background=self.control.continental_waters)
        one_player = Button(self, text="One Player", font=self.control.large_font, background=self.control.seven_seas)

        easy = Button(easy_hard, text="Easy", font=self.control.large_font, background=self.control.seven_seas)
        hard = Button(easy_hard, text="Hard", font=self.control.large_font, background=self.control.seven_seas)
        easy.pack(side="left")
        hard.pack(side="left")

        play_button = Button(self, text="Play!", font=self.control.bold_font, background=self.control.magic_carpet)

        title.grid(column=1, row=0)
        home_button.grid(column=0, row=0)
        two_player.grid(column=0, row=1, columnspan=2)
        one_player.grid(column=0, row=2, columnspan=2)
        easy_hard.grid(column=0, row=3, columnspan=2)
        play_button.grid(column=0, row=4, columnspan=2)

        def home_button_press():
            controller.show_frame("Welcome")


class TTT_Board(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.control = Controller_Class()
        self.config(padx=5, pady=5)

        # helps with dynamic resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


root = Page_Container()
root.mainloop()


# ideas:
# change animation into output window, have 2 frames, update all values and pictures upon reveal button click
#
#
#
#
#
#
#

# partner with alejandro on network stuff
# add 2 player local, 2 player end to end
#
#
#
