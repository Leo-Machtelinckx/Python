a=int(input("Rentrez une première longueur."))
b=int(input("Rentrez une deuxième longueur."))
c=int(input("Rentrez une troisième longueur."))
if a+c>b and a+b>c and b+c>a:
    hypoténuse=max(a,b,c)
    if (a*a)+(b*b)==(hypoténuse*hypoténuse) or (b*b)+(c*c)==(hypoténuse*hypoténuse) or (c*c)+(a*a)==(hypoténuse*hypoténuse):
        print("Le triangle est rectangle")
    if a==b!=c or b==c!=a or a==c!=b:
        print("Le triangle est isocèle.")
    if a==b==c:
        print("Le triangle est équilatérale.")
else:
    print("Le triangle est quelconque.")
    