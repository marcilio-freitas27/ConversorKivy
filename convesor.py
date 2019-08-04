# -*- coding: utf-8 -*-
# conversor.py

import time
import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget

# conversor.kv

Builder.load_string('''
<Conversor>:
    BoxLayout:
        orientation: 'vertical'
		canvas:
			Color:
				rgb: (0,0,1)
			Rectangle:
				pos: self.pos
				size: self.size
        ActionBar:
            ActionView:
				canvas:
					Color:
						rgb: (0,0,.5)
					Rectangle:
						size: self.size
						pos: self.pos
                ActionPrevious:
                    title:'conv1'
                    on_release:
						root.manager.transition.direction = 'right'
						root.manager.current = 'menu'
				ActionSeparator:
					icon: ''
				ActionButton:
					text: 'info'
					on_press: root.opened(self)
		GridLayout:
			padding: 190
			spacing: 10
			cols: 3

			TextInput:
				id : r
				multline: False
				font_size: 20
			Button:
				text: '='
				on_release:  c.text = str(int(r.text)/10000)
				background_color: [0,0,1,1]
				font_size: 20
			TextInput:
				id : c
				multline: False
				font_size: 20

			TextInput:
				id : rl
				multline: False
				font_size: 20
			Button:
				text: '='
				on_release: cv.text = str(int(rl.text)/1000)
				background_color: [0,0,1,1]
				font_size: 20
			TextInput:
				id : cv
				multline: False
				font_size: 20

			TextInput:
				id : ra
				multline: False
				font_size: 20
			Button:
				text: '='
				on_release:  ca.text = str(int(ra.text)/100)
				background_color: [0,0,1,1]
				font_size: 20
			TextInput:
				id : ca
				multline: False
				font_size: 20

			TextInput:
				id : rb
				multline: False
				font_size: 20
			Button:
				text: '='
				on_release: cb.text = str(int(rb.text)/10)
				background_color: [0,0,1,1]
				font_size: 20
			TextInput:
				id : cb
				multline: False
				font_size: 20

<Conversor1>:
    BoxLayout:
        orientation: 'vertical'
		canvas:
			Color:
				rgb: (0,0,1)
			Rectangle:
				pos: self.pos
				size: self.size
        ActionBar:
            ActionView:
				canvas:
					Color:
						rgb: (0,0,.5)
					Rectangle:
						size: self.size
						pos: self.pos
                ActionPrevious:
                    title:'conv2'
                    on_release:
						root.manager.transition.direction = 'right'
						root.manager.current = 'menu'
				ActionSeparator:
					icon: ''
                ActionButton:
                    minimum_width: '200sp'
                    text:'Info'
                    on_release: root.opened(self)
				ActionSeparator:
					icon: ''
        GridLayout:
			padding: 190
			spacing: 10
			cols: 3

			TextInput:
				id : r
				multline: False
				font_size: 20
			Button:
				text: '='
				on_release: c.text = str(int(r.text)*10000)
				background_color: [0,0,1,1]
				font_size: 20
			TextInput:
				id : c
				multline: False
				font_size: 20

			TextInput:
				id : ra
				multline: False
				font_size: 20
			Button:
				text: '='
				font_size: 20
				on_release: ca.text = str(int(ra.text)*1000)
				background_color: [0,0,1,1]
			TextInput:
				id : ca
				multline: False
				font_size: 20
			
			TextInput:
				id : rb
				multline: False
				font_size: 20
			Button:
				text: '='
				on_release: cb.text = str(int(rb.text)*100)
				background_color: [0,0,1,1]
				font_size: 20
			TextInput:
				id : cb
				multline: False
				font_size: 20

			TextInput:
				id : rc
				multline: False
				font_size: 20
			Button:
				text: '='
				font_size: 20
				on_release: cc.text = str(int(rc.text)*10)
				background_color: [0,0,1,1]
			TextInput:
				id : cc
				multline: False
				font_size: 20
<Inicial>:
	BoxLayout:
		orientation: 'vertical'
		canvas:
			Color:
				rgb: (0,0,1)
			Rectangle:
				pos: self.pos
				size: self.size
		ActionBar:
            ActionView:
				use_separator: True
				canvas:
					Color:
						rgb: (0,0,.5)
					Rectangle:
						size: self.size
						pos: self.pos
                ActionPrevious:
					title: 'Menu'
					app_icon: ''
					with_previous: False

		GridLayout:
			rows : 10
			padding: 50
			spacing: 20
			Button:
				text: 'Conv1'
				on_release:
					root.manager.transition.direction = 'right'
					root.manager.current = 'conv1'

				background_color : [0,0,1,1]
			Button:
				text: 'Conv2'
				on_release:
					root.manager.transition.direction = 'right'
					root.manager.current = 'conv2'
				background_color : [0,0,1,1]
			Button:
				text: 'Configurações'
				on_release: app.open_settings()
				background_color : [0,0,1,1]
			Button:
				text: 'Info'
				on_release: root.opened(self)
				background_color : [0,0,1,1]
			Button:
				text: 'Sair'
				on_release: app.stop()
				background_color : [0,0,1,1]
''')

# conversor.py


class POPup(Popup):
	pass

class Conversor(Screen):

	def opened(self, obj):
		pop = POPup(size = (512, 512), size_hint = (None, None), title = 'Info')
		grid = GridLayout(rows = 4, padding=30, spacing=10)
		button = Label(text='Converson de unidades decimais')
		button.bind()
		grid.add_widget(button)

		pop.add_widget(grid)
		pop.open()

class Conversor1(Screen):

	def opened(self, obj):
		pop = POPup(size = (512, 512), size_hint = (None, None), title = 'Info')
		grid = GridLayout(rows = 4, padding=30, spacing=10)
		button = Label(text='Converson de unidades')
		button.bind()
		grid.add_widget(button)

		pop.add_widget(grid)
		pop.open()

class Inicial(Screen):

	def opened(self, obj):
		pop = POPup(size = (512, 512), size_hint = (None, None), title = 'Info')
		grid = GridLayout(rows = 4, padding=30, spacing=10)
		button = Label(text='Converson de unidades feito com Python e Kivy v 1.0')
		button.bind()
		grid.add_widget(button)

		pop.add_widget(grid)
		pop.open()

sm = ScreenManager()
sm.add_widget(Inicial(name='menu'))
sm.add_widget(Conversor(name='conv1'))
sm.add_widget(Conversor1(name='conv2'))



class APP(App):
    def build(self):
        return sm

APP().run()
