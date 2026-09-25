# Aegis60 KMK Firmware

This is a starter KMK firmware for the Aegis60 (RP2040-ZERO).

## What this includes
- Exact row/column GPIO mapping from the current hardware netlist
- 61-key ANSI-like base layer
- Sparse matrix handling with `KC.NO` for physically empty matrix slots

## Flash steps
1. Install CircuitPython on RP2040-ZERO (if not already installed).
2. Copy the KMK library folder to your `CIRCUITPY` drive.
3. Copy `main.py` from this folder to the root of `CIRCUITPY`.
4. Replug/reset the board.

## Notes
- Matrix diode direction is configured as `COL2ROW`.
- In the schematic/netlist, GP0/GP1 are named `UATRT_TX` / `UART_RX` but are used as matrix rows in this design.
- If any key appears in the wrong place, verify switch orientation and matrix continuity first, then tune keycodes in `main.py`.
