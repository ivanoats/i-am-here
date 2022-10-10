
# I am here

A menubar app that keeps the mouse moving on your computer 

- to watch a movie without the screensaver turning on
- to read a long article
- to show others you are still there.

## Authors

Developed by Ivan Storck
- [@ivanoats on github](https://www.github.com/ivanoats)
- [@ivanoats on linkedin](https://www.linkedin.com/ivanoats)

## Development Dependencies

- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [Py2App](https://py2app.readthedocs.io/en/latest/index.html)
- [Rumps](https://rumps.readthedocs.io/en/latest/)


## Run Locally

Clone the project:

```bash
  git clone https://github.com/ivanoats/i-am-here.git
```

Go to the project directory:

```bash
  cd i-am-here
```

Install dependencies:

```bash
  python3 -m pip install -r requirements.txt
```

Start the app in development mode:

```bash
  python3 i-am-here.py
```

or build the app with alias mode:

```bash
python3 setup.py py2app -A
```


## Build and Install

Build the app with:

```bash
  python3 setup.py py2app 
```

Install the app (MacOS) with:

```bash
  cp -r dist/i-am-here.app /Applications
```

Then allow accessibilty in system preferences.

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
