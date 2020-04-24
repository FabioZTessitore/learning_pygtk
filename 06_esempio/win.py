import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class Handler:
    def __init__(self):
        self.lblMessaggio = builder.get_object('lblMessaggio')
        self.buffer = self.lblMessaggio.get_buffer()
        self.rossoTag = self.buffer.create_tag('rosso_bg', foreground="red")
        self.verdeTag = self.buffer.create_tag('verde_bg', foreground="green")
        self.bluTag = self.buffer.create_tag('blu_bg', foreground="blue")
        self.neroTag = self.buffer.create_tag('nero_bg', foreground="black")
        self.grassettoTag = self.buffer.create_tag('grassettoTag', weight=Pango.Weight.BOLD)
        self.corsivoTag = self.buffer.create_tag('corsivoTag', style=Pango.Style.ITALIC)
        self.sottolineatoTag = self.buffer.create_tag('sottolineatoTag', underline=Pango.Underline.SINGLE)

    def on_destroy(self, *args):
        Gtk.main_quit()

    def on_cmdVisualizza_clicked(self, button):
        txtNome = builder.get_object('txtNome')
        nome = txtNome.get_text()
        txtMessaggio = builder.get_object('txtMessaggio')
        messaggio = txtMessaggio.get_text()

        if nome and messaggio:
            self.buffer.set_text(nome + ': ' + messaggio)
        else:
            self.buffer.set_text('Niente da dire')
        self.lblMessaggio.set_buffer(self.buffer)

    def on_cmdCancella_clicked(self, button):
        txtNome = builder.get_object('txtNome')
        txtNome.set_text('')
        txtNome.grab_focus()
        txtMessaggio = builder.get_object('txtMessaggio')
        txtMessaggio.set_text('')
        self.buffer.set_text('')
        self.lblMessaggio.set_buffer(self.buffer)
        

    def on_cmdStampa_clicked(self, button):
        print('Stampa')

    def on_cmdEsci_clicked(self, button):
        self.on_destroy(button)

    def on_optRosso_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.rossoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.rossoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
    
    def on_optVerde_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.verdeTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.verdeTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_optBlu_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.bluTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.bluTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_optNero_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.neroTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.neroTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_chkGrassetto_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.grassettoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.grassettoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_chkSottolineato_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.sottolineatoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.sottolineatoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    def on_chkCorsivo_toggled(self, button):
        if button.get_active():
            self.buffer.apply_tag(self.corsivoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())
        else:
            self.buffer.remove_tag(self.corsivoTag, self.buffer.get_start_iter(), self.buffer.get_end_iter())

    
builder = Gtk.Builder()
builder.add_from_file("win.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()