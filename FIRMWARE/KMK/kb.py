import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()
        self.col_pins = (board.D1, board.D0, board.D9)
        self.row_pins = (board.D3, board.D2, board.D6)
        self.diode_orientation = DiodeOrientation.ROW2COL
        self.coord_mapping = [
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        ]
