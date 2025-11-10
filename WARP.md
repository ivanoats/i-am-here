# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Python-based macOS menubar application that keeps the mouse moving at regular intervals to prevent screensavers from activating. It's a single-file application built with Rumps (Ridiculously Uncomplicated macOS Python Statusbar apps) and PyAutoGUI.

## Development Commands

### Setup

```bash
# Install dependencies (use Python 3)
python3 -m pip install -r requirements.txt
```

### Running

```bash
# Run in development mode
python3 i-am-here.py

# Build in alias mode (faster for development, creates symlink to source)
python3 setup.py py2app -A
```

### Building & Installing

```bash
# Build standalone app bundle
python3 setup.py py2app

# Install to Applications folder
cp -r dist/i-am-here.app /Applications
```

Note: After installation, you must grant Accessibility permissions in System Preferences for PyAutoGUI to control the mouse.

## Architecture

### Core Components

**Single-file application** (`i-am-here.py`):

- `IAmHereApp`: Main application class inheriting from `rumps.App`
- Uses a timer that fires every 5 seconds (`INTERVAL = 5`)
- `on_tick()`: Timer callback that moves mouse 10 pixels down using PyAutoGUI
- Simple menubar with "About" and "Quit" menu items
- Clock emoji (⏰) as menubar icon

### Key Dependencies

- **Rumps**: Manages macOS menubar interface and menu items
- **PyAutoGUI**: Handles mouse movement automation (requires Accessibility permissions)
- **py2app**: Packages Python application as standalone macOS .app bundle

### Important Notes

- The app uses a custom fork of Rumps from GitHub (`jaredks/rumps@master`) rather than PyPI version
- Mouse movement is relative (`pyautogui.moveRel(0, 10)`) not absolute
- Timer runs continuously once started, no pause/stop functionality currently implemented
