#!/usr/bin/env python3
import rumps
import pyautogui

APP_NAME = "I am here"
INTERVAL = 5

class IAmHereApp(rumps.App):
    def __init__(self):
        super(IAmHereApp, self).__init__(APP_NAME)
        self.app = rumps.App(APP_NAME)
        self.timer =rumps.Timer(self.on_tick, INTERVAL)
        self.set_up_menu()
        self.timer.start()

    @rumps.clicked("About")
    def about(self):
        rumps.alert(title=APP_NAME, message="I am here"f"\nDeveloped by Ivan Storck\nversion: 0.0.1", ok=None, cancel=None)

    # @rumps.clicked("Quit")
    # def quit(self, _):
    #   rumps.quit_application()

    def set_up_menu(self):
        self.app.title = "⏰"
        self.menu = ["About", "Quit"]

    def on_tick(self, sender):
      pyautogui.moveRel(0, 10)

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = IAmHereApp()
    app.run()
