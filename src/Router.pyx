

cimport MagDatabase
from collections import deque

class Router:

    def __init__(self, db, str cellname):

        self.db     = db
        self.cell   = db.getCell(cellname)
        self.layer  = 'metal1'
        self.stack  = deque([])

    def begin(self, int x, int y, str layer, int width = 20):

        self.cursor_x = x
        self.cursor_y = y
        self.layer = layer
        self.width = width

    def route(self, str direction, int length, int width):

        new_x = self.cursor_x
        new_y = self.cursor_y

        if direction == 'n':
            new_y += length

            xbot = self.cursor_x - width // 2
            ybot = self.cursor_y - width // 2

            xtop = self.cursor_x + width // 2
            ytop = new_y + width // 2

        elif direction == 's':
            new_y -= length

            xbot = self.cursor_x - width // 2
            ybot = new_y - width // 2

            xtop = self.cursor_x + width // 2
            ytop = self.cursor_y + width // 2

        elif direction == 'e':
            new_x += length

            xbot = self.cursor_x - width // 2
            ybot = self.cursor_y - width // 2

            xtop = new_x + width // 2
            ytop = new_y + width // 2

        elif direction == 'w':
            new_x -= length

            xbot = new_x - width // 2
            ybot = self.cursor_y - width // 2

            xtop = self.cursor_x + width // 2
            ytop = self.cursor_y + width // 2

        self.cell.addRect(self.layer, xbot, ybot, xtop, ytop)

        self.cursor_x = new_x
        self.cursor_y = new_y
        self.width = width

    def routeTo(self, direction, dest, width):

        if direction == 'n' or direction == 's':
            d = dest - self.cursor_y

            if (d < 0):
                self.route('s', -d, width)
            else:
                self.route('n', d, width)
        elif direction == 'e' or direction == 'w': 
            d = dest - self.cursor_x

            if (d < 0):
                self.route('w', -d, width)
            else:
                self.route('e', d, width)
       


    def via(self, layer, w, h):

        if (self.layer == 'metal1' and layer == 'metal2') or (self.layer == 'metal2' and layer == 'metal1'):
            l = 'via1'

            self.cell.addRect(l, self.cursor_x - w / 2, self.cursor_y - h / 2, self.cursor_x + w / 2, self.cursor_y + w / 2)

            self.layer = layer
    
        else:

            raise ValueError(f"Unknown layer pair: {self.layer} {layer}")

    def push(self):
        self.stack.append((self.cursor_x, self.cursor_y, self.layer, self.width))

    def pop(self):
        self.cursor_x, self.cursor_y, self.layer, self.width = self.stack.pop()



