"""The help button and its thing"""

import tkinter as tk
from tkinter import messagebox

class HelpMe:
    """The button and its window"""
    def __init__(self, parent):

        self.parent = parent

        # Just the button this time
        self.help_me = tk.Button(
            self.parent.parent.parent.root,
            text= " HELP ",
            font= ("Consolas", 16),
            bg= "yellow",
            fg= "black",
            activebackground= "cyan",
            activeforeground= "white",
            command= self.pop_it_up
        )

    def button_placement(self):
        """Place the button if conditions are suitable"""
        if self.parent.parent.parent.parent.prp.timer_chosen_time != -1 or \
            self.parent.parent.parent.parent.prp.timer_style == "chronometer":
            self.help_me.place_forget()
            return

        self.help_me.place(x= 262, y= 510)

    def pop_it_up(self):
        """Pop-up the time converter"""
        win = tk.Toplevel(self.parent.parent.parent.root)
        win.geometry("300x175")
        win.title("Time Converter")
        win.configure(background= "#c0c0c0")
        win.iconphoto(False, tk.PhotoImage(file= "icon.png"))

        # Entry + Label
        tk.Label(win, text="Minutes:", bg= "#c0c0c0").grid(row=1, column=0, pady= (15, 0))
        minute_entry = tk.Entry(win, width=5)
        minute_entry.grid(row=1, column=1, pady= (10, 0))

        tk.Label(win, text="Seconds:", bg= "#c0c0c0").grid(row=2, column=0)
        second_entry = tk.Entry(win, width=5)
        second_entry.grid(row=2, column=1)

        result_label = tk.Label(win, text="Total: —", bg= "#c0c0c0")
        result_label.grid(row=4, column=0, columnspan=2)

        i_got_you_label = tk.Label(
        win, 
        text="Don't worry, I've automatically entered this number\nyou may close this window now.",
        bg= "#c0c0c0", fg= "#c0c0c0"
        )

        i_got_you_label.grid(row=6, column=0, columnspan=2, padx= (10, 0))

        def vanish_label():
            """Hide the i_got_you_label text by using colors"""
            i_got_you_label.config(fg= "#c0c0c0")

        def handler(_):
            """A function to run this function"""
            vanish_label()

        minute_entry.bind("<Button-1>", handler)
        second_entry.bind("<Button-1>", handler)

        def calculate_total():
            """Calculate the total time in seconds"""
            try:
                minutes = int(minute_entry.get() or 0)
                seconds = int(second_entry.get() or 0)
                total = minutes * 60 + seconds

                if (minutes, seconds) == (0, 0):
                    result_label.config(text= "Okay I saw you clicking this button soullessly")
                    vanish_label()
                    self.parent.timer_custom_entrybox.delete(0, tk.END)
                    self.parent.timer_custom_entrybox.insert(0, "120")

                elif (minutes < 0 and seconds < 0):
                    result_label.config(text= "Negative numbers are not tolerated.")
                    vanish_label()

                    self.parent.timer_custom_entrybox.delete(0, tk.END)
                    self.parent.timer_custom_entrybox.insert(0, str(seconds))
                    

                elif (minutes == 0 and seconds > 0):

                    result_label.config(
                        text= f"{seconds} seconds is {total} seconds\n"
                        "Wasn't that a little obvious?"
                    )
                    vanish_label()
                    self.parent.timer_custom_entrybox.delete(0, tk.END)
                    self.parent.timer_custom_entrybox.insert(0, str(seconds))

                elif total < 3600:

                    result_label.config(text= f"Total: {total} seconds")
                    i_got_you_label.config(foreground= "black")
                    self.parent.timer_custom_entrybox.delete(0, tk.END)
                    self.parent.timer_custom_entrybox.insert(0, str(total))

                else:
                    result_label.config(text= "More than an hour? Are you testing the boundaries?")
                    vanish_label()
                    self.parent.timer_custom_entrybox.delete(0, tk.END)
                    self.parent.timer_custom_entrybox.insert(0, "3600")

                self.parent.parent.parent.parent.upd.update_chosen_time(int(total))

            except ValueError:
                messagebox.showerror("Error", "You should enter valid numbers")

        tk.Button(win, text="Calculate",command=calculate_total).grid(row=3, column=0, columnspan=2)
