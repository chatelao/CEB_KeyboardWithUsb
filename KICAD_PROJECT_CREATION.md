# Creating a KiCad Project from the Command Line

This document outlines the steps to create a KiCad project from scratch using the command line. This is useful for automating the project creation process and for environments where a graphical user interface is not available.

## Installation

These instructions are for Ubuntu-based systems.

### 1. Add the KiCad PPA

First, you need to add the KiCad PPA to your system to get the latest version of KiCad.

```bash
sudo add-apt-repository ppa:kicad/kicad-9.0-releases
sudo apt update
```

### 2. Install KiCad Nightly

Install the `kicad-nightly` package. We use the nightly version as it's more likely to have the latest `kicad-cli` features.

```bash
sudo apt install kicad-nightly -y
```

**Note:** The installation can take a long time.

### 3. Make `kicad-cli` accessible

The `kicad-cli` binary is not in the default `PATH`. You need to find it and create a symbolic link.

```bash
# Find the location of kicad-cli
find / -name kicad-cli 2>/dev/null

# Create a symbolic link (replace the path with the one you found)
sudo ln -s /usr/lib/kicad-nightly/bin/kicad-cli /usr/bin/kicad-cli
```

### 4. Set the `LD_LIBRARY_PATH`

The `kicad-cli` tool may not be able to find its shared libraries. You need to set the `LD_LIBRARY_PATH` environment variable.

First, find the location of a required library, for example `libkicommon.so.9.0.0`.

```bash
find / -name libkicommon.so.9.0.0 2>/dev/null
```

Then, add the directory to your `LD_LIBRARY_PATH`. You should add this line to your shell's startup file (e.g., `~/.bashrc` or `~/.zshrc`) to make the change permanent.

```bash
export LD_LIBRARY_PATH=/usr/lib/kicad-nightly/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
```

### 5. Verify the installation

Finally, verify that `kicad-cli` is working correctly.

```bash
kicad-cli --version
```

## Project Creation

The `kicad-cli` tool does not currently have a command to create new projects. Therefore, you need to create the project files manually. A minimal KiCad project consists of a `.kicad_pro` file and a `.kicad_sch` file.

### 1. Create the Project File

The project file (`.kicad_pro`) is a JSON file that contains information about the project, such as the board and schematic file names.

Create a file named `myproject.kicad_pro` with the following content:

```json
{
  "board": {
    "title": "myproject",
    "filename": "myproject.kicad_pcb",
    "sch": "myproject.kicad_sch"
  }
}
```

### 2. Create the Schematic File

The schematic file (`.kicad_sch`) is an s-expression file that contains the schematic information.

Create a file named `myproject.kicad_sch` with the following minimal content:

```lisp
(kicad_sch
  (version 20240702)
  (generator "Jules")
  (uuid "00000000-0000-0000-0000-000000000000")
)
```

This creates an empty schematic.

## Adding a Component

To add a component to the schematic, you need to add a `lib_symbols` section and a `symbol` section to the `.kicad_sch` file.

### 1. Define the Symbol in the Library

First, define the symbol in the `lib_symbols` section. This section contains all the symbols used in the schematic. The following example defines a simple resistor symbol.

```lisp
(lib_symbols
  (symbol "Device:R" (in_bom yes) (on_board yes)
    (property "Reference" "R" (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "R" (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "R_0_1"
      (rectangle (start -1.27 -0.635) (end 1.27 0.635)
        (stroke (width 0.254) (type default))
        (fill (type none))
      )
    )
    (symbol "R_1_1"
      (pin passive line (at -2.54 0 0) (length 1.27)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 2.54 0 180) (length 1.27)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
)
```

### 2. Add a Symbol Instance

Next, add an instance of the symbol to the schematic. This places the component on the schematic sheet.

```lisp
(symbol
  (lib_id "Device:R")
  (at 152.4 101.6 0)
  (unit 1)
  (in_bom yes)
  (on_board yes)
  (uuid "00000000-0000-0000-0000-000000000001")
  (property "Reference" "R1" (at 152.4 99.06 0)
    (effects (font (size 1.27 1.27)))
  )
  (property "Value" "1k" (at 152.4 103.52 0)
    (effects (font (size 1.27 1.27)))
  )
)
```

You can add this to your `myproject.kicad_sch` file after the `lib_symbols` section.

## Validation

After creating the schematic, you can validate it using the Electrical Rules Checker (ERC).

```bash
kicad-cli sch erc myproject.kicad_sch
```

This will produce a report file named `myproject-erc.rpt`. You can examine this file to see the results of the ERC.

The output for our example project will look like this:

```
ERC report (2025-11-12T10:52:13+0000, Encoding UTF8)

***** Sheet /
[pin_not_connected]: Pin not connected
    ; error
    @(149.86 mm, 101.60 mm): Symbol R1 Pin 1 [Passive, Line]
[pin_not_connected]: Pin not connected
    ; error
    @(154.94 mm, 101.60 mm): Symbol R1 Pin 2 [Passive, Line]
[lib_symbol_issues]: The current configuration does not include the symbol library 'Device'
    ; warning
    @(152.40 mm, 101.60 mm): Symbol R1 [R]

 ** ERC messages: 3  Errors 2  Warnings 1
```

The errors are expected since the resistor pins are not connected to anything. The warning about the missing 'Device' library can also be ignored for this example. The important thing is that the ERC check ran successfully, which validates the project structure and schematic file format.
