import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def copy_txtName_into_lblMessage():
    lblMessage = builder.get_object('lblMessage')
    txtName = builder.get_object('txtName')
    name = txtName.get_text()
    if name:
        lblMessage.set_text("Your name is " + name)
    else:
        lblMessage.set_text("Please, tell me your name")

class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()
    
    def on_btnChangeMessage_clicked(self, button):
        copy_txtName_into_lblMessage()
    
    def on_txtName_activate(self, entry):
        copy_txtName_into_lblMessage()
    
    def on_btnQuit_clicked(self, button):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("win.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()