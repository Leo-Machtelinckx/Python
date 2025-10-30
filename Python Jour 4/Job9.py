def moyenne(note1,note2,note3):
    moyenne_etudiant=(note1+note2+note3)/3
    if moyenne_etudiant>=15:
        print("Très bon élève")
    elif moyenne_etudiant>=11:
        print("Bon élève!")
    elif moyenne_etudiant>=8:
        print("Élève moyen")
    elif moyenne_etudiant>=0:
        print("Élève devant faire des efforts")
note1=float(input("Insérez une première note."))
note2=float(input("Insérez une deuxième note."))
note3=float(input("Insérez une troisième note."))
moyenne(note1,note2,note3)
