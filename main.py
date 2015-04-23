#: -*- encoding: utf-8 -*-

import kivy
from kivy.logger import Logger
from kivy.event import EventDispatcher
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from jnius import autoclass
from kivy.properties import StringProperty, ObjectProperty

try:
    Build = autoclass('android.os.Build')
    BuildVERSION = autoclass('android.os.Build$VERSION')
    BuildVERSION_CODES = autoclass('android.os.Build$VERSION_CODES')
except:
    Logger.info('System: Not an Android platform!')
    Build = None
    BuildVERSION = None
    BuildVERSION_CODES = None

kivy.require('1.9.0')

from kivy.app import App


class AppScreenManager(ScreenManager):

    def switch_to_screen(self, screen):
        self.current = screen


class MainScreen(Screen):
    pass


class InfoLabel(GridLayout):

    info_label = StringProperty('')
    info_text = StringProperty('')

class AndroidBuildWrapper(EventDispatcher):

    serial = StringProperty('')
    board = StringProperty('')
    model = StringProperty('')

    def __init__(self, **kwargs):
        super(AndroidBuildWrapper, self).__init__(**kwargs)

        if Build is not None:
            self.serial = Build.SERIAL
            self.board =  Build.BOARD
            self.model = Build.MODEL

class AndroidDeviceInfoApp(App):

    android_build_wrapper = ObjectProperty()

    def __init__(self, **kwargs):
        super(AndroidDeviceInfoApp, self).__init__(**kwargs)
        self.android_build_wrapper = AndroidBuildWrapper()

if __name__ == '__main__':
    AndroidDeviceInfoApp().run()