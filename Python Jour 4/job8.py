def fonction(type,saison):
    if type=="fruits" and saison=="hiver":
        print("Orange,mandarine et kiwi")
    elif type=="fruits" and saison=="été":
        print("Poire,Fraise,Cassis")
    elif type=="légumes" and saison=="hiver":
        print("carotte,topinambour,endive")
    elif type=="légumes" and saison=="été":
        print("artichaut,aubergine,navet")
    else:
        print("Error!")
fonction("fruits","hiver")