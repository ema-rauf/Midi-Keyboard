# MIDI Keypad firmware (KMK + CircuitPython, Waveshare ESP32-S3-Zero)
# Based on Kai Pereira's MIDI-Keypad firmware, sliders removed.
import keypad
import touchio
from microcontroller import pin

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.modules.midi import MidiKeys
from kmk.scanners import Scanner
from kmk.scanners.keypad import KeysScanner


# KMK has no scanner for touch pads, so this is a small one.
# Don't touch the pads while the board boots: they calibrate on startup.
class TouchScanner(Scanner):
    def __init__(self, pins):
        self.pads = [touchio.TouchIn(p) for p in pins]
        self.pressed = [False] * len(pins)

    @property
    def key_count(self):
        return len(self.pads)

    def scan_for_changes(self):
        for i, pad in enumerate(self.pads):
            touched = pad.value
            if touched != self.pressed[i]:
                self.pressed[i] = touched
                return keypad.Event(i + self.offset, touched)


keyboard = KMKKeyboard()
midi = MidiKeys()
media_keys = MediaKeys()

keyboard.matrix = [
    # Touch keys TOUCH1-TOUCH7 = GP13..GP7 (keys 0-6)
    TouchScanner([pin.GPIO13, pin.GPIO12, pin.GPIO11, pin.GPIO10, pin.GPIO9, pin.GPIO8, pin.GPIO7]),
    # Switches SW1-SW3 = GP4, GP5, GP6 (keys 7-9)
    KeysScanner([pin.GPIO4, pin.GPIO5, pin.GPIO6], value_when_pressed=False, pull=True),
]

# Touch keys play a C major scale, switches play drums
keyboard.keymap = [[
    KC.MIDI_NOTE(60), KC.MIDI_NOTE(62), KC.MIDI_NOTE(64), KC.MIDI_NOTE(65),
    KC.MIDI_NOTE(67), KC.MIDI_NOTE(69), KC.MIDI_NOTE(71),
    KC.MIDI_NOTE(36), KC.MIDI_NOTE(38), KC.MIDI_NOTE(42),  # kick, snare, hi-hat
]]

# Encoder (A = TX/GPIO43, B = RX/GPIO44) controls computer volume
encoder = EncoderHandler()
encoder.pins = ((pin.GPIO43, pin.GPIO44, None),)
encoder.map = [((KC.VOLD, KC.VOLU, KC.NO),)]

keyboard.modules = [midi, encoder]
keyboard.extensions = [
    media_keys,
    # 3 SK6812MINI-E LEDs, data on GP3
    RGB(pixel_pin=pin.GPIO3, num_pixels=3, val_default=80, animation_mode=AnimationModes.RAINBOW),
]

if __name__ == '__main__':
    keyboard.go()
