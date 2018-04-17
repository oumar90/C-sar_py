# Fonction de chiffrement d'un caractere
def cesar_chiffre_nombre(x,k):
	return (x+k)%26

# Fonction de dechiffrement d'un caractere
def cesar_dechiffre_nombre(x,k):
	return (x-k)%26

# Fonction de chiffrement d'une chaine de caractere
def cesar_chiffre_mot(mot, k):
	mot_chiffre = [] #Liste vide
	for lettre in mot: #pour chaque lettre que tu trouve dans mot
		nombre = ord(lettre) - 65 #convertis le lettre en nombre de 0 à 25 en utilisant le ASCII
		nombre_chiffre = cesar_chiffre_nombre(nombre, k) #on Chiffre le nombre
		lettre_chiffre = chr(nombre_chiffre+65) #on transforme le nombre en chiffre
		mot_chiffre.append(lettre_chiffre) #on stocke le lettre dans la liste
	mot_chiffre= "".join(mot_chiffre) #on revient à la chaine de caractere
	return mot_chiffre #On returne le mot chiffrer

# Fonction de dechiffrement d'une chaine de caractere
def cesar_dechiffre_mot(mot, k):
	mot_dechiffre = [] #Liste vide
	for lettre in mot: #pour chaque lettre que tu trouve dans mot
		nombre = ord(lettre) - 65 #convertis le lettre en nombre de 0 à 25 en utilisant le ASCII
		nombre_dechiffre = cesar_dechiffre_nombre(nombre, k)  #on dechiffre le nombre
		lettre_dechiffre = chr(nombre_dechiffre+65) #on transforme le nombre en chiffre
		mot_dechiffre.append(lettre_dechiffre) #on stocke le lettre dans la liste
	mot_dechiffre= "".join(mot_dechiffre) #on revient à la chaine de caractere
	return mot_dechiffre #On returne le mot dechiffrer

#=====================Programme pricipale======================
if __name__ == '__main__':

	while 1:
	  	print("##################################################################")
	    print("#                                                                #")
	    print("#         Author : Oumar Djimé Ratou                             #")
	    print("#         Algorithme : César                                     #")
	    print("#                                                                #")
	    print("##################################################################")

	    print()

		print("***************************************************************************")
		print("************     Chiffrement et dechiffrement de cesar*********************")
		print("************	 (C) Chiffrement.                       *******************")
		print("************	 (D) Déchiffrement.                     *******************")
		print("************	 (Q) Quitter.                           *******************")
		print("***************************************************************************")
		choix = input("Veillez choisir votre choix :").upper()
		
		if choix == 'C': #Si on choisi 'c' c'est pour chiffrer un message
			print("*************** Vous avez choisi le Chiffrement **************************")
			print()

			message = input("Veillez entrer le message à chiffrer :")
			key     = int(input("Veillez entrer votre clé secrète :"))
			message = message.upper()		

			mot_chiffre = cesar_chiffre_mot(message, key)
		f
			print("le mot {} est chiffrer en {}.".format(message, mot_chiffre))
			
		elif (choix == 'D'): #Si  on choisi 'd' pour dechiffrer un message
			print("**************** Vous avez choisi le Déhiffrement************************")
			print()

			mot_chiffre = input("Veillez entrer le message à déchiffrer :")
			key     = int(input("Veillez entrer votre clé secrète :"))
			mot_chiffre = mot_chiffre.upper()		

			mot_dechiffre = cesar_dechiffre_mot(mot_chiffre, key)

			print("le mot {} est dechiffrer en {}.".format(mot_chiffre, mot_dechiffre))
		else: #Sinon on quitte le programme 
			print("Merci d'avoir esseyer notre Programme, bye bye !!!!!!!")
			break
