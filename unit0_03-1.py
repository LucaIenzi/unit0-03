# Created by: luca
# Created on: Aug 2016
# Created for: ICS3U
# This program is the Hello, World program, but with a button

import ui

def hello_world_touch_up_inside(sender):
	view['hello_world_lable'].text = ("hello world")

view = ui.load_view()
view.present('sheet')
