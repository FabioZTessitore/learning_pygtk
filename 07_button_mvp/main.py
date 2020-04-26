import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Message:
    def __init__(self, message=''):
        self.text = message
    
    def setText(self, message):
        self.text = message

    def getText(self):
        return self.text

class Presenter:
    def __init__(self, view):
        self.view = view
        self.message = Message()

    def setText(self, message):
        self.message.setText(message)
        self.view.updateMessage(self.message.getText())

class Window:
    def __init__(self):
        self.presenter = Presenter(self)

        builder = Gtk.Builder()
        builder.add_from_file("win.glade")
        builder.connect_signals(self)
        
        self.lblMessage = builder.get_object('lblMessage')

        main_window = builder.get_object("window1")
        main_window.show_all()
        Gtk.main()

    def on_destroy(self, *args):
        Gtk.main_quit()
    
    def on_btnChangeMessage_clicked(self, button):
        self.presenter.setText("Hello, World!")

    def updateMessage(self, message):
        self.lblMessage.set_text(message)

Window()