# Birk

CLI tool for backup files and folders.

## Install

```text
pip install git+https://github.com/1b0325h/Birk
```

**Local:**

```text
python setup.py install
```

## Usage

```powershell
# Create backup from source list to save destination.
birk run

# Add a new path to source list.
birk add <ABSOLUTE_PATH>

# Set save destination.
birk set <ABSOLUTE_PATH>

# Remove path from source list.
birk remove

# Lists all source list items and save destination.
birk list

# Destroy all path items.
birk destroy
```
