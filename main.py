from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.utils import platform

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

from uix import *

__version__ = "1.0.1"

if platform != "android":
    scale = 40
    Window.size = (9*scale,14*scale)

class MainScreen(Screen):
    pass

class MainScreenInput(Screen):
    pass

class MainScreenLog(Screen):
    pass

class MainScreenAbout(Screen):
    pass

class MainApp(MDApp):
    title_about = f"Tap n Count {__version__}\n created by Aghnat HS"
    total = []
    nominal = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.title = "Tap n Count"
        self.screen = MainScreen()
        
        return self.screen
    
    def on_start(self):
        self.nominal_grid = self.screen.ids.input_screen.ids.nominal_grid
        self.log_lists = self.screen.ids.log_screen.ids.log_lists
        self.screen.ids.tabs.switch_tab("Input")
        self.create_nominal_grid()

    def create_nominal_grid(self):
        for val in self.nominal:
            self.nominal_grid.add_widget(
                NominalButton(
                        text="{:,.0f}".format(val),
                        value=val
                )
            )

        for nominal_button in self.nominal_grid.children:
            nominal_button.on_release = lambda x=nominal_button.value: self.input_nominal(x)

    def input_nominal(self,val):
        self.total.append(val)
        self.log(f"+{val}")

    def reset_nominal(self):
        self.total.clear()
        self.log_lists.clear_widgets()
    
    def sum_nominal(self):
        sums = sum(self.total)
        total = "Total : Rp{:,.0f}".format(sums)
        Snackbar(
                duration=2,
                text=total, 
                snackbar_x=dp(15),
                snackbar_y=dp(10), 
                size_hint_x=(Window.width - (dp(20) * 2)) / Window.width
            ).open()
        self.log(total)
    
    def log(self, text):
        self.log_lists.add_widget(LogList(text=text))


app = MainApp()
app.run()