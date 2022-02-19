from kivy.properties import NumericProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import OneLineListItem
from kivymd.uix.tab import MDTabsBase


class NominalButton(MDRectangleFlatButton):
    
    def __init__(self,value, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = 1
        self.font_size = "18sp"
        self.value = value

class LogList(OneLineListItem):
    text = StringProperty()

class Tab(FloatLayout, MDTabsBase):
    pass