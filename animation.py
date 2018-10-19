from tkinter import *
from sprite import *
import random


class Animation:
    def __init__(self, w, h):
        self.root = Tk()
        self.canvas = Canvas(self.root,
                             width=w,
                             height=h
                             )
        self.canvas.pack()

        self.start = Button(self.root, text="Start animation", command=self.start_anim)
        self.add_pic = Button(self.root, text="Add Pic", command=self.add_pic)
        self.add_ach = Button(self.root, text="Add Ach", command=self.add_ach)
        self.start.pack()
        self.add_pic.pack()
        self.add_ach.pack()

        self.tooth_pic = PhotoImage(file="ball.png")
        self.tooth_ach = PhotoImage(file="ball2.png")

        self.animate_flag = False
        self.width = w
        self.height = h
        self.sprites = []

        self.root.title("Animation")
        self.loop()
        self.root.mainloop()

    def start_anim(self):
        self.animate_flag = not self.animate_flag
        if self.animate_flag:
            self.start["text"] = "Stop"
        else:
            self.start["text"] = "Start"

    def add_pic(self):
        self.sprites.append(Sprite(self.canvas,
                                   self.width / 2,  # random.randrange(0, w, 10),
                                   self.height / 2,  # random.randrange(0, h, 10),
                                   random.uniform(-5, 5),
                                   random.uniform(-5, 5),
                                   self.tooth_pic
                                   ))

    def add_ach(self):
        self.sprites.append(Sprite(self.canvas,
                                   self.width / 2,  # random.randrange(0, w, 10),
                                   self.height / 2,  # random.randrange(0, h, 10),
                                   random.uniform(-5, 5),
                                   random.uniform(-5, 5),
                                   self.tooth_ach
                                   ))

    def loop(self):
        if self.animate_flag:
            for s in self.sprites:
                s.move(self.width, self.height)
        self.canvas.after(10, self.loop)
