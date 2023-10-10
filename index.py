import modul_note as note

print("\n+-- NOT DEFTERİM --+\n")
fname = input("Dosya adı girin.. ")
fname = fname+".txt"
note.createFolder(fname)
while True:
    action = int(input(""" Yapmak istediğiniz işelemi seçin
    1 - Not Ekle
    2 - Notlarım 
    """))
    if action == 1:
        note.appendNote(fname)
    elif action == 2:
        note.viewNotes(fname)
        