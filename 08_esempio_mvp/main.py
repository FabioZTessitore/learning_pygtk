import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class Message:
    def __init__(self, name='', message=''):
        self.name = name
        self.text = message
        self.color = 'red'
        self.bold = False
        self.italic = False
        self.underline = False
    
    def setName(self, name):
        self.name = name
    
    def setMessage(self, message):
        self.text = message

    def setColor(self, color):
        self.color = color

    def getMessage(self):
        if self.name and self.text:
            return self.name + ": " + self.text
        else:
            return 'Niente da dire'

    def getColor(self):
        return self.color

    def setBold(self, bold):
        self.bold = bold
    
    def setItalic(self, italic):
        self.italic = italic

    def setUnderline(self, underline):
        self.underline = underline

class Presenter:
    def __init__(self, view):
        self.view = view
        self.message = Message()

    def setMessage(self, name, message):
        self.message.setName(name)
        self.message.setMessage(message)
        self.view.updateMessage(self.message.getMessage())
        self.view.applyColor(self.message.getColor())
    
    def setColor(self, color):
        self.message.setColor(color)
        self.view.applyColor(self.message.getColor())

    def setBold(self, bold):
        self.message.setBold(bold)
        self.view.applyFontStyle(self.message.bold, self.message.italic, self.message.underline)
    def setItalic(self, italic):
        self.message.setItalic(italic)
        self.view.applyFontStyle(self.message.bold, self.message.italic, self.message.underline)

    def setUnderline(self, underline):
        self.message.setUnderline(underline)
        self.view.applyFontStyle(self.message.bold, self.message.italic, self.message.underline)

class Window:
    def __init__(self):
        self.presenter = Presenter(self)

        builder = Gtk.Builder()
        builder.add_from_file("win.glade")
        builder.connect_signals(self)

        self.lblMessaggio = builder.get_object('lblMessaggio')
        self.buffer = self.lblMessaggio.get_buffer()
        self.rossoTag = self.buffer.create_tag('rosso_bg', foreground="red")
        self.verdeTag = self.buffer.create_tag('verde_bg', foreground="green")
        self.bluTag = self.buffer.create_tag('blu_bg', foreground="blue")
        self.neroTag = self.buffer.create_tag('nero_bg', foreground="black")
        self.grassettoTag = self.buffer.create_tag('grassettoTag', weight=Pango.Weight.BOLD)
        self.corsivoTag = self.buffer.create_tag('corsivoTag', style=Pango.Style.ITALIC)
        self.sottolineatoTag = self.buffer.create_tag('sottolineatoTag', underline=Pango.Underline.SINGLE)
        
        self.txtNome = builder.get_object('txtNome')
        self.txtMessaggio = builder.get_object('txtMessaggio')
        self.chkGrassetto = builder.get_object('chkGrassetto')
        self.chkCorsivo = builder.get_object('chkCorsivo')
        self.chkSottolineato = builder.get_object('chkSottolineato')

        window = builder.get_object("window1")
        window.show_all()
        Gtk.main()

    def on_destroy(self, *args):
        Gtk.main_quit()

    def updateMessage(self, messaggio):
        self.buffer.set_text(messaggio)
        self.lblMessaggio.set_buffer(self.buffer)

    def applyColor(self, color):
        if color == 'red':
            self.buffer.apply_tag(self.rossoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        elif color == 'green':
            self.buffer.apply_tag(self.verdeTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        elif color == 'blue':
            self.buffer.apply_tag(self.bluTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.apply_tag(self.neroTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def applyFontStyle(self, bold, italic, underline):
        if bold:
            self.buffer.apply_tag(self.grassettoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        if italic:
            self.buffer.apply_tag(self.corsivoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        if underline:
            self.buffer.apply_tag(self.sottolineatoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())


    def on_cmdVisualizza_clicked(self, button):
        nome = self.txtNome.get_text()
        messaggio = self.txtMessaggio.get_text()
        self.presenter.setMessage(nome, messaggio)

    def on_cmdCancella_clicked(self, button):
        self.presenter.setMessage('', '')
        self.presenter.setBold(False)
        self.presenter.setItalic(False)
        self.presenter.setUnderline(False)
        self.txtNome.set_text('')
        self.txtMessaggio.set_text('')
        self.txtNome.grab_focus()
        self.chkGrassetto.set_active(False)
        self.chkCorsivo.set_active(False)
        self.chkSottolineato.set_active(False)

    def on_cmdStampa_clicked(self, button):
        print('Stampa')

    def on_cmdEsci_clicked(self, button):
        self.on_destroy(button)

    def on_optRosso_toggled(self, button):
        if button.get_active():
            self.presenter.setColor('red')
        else:
            self.buffer.remove_tag(self.rossoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
    
    def on_optVerde_toggled(self, button):
        if button.get_active():
            self.presenter.setColor('green')
        else:
            self.buffer.remove_tag(self.verdeTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_optBlu_toggled(self, button):
        if button.get_active():
            self.presenter.setColor('blue')
        else:
            self.buffer.remove_tag(self.bluTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_optNero_toggled(self, button):
        if button.get_active():
            self.presenter.setColor('black')
        else:
            self.buffer.remove_tag(self.neroTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_chkGrassetto_toggled(self, button):
        if button.get_active():
            self.presenter.setBold(True)
        else:
            self.presenter.setBold(False)
            self.buffer.remove_tag(self.grassettoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_chkSottolineato_toggled(self, button):
        if button.get_active():
            self.presenter.setUnderline(True)
        else:
            self.presenter.setUnderline(False)
            self.buffer.remove_tag(self.sottolineatoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_chkCorsivo_toggled(self, button):
        if button.get_active():
            self.presenter.setItalic(True)
        else:
            self.presenter.setItalic(False)
            self.buffer.remove_tag(self.corsivoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

Window()