import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Ordine:
    prezzo = {
        'cappuccino': 2000,
        'espresso': 1500,
        'latte': 1000,
        'freddo': 3000
    }
    percentServizio = .08

    def __init__(self):
        self.quantita = 0
        self.bevanda = 'cappuccino'
        self.servizio = False

class ListaOrdini:
    def __init__(self):
        self.ordini = []
        self.totaleParziale = 0
        self.totale = 0
        self.servizio = 0

    def add(self, ordine):
        self.ordini.append(ordine)
        self.totaleParziale += ordine.curImportoArticolo
        if ordine.servizio:
            self.servizio = self.totaleParziale * Ordine.percentServizio
        self.totale = self.totaleParziale + self.servizio

class Presenter:
    def __init__(self, view):
        self.view = view
        self.ordine = Ordine()
        self.listaOrdini = ListaOrdini()

    def setServizio(self, servizio):
        self.ordine.servizio = servizio

    def calcola(self, quantita):
        self.ordine.quantita = quantita
        curPrezzo = Ordine.prezzo[self.ordine.bevanda]
        self.ordine.curImportoArticolo = curPrezzo * quantita
        self.listaOrdini.add(self.ordine)
        self.view.update(self.ordine.curImportoArticolo, self.listaOrdini.totaleParziale, self.listaOrdini.servizio, self.listaOrdini.totale)


class Window:
    def __init__(self):
        self.presenter = Presenter(self)

        builder = Gtk.Builder()
        builder.add_from_file("win.glade")
        builder.connect_signals(self)

        self.txtQuantita = builder.get_object('txtQuantita')
        self.txtImportoArticolo = builder.get_object('txtImportoArticolo')
        self.txtTotaleParziale = builder.get_object('txtTotaleParziale')
        self.txtServizio = builder.get_object('txtServizio')
        self.txtTotale = builder.get_object('txtTotale')
        self.chkServizio = builder.get_object('chkServizio')

        self.infoDialog = builder.get_object('dlgInfo')

        self.window = builder.get_object("window1")
        self.window.show_all()
        Gtk.main()

    def on_destroy(self, *args):
        Gtk.main_quit()
    
    def on_cmdCalcola_clicked(self, button):
        quantita = self.txtQuantita.get_text()
        try:
            quantita = int(quantita)
            self.presenter.calcola(quantita)
        except ValueError:
            dialog = Gtk.MessageDialog(parent=self.window, flags=0, message_type=Gtk.MessageType.ERROR, buttons=Gtk.ButtonsType.CLOSE, text="Quantità deve essere un intero")
            dialog.run()
            dialog.destroy()
            self.txtQuantita.grab_focus()

    def on_cmdAzzera_clicked(self, button):
        self.presenter.calcola(0)
        self.txtQuantita.set_text('')
        self.txtQuantita.grab_focus()
        self.txtImportoArticolo.set_text('')
        self.chkServizio.set_active(False)

    def on_chkServizio_toggled(self, button):
        if button.get_active():
            self.presenter.setServizio(True)
        else:
            self.presenter.setServizio(False)
    
    def on_mnuColore_activate(self, menuItem):
        def color_activated(dialog):
            color = dialog.get_rgba()
            # deprecated
            self.txtTotaleParziale.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(*color))
        
        dialog = Gtk.ColorChooserDialog(title="Scegli un colore", parent=self.window)
        if dialog.run() == Gtk.ResponseType.OK:
            color_activated(dialog)
        dialog.destroy()
    
    def on_mnuInfo_activate(self, menuItem):
        self.infoDialog.run()
        self.infoDialog.hide()

    def update(self, importoArticolo, totaleParziale, servizio, totale):
        self.txtImportoArticolo.set_text(str(importoArticolo))
        self.txtTotaleParziale.set_text(str(totaleParziale))
        self.txtServizio.set_text(str(servizio))
        self.txtTotale.set_text(str(totale))

    def on_cmdInfoOK_clicked(self, button):
        pass

Window()