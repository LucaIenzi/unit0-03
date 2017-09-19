import ui

def hello_world_english_touch_up_inside(sender):
	view['hello_world_lable'].text = ("hello world")
def hello_world_freanch_touch_up_inside(sender):
	view['hello_world_lable'].text = ("bon vinue mondre")
def hello_world_italin_touch_up_inside(sender):
	view['hello_world_lable'].text = ("bonjorno tute tera")
		
view = ui.load_view()
view.present('sheet')
