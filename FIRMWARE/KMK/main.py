import board
import digitalio

from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules import Module

from kb import KMKKeyboard


class LayerButton(Module):
    def __init__(self, pin, num_layers):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = digitalio.Pull.UP
        self.prev = True
        self.num_layers = num_layers

    def during_bootup(self, keyboard):
        pass

    def before_matrix_scan(self, keyboard):
        val = self.pin.value
        if not val and self.prev:
            cur = keyboard.active_layers[0] if keyboard.active_layers else 0
            nxt = (cur + 1) % self.num_layers
            keyboard.active_layers = [nxt]
        self.prev = val


keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

NUM_LAYERS = 4
keyboard.modules.append(LayerButton(board.D8, NUM_LAYERS))

keyboard.keymap = [
    [
        KC.MACRO("L0 K1"),
        KC.MACRO("L0 K2"),
        KC.MACRO("L0 K3"),
        KC.MACRO("L0 K4"),
        KC.MACRO("L0 K5"),
        KC.MACRO("L0 K6"),
        KC.MACRO("L0 K7"),
        KC.MACRO("L0 K8"),
        KC.MACRO("L0 K9"),
    ],
    [
        KC.MACRO("L1 K1"),
        KC.MACRO("L1 K2"),
        KC.MACRO("L1 K3"),
        KC.MACRO("L1 K4"),
        KC.MACRO("L1 K5"),
        KC.MACRO("L1 K6"),
        KC.MACRO("L1 K7"),
        KC.MACRO("L1 K8"),
        KC.MACRO("L1 K9"),
    ],
    [
        KC.MACRO("L2 K1"),
        KC.MACRO("L2 K2"),
        KC.MACRO("L2 K3"),
        KC.MACRO("L2 K4"),
        KC.MACRO("L2 K5"),
        KC.MACRO("L2 K6"),
        KC.MACRO("L2 K7"),
        KC.MACRO("L2 K8"),
        KC.MACRO("L2 K9"),
    ],
    [
        KC.MACRO("L3 K1"),
        KC.MACRO("L3 K2"),
        KC.MACRO("L3 K3"),
        KC.MACRO("L3 K4"),
        KC.MACRO("L3 K5"),
        KC.MACRO("L3 K6"),
        KC.MACRO("L3 K7"),
        KC.MACRO("L3 K8"),
        KC.MACRO("L3 K9"),
    ],
]

if __name__ == "__main__":
    keyboard.go()
