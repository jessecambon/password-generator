#!/usr/bin/python
import gtk
import gtk.glade
import pygtk
import passgen
pygtk.require('2.0')

class window:
	def delete_event(self, widget, event, data=None):
		print "delete_event occured!"
		return False
		
	def destroy(self, widget, data=None):
		print "destroy occured!"
		gtk.main_quit()
		
	def create_pass(self, button):
		"""Creates the password and displays it."""
	
		# Retrieve password length from SpinButton
		length = int(self.spinbutton1.get_value_as_int())
		
		# Configure character selection based on checkboxes
		num, lower, upper, punc = False, False, False, False
		if self.check_num.get_active():
			num=True
		
		if self.check_lower.get_active():
			lower=True
			
		if self.check_upper.get_active():
			upper=True
	
		if self.check_punc.get_active():
			punc=True
		
		blacklist = self.blacklist.get_text().replace(" ", "")

		if "," in blacklist:
			blacklist = "".join(blacklist.split(","))
		
		
		password = passgen.passgen(length, num, lower, upper, punc, blacklist)
		self.pass_display.set_text(password)
		
	def copy_to_clipboard(self, button):
		"""Copies displayed password to clipboard"""
		self.pass_display.select_region(0, -1)
		self.pass_display.copy_clipboard()
	
	def __init__(self):            
		xml = gtk.glade.XML("passgen.glade")
		
		# Import widgets from XML
		self.window = xml.get_widget("window1")
		self.exit_button = xml.get_widget("exit_button")
		self.button1 = xml.get_widget("button1")
		self.check_lower = xml.get_widget("check_lower")
		self.check_upper = xml.get_widget("check_upper")
		self.check_num = xml.get_widget("check_num")
		self.check_punc = xml.get_widget("check_punc")
		self.spinbutton1 = xml.get_widget("spinbutton1")
		self.blacklist = xml.get_widget("blacklist")
		self.pass_display = xml.get_widget("pass_display")
		self.copy_button = xml.get_widget("copy_button")
		
		## sets window icon and shows window
		icon = self.window.render_icon(gtk.STOCK_DIALOG_AUTHENTICATION, gtk.ICON_SIZE_DIALOG)
		self.window.set_icon(icon)
		self.window.show()
		
		# Signal Handling
		self.window.connect("destroy", self.destroy, None)
		self.window.connect("delete_event", self.delete_event)
		self.exit_button.connect("clicked", self.destroy)
		self.button1.connect("clicked", self.create_pass)
		self.copy_button.connect("clicked", self.copy_to_clipboard)
	
	def main(self):
		gtk.main() # main gtk loop
		
w = window()
w.main()
