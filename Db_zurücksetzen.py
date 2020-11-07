import sqlite3

conn = sqlite3.connect("Vokabeltrainer.db")
c = conn.cursor()
aufruf = ""


inhalt = ""
c.execute("SELECT * FROM Deutsch_Englisch")
inhalt = c.fetchall()
for i in inhalt:
    num, deutsch, englisch, de_bit, en_bit, ges_bit = i
    de_bit = 0
    en_bit = 0
    ges_bit = 1
    print(num, deutsch, englisch, de_bit, en_bit, ges_bit)
    c.execute("UPDATE Deutsch_Englisch SET DE_bit=?, EN_bit=?, Ges_bit=? WHERE Num=? ", (de_bit, en_bit, ges_bit, num))
    conn.commit()
