import codecs

def createFolder(x):
    with codecs.open(x,"w",encoding="utf-8") as folder:
        print("-"*30)
        firstNote = input("İlk notunu gir.. ")
        print("-"*30,"\n")
        folder.write(firstNote)

def appendNote(x):
    print("-"*30)
    newNote = input("Yeni notunu ekle.. ")
    print("-"*30,"\n")
    newNote = "\n"+newNote
    with codecs.open(x,"a",encoding="utf-8") as note:
        note.write(newNote)

def viewNotes(x):
    with codecs.open(x,"r",encoding="utf-8") as viewNotes:
        notes = viewNotes.readlines()
        count = 1
        for i in notes:
            print("-"*30,"\n")
            print(str(count)+". Not: ",i)
            count+=1
            print("-"*30,"\n")