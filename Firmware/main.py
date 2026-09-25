import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# RP2040-ZERO pin map from Aegis60 schematic/netlist.
keyboard.col_pins = (
    board.GP6,   # COL0
    board.GP9,   # COL1
    board.GP29,  # COL2
    board.GP28,  # COL3
    board.GP27,  # COL4
    board.GP26,  # COL5
    board.GP15,  # COL6
    board.GP14,  # COL7
    board.GP13,  # COL8
    board.GP12,  # COL9
    board.GP11,  # COL10
    board.GP10,  # COL11
    board.GP8,   # COL12
    board.GP7,   # COL13
)

keyboard.row_pins = (
    board.GP2,  # ROW0
    board.GP0,  # ROW1 (net label UATRT_TX in project files)
    board.GP1,  # ROW2 (net label UART_RX in project files)
    board.GP3,  # ROW3
    board.GP4,  # ROW4
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

NO = KC.NO

keyboard.keymap = [
    [
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
    ],
    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y,
        KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
    ],
    [
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H,
        KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, NO, KC.ENT,
    ],
    [
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, NO, KC.B,
        KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, NO, KC.RSFT,
    ],
    [
        KC.LCTL, KC.LGUI, KC.LALT, NO, NO, NO, KC.SPC,
        NO, NO, KC.RALT, KC.RGUI, KC.APP, NO, KC.RCTL,
    ],
]

if __name__ == '__main__':
    keyboard.go()
