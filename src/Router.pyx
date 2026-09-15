

cimport MagDatabase

class Router:

    def __init__(self, db, str cellname):

        self.db     = db
        self.cell   = db.getCell(cellname)
        self.layer  = 'metal1'

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

        if direction == 's':
            new_y -= length

            xbot = self.cursor_x - width // 2
            ybot = new_y - width // 2

            xtop = self.cursor_x + width // 2
            ytop = self.cursor_y + width // 2

        if direction == 'e':
            new_x += length

            xbot = self.cursor_x - width // 2
            ybot = self.cursor_y - width // 2

            xtop = new_x + width // 2
            ytop = new_y + width // 2

        if direction == 'w':
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

        if direction == 'n':
            self.route(direction, dest - self.cursor_y, width)
        elif direction == 's':
            self.route(direction, self.cursor_y - dest, width)
        elif direction == 'e':
            self.route(direction, dest - self.cursor_x, width)
        elif direction == 'w':
            self.route(direction, self.cursor_x - dest, width)
       


    def via(self, layer, w, h):

        if (self.layer == 'metal1' and layer == 'metal2') or (self.layer == 'metal2' and layer == 'metal1'):
            l = 'via1'

            self.cell.addRect(l, self.cursor_x - w / 2, self.cursor_y - h / 2, self.cursor_x + w / 2, self.cursor_y + w / 2)

            self.layer = layer
    
        else:

            raise ValueError(f"Unknown layer pair: {self.layer} {layer}")

