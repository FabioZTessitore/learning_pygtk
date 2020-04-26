import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Libro:
    def __init__(self):
        pass

    def setQuantita(self, quantita):
        self.quantita = quantita

    def setTitolo(self, titolo):
        self.titolo = titolo

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo


class Presenter:
    def __init__(self, view):
        self.view = view
        self.libro = Libro()

    def reset(self):
        self.acquisto(0, '', 0.)

    def acquisto(self, quantita, titolo, prezzo):
        self.libro.setQuantita(quantita)
        self.libro.setTitolo(titolo)
        self.libro.setPrezzo(prezzo)
        prezzoTotale, sconto, prezzoScontato = self.calcola()
        self.view.update(self.libro.quantita, self.libro.titolo, self.libro.prezzo, prezzoTotale, sconto, prezzoScontato)

    def calcola(self):
        prezzoTotale = self.libro.prezzo * self.libro.quantita
        sconto = prezzoTotale * .15
        prezzoScontato = prezzoTotale - sconto
        return (prezzoTotale, sconto, prezzoScontato)

class Window:
    def __init__(self):
        self.presenter = Presenter(self)

        builder = Gtk.Builder()
        builder.add_from_file("win.glade")
        builder.connect_signals(self)

        self.txtQuantita = builder.get_object('txtQuantita')
        self.txtTitolo = builder.get_object('txtTitolo')
        self.txtPrezzo = builder.get_object('txtPrezzo')
        self.txtPrezzoTotale = builder.get_object('txtPrezzoTotale')
        self.txtSconto = builder.get_object('txtSconto')
        self.txtPrezzoScontato = builder.get_object('txtPrezzoScontato')

        window = builder.get_object("window1")
        window.show_all()
        Gtk.main()

    def update(self, quantita, titolo, prezzo, prezzoTotale, sconto, prezzoScontato):
        self.txtQuantita.set_text(str(quantita))
        self.txtTitolo.set_text(titolo)
        self.txtPrezzo.set_text(str(int(prezzo * 100)/100))
        self.txtPrezzoTotale.set_text(str(int(prezzoTotale*100)/100))
        self.txtSconto.set_text(str(int(sconto*100)/100))
        self.txtPrezzoScontato.set_text(str(int(prezzoScontato*100)/100))
    
    def on_cmdCalcola_clicked(self, button):
        try:
            self.presenter.acquisto(
                int(self.txtQuantita.get_text()),
                self.txtTitolo.get_text(),
                float(self.txtPrezzo.get_text())
            )
        except:
            pass
        
    def on_cmdAzzera_clicked(self, button):
        self.presenter.reset()

    def on_cmdStampa_clicked(self, button):
        print("Stampa")

    def on_destroy(self, *args):
        Gtk.main_quit()

Window()