from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen





class MainScreen(Screen): pass



class Interface(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        return MainScreen()




Interface().run() 
