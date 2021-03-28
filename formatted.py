import tkinter as tk
#import ttk
from tkinter import ttk
from difflib import SequenceMatcher
import pandas as pd

class Win(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.mainf = tk.Frame(master, height=1000, width=1000, pady=50, padx=50)
        self.mainf.grid(row=10, column=10)



        self.s = ttk.Style()
        self.s.theme_use('alt')

        self.colors = ['red', 'green', 'blue', 'orange']
        self.mainf.configure(background='orange')
        self.s.theme_use('clam')

        some_input = "test input widget"
        self.some_entry = tk.Entry(self.mainf, textvariable=some_input, width=18)
        self.some_entry.insert(0, "Enter the fact")
        self.some_entry.grid(row=1, column=2, padx=10, pady=10)
        # self.some_entry.place(x=20, y=30)

        self.my_string_var = tk.StringVar()
        print("1")

        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()

        def result_1():
            self.my_string_var.set("result1")

        def result_2():
            self.my_string_var.set("result2")

        def result_3():
            data = pd.read_csv("total_news.csv")
            for i in range(10):
                print(self.some_entry.get(), data.loc[[i]]["Statement"])
                score = similar(str(self.some_entry.get()), str(data.loc[[i]]["Statement"]))
                # print(score)
                if score > 0.6:
                    label_list = list(data.loc[[i]]["Label"])
                    print(label_list[0])
                    self.my_string_var.set(str(label_list[0]))
                    break
                else:
                    print(score)
            # self.my_string_var.set("result3")

        self.my_string_var.set("Results")

        # create a label widget
        my_label = ttk.Label(self.mainf, textvariable=self.my_string_var)

        b1 = ttk.Button(self.mainf, text="Train", command=result_1)
        b2 = ttk.Button(self.mainf, text="Predict", command=result_2)
        b3 = ttk.Button(self.mainf, text="Scrape", command=result_3)

        b1.grid(row=3, column=1, padx=10, pady=10)
        b2.grid(row=3, column=2, padx=10, pady=10)
        b3.grid(row=3, column=3, padx=10, pady=10)
        my_label.grid(row=5, column=2, padx=10, pady=20)




    def colour_btns(self):
        self.red = ttk.Button(self.mainf, text="red",
                              command=lambda: self.change_background(
                                  self.colors[0]))
        self.green = ttk.Button(self.mainf, text="green",
                                command=lambda: self.change_background(
                                    self.colors[1]))
        self.blue = ttk.Button(self.mainf, text="blue",
                               command=lambda: self.change_background(
                                   self.colors[2]))
        self.orange = ttk.Button(self.mainf, text="orange",
                                 command=lambda: self.change_background(
                                     self.colors[3]))
        self.red.grid(row=0, column=0)
        self.green.grid(row=1, column=0)
        self.blue.grid(row=2, column=0)
        self.orange.grid(row=3, column=0)

    def theme_btns(self):
        self.alt = ttk.Button(self.mainf, text="alt",
                              command=lambda: self.change_theme('alt'))

        self.aqua = ttk.Button(self.mainf, text="aqua",
                               command=lambda: self.change_theme('aqua'))
        self.clam = ttk.Button(self.mainf, text="clam",
                               command=lambda: self.change_theme('clam'))
        self.deflt = ttk.Button(self.mainf, text="default",
                                command=lambda: self.change_theme('default'))
        self.classic = ttk.Button(self.mainf, text="classic",
                                  command=lambda: self.change_theme('classic'))
        self.alt.grid(row=0, column=1)
        self.aqua.grid(row=1, column=1)
        self.clam.grid(row=2, column=1)
        self.deflt.grid(row=3, column=1)
        self.classic.grid(row=4, column=1)

    def change_background(self, color):
        self.mainf.configure(background='{}'.format(color))

    def change_theme(self, theme):
        """
        Changes theme of gui. Input is name of theme as string.
        """
        self.s.theme_use(theme)


root = tk.Tk()
root.title('Detect the Rumour')
root.update()

app = Win(root)

root.mainloop()