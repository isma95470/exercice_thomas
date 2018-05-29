# exercice_thomas
repo exercice

from random import randrange
from math import ceil
credits = 1000
print("Bienvenue au Zcasino ! Vos credits sont de 1000$")

while credits > 0:
    mise = input("Combien souhaitez vous miser : ")
    mise = int(mise)
    num_joueur = input("Veuillez misez sur un numero : ")
    num_joueur = int(num_joueur)
    num_gagnant = randrange(50)
    print("la roulette tourne ... et s'arrete sur le ",num_gagnant , "!!")
    
    if num_joueur == num_gagnant:
        mise = mise * 3
        credits = credits + mise
        print("Vous gagnez : ", mise ,"Vous avez desormais : ", credits)
    
    elif num_joueur % 2 == 0 and num_gagnant % 2 == 0:
        mise = ceil(mise) * 0.5
        credits = credits + mise
        print("Meme couleur, vous gagnez : ", mise , "Vous avez desormais : ", credits)
        
    else:
        credits = credits - mise
        print("Vous perdez : ",mise , "Vous avez desormais : ", credits)

else:
    print("Vous etes ruiné")
