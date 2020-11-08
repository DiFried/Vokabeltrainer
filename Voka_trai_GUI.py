##
##pythonbuch.com/gui.html
##


from tkinter import *
from datetime import date

begriff="Haus"
sprache= "Deutsch - Englisch"
version="1.0"

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

# --------------- Label erstellen -------------------------------
versions_label = Label(fenster,text="Version:" + version)
datums_label = Label(fenster, text='Datum: '+aktDatum)
# ----------------------- Vorgabe: Deutsch oder Englisch -----------------
t1_label = Label(fenster, text='Deutsch', font=' Calibri 15 bold')
# ----------------------- Antowrt: Deutsch oder Englisch -----------------
t2_label = Label(fenster, text='Englisch', font=' Calibri 15 bold')
# ----------------------- Begriff ausgeben -----------------
t3_label = Label(fenster, text=begriff, fg="red", font=' Calibri 20 bold')
# ----------------------- Benutzer Eingabe-Feld ------------------------------
eingabefeld = Entry(fenster, bd=5, width=20)


#t1_label["font"] = "20 bold"

#antwort_label= Label(fenster, text="Deine Antwort:")

richtig_label= Label(fenster, text='')


eingabe_button = Button(fenster, text="Eingabe", command=antwort_action())
exit_button= Button(fenster, text="Beenden ",command=fenster.quit)


#uhrzeit_label.grid(row = 0, column=2,padx=30)

#frage_begriff_label.grid(row=2, column=1,sticky=W, padx=50)
#antwort_label.grid(row = 3, column= 0,sticky=W)



# -------------- Widgets platzieren ------------------------------
versions_label.grid(row=0, column=0, sticky=W, padx=10)
datums_label.grid(row= 0, column=3,sticky=W, padx=10)
#t1_label.grid(row=1, column=0, pady=10, sticky=W, padx=10)
t1_label.grid(row=1, column=1, sticky=W)
t2_label.grid(row=1, column=2, sticky=W)
t3_label.grid(row=2, column=1, sticky=W)
eingabefeld.grid(row=2, column=2, sticky=W)
richtig_label.grid(row=2,column=3, sticky=W, padx=10)

eingabe_button.grid(row=3, column=2, pady=10, sticky=W)
exit_button.grid(row= 3, column= 3, padx= 10,sticky=W)





# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()