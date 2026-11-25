# MIDI Keyboard

A USB MIDI controller on a custom PCB. Touch the copper keys to play notes, press the switches for drums, and turn the knob for volume.

It plugs into a computer over USB-C and shows up as a MIDI instrument, so it works with music software like FL Studio, Ableton or LMMS.

![3D render of the PCB, front](images/3d-front.png)

## How it works

The 7 piano keys are bare copper pads on the PCB. The ESP32-S3 measures their capacitance, so when your finger touches a pad it detects the change and sends a MIDI note. The 3 Choc switches send drum notes, the rotary encoder changes the computer's volume, and 3 RGB LEDs mounted on the back shine through holes in the board.

## Why I made it

I wanted to learn PCB design from start to finish: drawing a schematic, making a custom footprint, laying out and routing a board, and getting it ready to manufacture. A MIDI keypad was a fun way to do that, because at the end I get a real instrument I can make beats with.

![3D render of the PCB, back](images/3d-back.png)

## Features

- 7 capacitive touch keys (C major scale, MIDI notes 60-71)
- 3 Kailh Choc low-profile switches (kick, snare, hi-hat)
- 1 EC11 rotary encoder (computer volume)
- 3 SK6812MINI-E RGB LEDs, reverse-mounted to shine through the board
- Waveshare ESP32-S3-Zero, plugs in over USB-C

## Parts list

| Designator | Part | Qty | Unit price (USD) | Total (USD) |
|---|---|---|---|---|
| U1 | [Waveshare ESP32-S3-Zero](https://www.aliexpress.com/item/1005012733231291.html) | 1 | 6.98 | 6.98 |
| SW1-SW3 | [Kailh Choc low-profile switch, pack of 10 (3 used)](https://www.aliexpress.com/item/1005008883418065.html) | 1 | 5.03 | 5.03 |
| SW4 | [EC11 rotary encoder, 20 mm shaft, with switch](https://www.aliexpress.com/item/1005007644083514.html) | 1 | 1.09 | 1.09 |
| D1-D3 | [SK6812MINI-E RGB LED, pack (3 used)](https://www.aliexpress.com/item/1005008591589739.html) | 1 | 3.16 | 3.16 |
| PCB | [2-layer 1.6 mm FR-4 PCB, 90.6 x 86.6 mm, JLCPCB (5 pcs)](https://cart.jlcpcb.com/quote) | 5 | 0.80 | 4.00 |
| | **Total (before shipping)** | | | **20.26** |

The 7 capacitive touch keys (J1) are bare copper on the PCB, so they are part of the PCB line and have no separate cost.

Full list with links: [BOM.csv](BOM.csv)

## Pin map

| Part | Pins |
|---|---|
| Touch keys 1-7 | GP13, GP12, GP11, GP10, GP9, GP8, GP7 |
| Switches SW1-SW3 | GP4, GP5, GP6 |
| Encoder A / B | TX (GPIO43) / RX (GPIO44) |
| LED data | GP3 |
| LED power | 5V |

## Files

- `PCB/` KiCad project (schematic, board, custom touch-key footprint)
- `PCB/production/` Gerber zip, BOM and positions for JLCPCB
- `firmware/code.py` KMK firmware
- `BOM.csv` parts list with prices and links

## Firmware setup

1. Install CircuitPython for the Waveshare ESP32-S3-Zero.
2. Copy the `kmk` folder from [KMK](https://github.com/KMKfw/kmk_firmware) and the `adafruit_midi` library onto the board.
3. Copy `firmware/code.py` onto the board.
4. Don't touch the keys while it boots: the touch pads calibrate at startup.

## Credits

Based on [Kai Pereira's MIDI keypad tutorial](https://github.com/KaiPereira/MIDI-Keypad).
