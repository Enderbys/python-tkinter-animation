class Sprite:
    def __init__(self, canvas, x_position, y_position, dx, dy, ch):
        self.canvas = canvas
        self.dx = dx
        self.dy = dy

        self.img = ch
        self.shape = self.canvas.create_image(x_position,
                                              y_position,
                                              image=self.img)

    def move(self, w, h):
        self.canvas.move(self.shape, self.dx, self.dy)
        pos = self.canvas.coords(self.shape)
        if pos[0] > w:
            self.dx = -self.dx
        if pos[0] < 0:
            self.dx = -self.dx
        if pos[1] > h:
            self.dy = -self.dy
        if pos[1] < 0:
            self.dy = -self.dy
        self.canvas.coords(self.shape, pos)
