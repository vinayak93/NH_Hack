import tkinter as tk
#import ttk
from tkinter import ttk
from difflib import SequenceMatcher
import pandas as pd
from PIL import ImageTk, Image


class Win(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.mainf = tk.Frame(master, height=1000, width=1000, pady=50, padx=50)
        self.mainf.grid(row=10, column=10)



        self.s = ttk.Style()
        self.s.theme_use('alt')

        self.colors = ['red', 'green', 'blue', 'orange']
        self.mainf.configure(background='light blue')
        self.s.theme_use('clam')

        some_input = "test input widget"
        self.some_entry = tk.Entry(self.mainf, textvariable=some_input, width=18)
        self.some_entry.insert(0, "Please enter the text...")
        self.some_entry.grid(row=1, column=2, padx=10, pady=30)
        # self.some_entry.place(x=20, y=30)
        self.img = Image.open("hackathon.png")
        self.image1 = self.img.resize((120, 60), Image.ANTIALIAS)
        self.my_string_var = tk.StringVar()

        self.load = Image.open("unh.jpeg")
        self.loads = self.load.resize((120, 60), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.loads)


        # labels can be text or images
        self.img = ttk.Label(self.mainf, image=self.render)
        self.img.image = self.render
        self.img.place(x=385, y=260)
        print("1")

        def similar(a, b):
            return SequenceMatcher(None, a, b).ratio()

        def result_1():
            self.my_string_var.set("Training complete")

        def result_2():
            self.my_string_var.set("Hoax-BUSTER Prediction:"+ "result2")

        def result_3():
            data = pd.read_csv("total_news.csv")
            for i in range(10):
                print(self.some_entry.get(), data.loc[[i]]["Statement"])
                score = similar(str(self.some_entry.get()), str(data.loc[[i]]["Statement"]))
                # print(score)
                if score > 0.6:
                    label_list = list(data.loc[[i]]["Label"])
                    print(label_list[0])
                    if (str(label_list[0]) == "true") or (str(label_list[0]) == "mostly-true") or (str(label_list[0]) == "half-true"):
                        self.my_string_var.set("Scrape Prediction:"+ "real")
                    else:
                        self.my_string_var.set("Scrape Prediction:" + "fake")
                    break
                else:
                    self.my_string_var.set("Scrape Prediction:" + "not found")
                    print(score)
            # self.my_string_var.set("result3")

        self.my_string_var.set("Results")
        test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.mainf, image=test)
        self.label1.image = test

        # create a label widget
        my_label = ttk.Label(self.mainf, textvariable=self.my_string_var)
        result_label = ttk.Label(self.mainf, text = "scrape result is")

        b1 = ttk.Button(self.mainf, text="Train", command=result_1)
        b2 = ttk.Button(self.mainf, text="Predict", command=result_2)
        b3 = ttk.Button(self.mainf, text="Scrape", command=result_3)

        b1.grid(row=3, column=1, padx=10, pady=10)
        b2.grid(row=3, column=2, padx=10, pady=10)
        b3.grid(row=3, column=3, padx=10, pady=10)
        #result_label.grid(row=5, column=1,  padx = 10, pady=50)
        my_label.grid(row=5, column=2, pady=60)
        #label1.grid(row=15, column=0, pady = 0)
        self.label1.place(x=-45, y=260)









root = tk.Tk()
root.title('Detect the Rumour')
root.update()

app = Win(root)

root.mainloop()