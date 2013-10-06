# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #!/usr/bin/python
#
# main.py
# Copyright (C) 2013 CECI <knick@localhost.localdomain>
# 
# Clemente-Client is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Clemente-Client is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk
import os
import sys

# import libraries of directory clemente-client
sys.path.append("../..")

UI_FILE = "clemente_client.ui"
UI_FILE_CONFIG = "config_client.ui"
VALORS = {"ip":"", "port":""}

class GUI_Config:
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE_CONFIG)
		self.builder.connect_signals(self)

		window_config = self.builder.get_object('window1')
		window_config.show_all()
		

	def destroy(window, self):
		Gtk.main_quit()
		
	def on_button_ok_clicked(self,button):
		ip = self.builder.get_object('entry_ip').get_text()
		port = self.builder.get_object('entry_port').get_text()
		if ip is not "" and port is not "":
			VALORS['ip'] = ip
			VALORS['port'] = port
			

class GUI:
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')
		window.show_all()

	def destroy(window, self):
		Gtk.main_quit()
		
	def on_menu_edit_config(self,menu):
		GUI_Config()
		
	def on_menu_view_see_config(self,menu):		
		print "valors: ",VALORS

	def on_menu_server_quit(self,menu):
		exit()

	def on_menu_server_connect(self,menu):
		pass

def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())

