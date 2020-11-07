##
##pythonbuch.com/gui.html
##


from tkinter import *
from datetime import date

begriff="Haus"
sprache= "Deutsch - Englisch"
version="2.0"

def antwort_action():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        richtig_label.config(text="Antwort ist richtig")
    else:
        entry_text = "Antwort ist nicht richtig. "
        richtig_label.config(text=entry_text)



x=date.today()
aktDatum=x.strftime('%d.%m.%Y')
print(aktDatum)


# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
#def button_action():
#    anweisungs_label.config(text="Ich wurde geändert!")


# Ein Fenster erstellen und Größe definieren
fenster = Tk()
fenster.geometry("500x200")

# Den Fenstertitle erstellen
fenster.title("Vokabeltrainer Deutsch-Englisch - Englisch-Deutsch")

# Label erstellen
versions_label = Label(fenster,text="Version:" + version)
datums_label = Label(fenster, text='Datum: '+aktDatum)
#uhrzeit_label = Label(fenster, text="Uhrzeit: ")
frage_label = Label(fenster, text='Frage: '+sprache)
frage_begriff_label = Label(fenster, text=begriff, fg="red")
frage_begriff_label["font"] = "Calibri 20 bold"

antwort_label= Label(fenster, text="Deine Antwort:")
eingabefeld = Entry(fenster, bd=5, width=20)
richtig_label= Label(fenster)


eingabe_button = Button(fenster, text="Klick me", command=antwort_action())
exit_button= Button(fenster, text="Beenden ",command=fenster.quit)
versions_label.grid(row=0, column=0, sticky=W)
datums_label.grid(row= 0, column=1,sticky=W, padx=50)
#uhrzeit_label.grid(row = 0, column=2,padx=30)
frage_label.grid(row = 2, column= 0,pady=10)
frage_begriff_label.grid(row=2, column=1,sticky=W, padx=50)
antwort_label.grid(row = 3, column= 0,sticky=W)
eingabefeld.grid(row=3, column=1, sticky=W,padx=50)


#frage_begriff_label.grid(row=2, column=0)

eingabe_button.grid(row=6, column=1, pady=10, sticky=W, padx=50)
exit_button.grid(row= 6, column= 2, sticky=W)
richtig_label.grid(row=5,column=1, sticky=W, padx=50)




# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()