print("entrer seconde dans le jour (86400) ")
Seconde_dans_le_jour = float(input())
print("entrer la periode de modulo ")
Seconde_periode = float(input())
div = Seconde_dans_le_jour / Seconde_periode
print ("Val Div", div);
dmod = divmod(Seconde_dans_le_jour , Seconde_periode)
print ("Val Mod", dmod);
divint = Seconde_dans_le_jour // Seconde_periode
print ("Val Mod", divint);
divrest = Seconde_dans_le_jour % Seconde_periode
print ("Val Mod", divrest);
