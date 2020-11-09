##
##pythonbuch.com/gui.html
##


from tkinter import *
from datetime import date
from functools import partial


begriff="Haus"
a1="house"
sprache= "Deutsch - Englisch"
version="1.0"

def antwort_action(event):
    print(e1.get())
    if (e1.get() == a1):
        antwort='Richtige Antwort.'
        f1='green'
    else:
        antwort='Falsche Antwort.'
        f1='red'
    richtig_label= Label(fenster, text=antwort, fg=f1, font='Calibri, 15 bold').grid(row=2,column=3, sticky=W, padx=10)
    e1.delete(0,END)



x=date.today()
aktDatum=x.strftime('%d.%m.%Y')
print(aktDatum)


# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
#def button_action():
#    anweisungs_label.config(text="Ich wurde geändert!")


# Ein Fenster erstellen und Größe definieren
fenster = Tk()
fenster.geometry("600x200")

# Den Fenstertitle erstellen
fenster.title("Vokabeltrainer Deutsch-Englisch - Englisch-Deutsch")

# --------------- Label erstellen -------------------------------
versions_label = Label(fenster,text="Version:" + version).grid(row=0, column=0, sticky=W, padx=10)
datums_label = Label(fenster, text='Datum: '+aktDatum).grid(row= 0, column=3,sticky=W, padx=10)
# ----------------------- Vorgabe: Deutsch oder Englisch -----------------
t1_label = Label(fenster, text='Deutsch', font=' Calibri 15 bold').grid(row=1, column=1, sticky=W)
# ----------------------- Antowrt: Deutsch oder Englisch -----------------
t2_label = Label(fenster, text='Englisch', font=' Calibri 15 bold').grid(row=1, column=2, sticky=W)
# ----------------------- Begriff ausgeben -----------------
t3_label = Label(fenster, text=begriff, fg="red", font=' Calibri 20 bold').grid(row=2, column=1, sticky=W)
# ----------------------- Benutzer Eingabe-Feld ------------------------------
e1 = Entry(fenster, bd=5, width=20)
e1.grid(row=2, column=2, sticky=W)
# ----------------Cursor im Textfeld positionieren --------------------------------------
e1.focus_set()
#fenster.bind('<Return>', antwort_action())
#button_1.bind("<Button-1>", partial(printInput, name=name))


# -------------------Button erstellen und platziern -----------------------------------
Button(fenster, text="Enter", command=antwort_action).grid(row=3, column=2, pady=10, sticky=W)
Button(fenster, text="Beenden ",command=fenster.quit).grid(row= 3, column= 3, padx= 10,sticky=W)
fenster.bind('<Return>', antwort_action)










# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()