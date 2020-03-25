import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()
    
    def on_btnChangeMessage_clicked(self, button):
        lblMessage = builder.get_object('lblMessage')
        lblMessage.set_text("Hello, World!")
    
    def on_btnQuit_clicked(self, button):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("win.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()