import uuid

GRID = 2.54

def g(units):
    return round(units * GRID, 2)

def get_uuid():
    return str(uuid.uuid4())

HEADER = """(kicad_sch
  (version 20240702)
  (generator "Jules")
  (uuid "{uuid_root}")
  (paper "A4")
"""

LIB_SYMBOLS_START = """  (lib_symbols
"""

LIB_SYMBOLS_END = """  )
"""

FOOTER = """)
"""

SYM_R = """    (symbol "Device:R" (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (symbol "R_0_1"
        (rectangle (start -1.27 -0.635) (end 1.27 0.635) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "R_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 3.81 0 180) (length 2.54)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
"""

SYM_C = """    (symbol "Device:C" (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (property "Value" "C" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (symbol "C_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "C_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 3.81 0 180) (length 2.54)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
"""

SYM_D_SPICE = """    (symbol "Device:D" (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (property "Value" "D" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (symbol "D_0_1"
        (polyline (pts (xy -1.27 1.27) (xy -1.27 -1.27) (xy 1.27 0) (xy -1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
        (polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "D_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54)
          (name "A" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 3.81 0 180) (length 2.54)
          (name "K" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
"""

SYM_NE555 = """    (symbol "Timer:NE555" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (property "Value" "NE555" (at 0 0 0) (effects (font (size 1.27 1.27))))
      (symbol "NE555_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "NE555_1_1"
        (pin power_in line (at -7.62 2.54 0) (length 2.54)
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin input line (at -7.62 0 0) (length 2.54)
          (name "TRIG" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin output line (at -7.62 -2.54 0) (length 2.54)
          (name "OUT" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin input line (at -7.62 -5.08 0) (length 2.54)
          (name "RESET" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
        (pin input line (at 7.62 -5.08 180) (length 2.54)
          (name "CTRL" (effects (font (size 1.27 1.27))))
          (number "5" (effects (font (size 1.27 1.27))))
        )
        (pin input line (at 7.62 -2.54 180) (length 2.54)
          (name "THRES" (effects (font (size 1.27 1.27))))
          (number "6" (effects (font (size 1.27 1.27))))
        )
        (pin input line (at 7.62 0 180) (length 2.54)
          (name "DIS" (effects (font (size 1.27 1.27))))
          (number "7" (effects (font (size 1.27 1.27))))
        )
        (pin power_in line (at 7.62 2.54 180) (length 2.54)
          (name "VCC" (effects (font (size 1.27 1.27))))
          (number "8" (effects (font (size 1.27 1.27))))
        )
      )
    )
"""

def create_instance(lib_id, ref, value, x, y):
    return f"""  (symbol
    (lib_id "{lib_id}")
    (at {x} {y} 0)
    (unit 1)
    (in_bom yes)
    (on_board yes)
    (uuid "{get_uuid()}")
    (property "Reference" "{ref}" (at {x} {y-2} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{value}" (at {x} {y+2} 0) (effects (font (size 1.27 1.27))))
  )
"""

def create_label(name, x, y):
    return f"""  (label "{name}" (at {x} {y} 0)
    (effects (font (size 1.27 1.27)) (justify left bottom))
    (uuid "{get_uuid()}")
  )
"""

COMPONENTS = [
    {"ref": "U1", "lib": "Timer:NE555", "val": "NE555", "pos": (40, 40), "pins": {
        1: "GND", 2: "THRES", 3: "OUT", 4: "VCC",
        5: "CTRL", 6: "THRES", 7: "DIS", 8: "VCC"
    }},
    {"ref": "R1", "lib": "Device:R", "val": "68k", "pos": (20, 20), "pins": {
        1: "VCC", 2: "DIS"
    }},
    {"ref": "R2", "lib": "Device:R", "val": "68k", "pos": (20, 30), "pins": {
        1: "DIS", 2: "THRES"
    }},
    {"ref": "D1", "lib": "Device:D", "val": "1N4148", "pos": (30, 30), "pins": {
        1: "THRES", 2: "DIS"
    }},
    {"ref": "C1", "lib": "Device:C", "val": "10uF", "pos": (20, 40), "pins": {
        1: "THRES", 2: "GND"
    }},
    {"ref": "C2", "lib": "Device:C", "val": "10nF", "pos": (60, 40), "pins": {
        1: "CTRL", 2: "GND"
    }},
    {"ref": "R3", "lib": "Device:R", "val": "1k", "pos": (70, 20), "pins": {
        1: "VCC", 2: "LED1_A"
    }},
    {"ref": "D2", "lib": "Device:D", "val": "LED_Green", "pos": (70, 30), "pins": {
        1: "LED1_A", 2: "OUT"
    }},
    {"ref": "R4", "lib": "Device:R", "val": "1k", "pos": (70, 50), "pins": {
        1: "OUT", 2: "LED2_A"
    }},
    {"ref": "D3", "lib": "Device:D", "val": "LED_Red", "pos": (70, 60), "pins": {
        1: "LED2_A", 2: "GND"
    }},
]

def get_pin_pos(comp_pos, lib, pin_num):
    x, y = g(comp_pos[0]), g(comp_pos[1])
    if lib == "Device:R" or lib == "Device:C" or lib == "Device:D":
        if pin_num == 1: return round(x - 3.81, 2), y
        if pin_num == 2: return round(x + 3.81, 2), y
    elif lib == "Timer:NE555":
        # Fixed Y direction
        if pin_num == 1: return round(x - 7.62, 2), round(y - 2.54, 2)
        if pin_num == 2: return round(x - 7.62, 2), y
        if pin_num == 3: return round(x - 7.62, 2), round(y + 2.54, 2)
        if pin_num == 4: return round(x - 7.62, 2), round(y + 5.08, 2)
        if pin_num == 5: return round(x + 7.62, 2), round(y + 5.08, 2)
        if pin_num == 6: return round(x + 7.62, 2), round(y + 2.54, 2)
        if pin_num == 7: return round(x + 7.62, 2), y
        if pin_num == 8: return round(x + 7.62, 2), round(y - 2.54, 2)
    return x, y

def main():
    content = HEADER.format(uuid_root=get_uuid())
    content += LIB_SYMBOLS_START
    content += SYM_R
    content += SYM_C
    content += SYM_D_SPICE
    content += SYM_NE555
    content += LIB_SYMBOLS_END

    for comp in COMPONENTS:
        content += create_instance(comp["lib"], comp["ref"], comp["val"], g(comp["pos"][0]), g(comp["pos"][1]))
        for pin_num, net_name in comp["pins"].items():
            px, py = get_pin_pos(comp["pos"], comp["lib"], pin_num)
            content += create_label(net_name, px, py)

    content += FOOTER

    with open("myproject.kicad_sch", "w") as f:
        f.write(content)

if __name__ == "__main__":
    main()
