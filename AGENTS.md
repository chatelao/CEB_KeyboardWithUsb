# Tooling
- Use the KiCAD 10.0 prerelease

# CI/CD

## Github workflow
- Run the full testsuite with github CI/CD workflows
- Run the same toolset locally during development, replace the GH actions if needed

## On every push on every branch
- Verify schematics with erc
- Verify boards with drc

## On every release
- Generate all schematics als .pdf
- Generate all boards als .pdf
