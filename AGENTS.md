# Agent Instructions

This document outlines the rules and conventions that should be followed by any agent working on this repository.

## KiCad Project Validation

All KiCad projects in this repository must pass both Electrical Rule Checking (ERC) and Design Rule Checking (DRC). These checks are enforced by a GitHub Actions workflow that runs on every push to every branch.

### Running the Checks Locally

To run the checks locally, you can use the `kicad-cli` tool.

First, ensure you have KiCad installed and the `kicad-cli` tool is in your `PATH`. You may also need to set the `LD_LIBRARY_PATH` environment variable. Refer to the `KICAD_PROJECT_CREATION.md` document for detailed installation instructions.

Once your environment is set up, you need to identify the main project file (`.kicad_pro`), the schematic file (`.kicad_sch`), and the PCB file (`.kicad_pcb`). You can find the schematic and PCB filenames inside the `.kicad_pro` file, which is in JSON format.

After identifying the correct filenames, you can run the checks from the root of the repository:

```bash
# Replace <schematic_file> with the actual schematic filename
kicad-cli sch erc <schematic_file>

# Replace <pcb_file> with the actual PCB filename
kicad-cli pcb drc <pcb_file>
```

The output of these commands will be written to `.rpt` files. You should review these files for any errors or warnings.
