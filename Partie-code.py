

pricing = input("quelle pricing a utilisé 1  ")
if pricing == "1":
    print("Je suis content de l'entendre !")
    html_pricing = generate_pricing_1 
else:
    print("Je suis désolé de l'apprendre. html_pricing ")


mood = input("quelle nav_bar a utilisé 1 a 11 ")
# Affichage deS la réponse
if mood == "1":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_1() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "2":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_2() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")

# Affichage de la réponse
if mood == "3":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_3() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "4":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_4() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "5":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_5() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "6":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_6() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "7":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_7() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "8":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_8() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "9":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_9() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")



# Affichage de la réponse
if mood == "10":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_10() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")



# Affichage de la réponse
if mood == "11":
    print("Je suis content de l'entendre !")
    html_nav = generate_nav_11() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")



heros = input("quelle heros a utilisé 1 a  3 ")
# Affichage deS la réponse
if heros == "1":
    print("Je suis content de l'entendre !")
    html_heros = generate_heros_1() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if heros == "2":
    print("Je suis content de l'entendre !")
    html_heros = generate_heros_2() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if heros == "3":
    print("Je suis content de l'entendre !")
    html_heros = generate_heros_3() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


features = input("quelle nav_bar a utilisé 1 a 4 ")
# Affichage deS la réponse
if features == "1":
    print("Je suis content de l'entendre !")
    html_features = generate_features_1() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if features == "2":
    print("Je suis content de l'entendre !")
    html_features = generate_features_2() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if features == "3":
    print("Je suis content de l'entendre !")
    html_features = generate_features_3() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if features == "4":
    print("Je suis content de l'entendre !")
    html_features = generate_features_4() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# ------------------------------------------------ réponse 0-----------------------
#                                                            debut
# ------------------------------------------------ réponse 0-----------------------

 
# Affichage deS la réponse
if features == "0":
    print("Je suis content de l'entendre !")
    html_features = "   "
else:
    print("Je suis désolé de l'apprendre. features == 0 ?")

# Affichage de la réponse
if mood == "0":
    print("Je suis content de l'entendre !")
    html_nav = "     " 
else:
    print("Je suis désolé de l'apprendre. mood == 0 ?")

 # Affichage deS la réponse
if heros == "0":
    print("Je suis content de l'entendre !")
    html_heros = "    " 
else:
    print("Je suis désolé de l'apprendre. mood == 0 ?")


if pricing == "0":
    print("Je suis content de l'entendre !")
    html_pricing = generate_pricing_1 
else:
    print("Je suis désolé de l'apprendre. html_pricing ")


# ------------------------------------------------ réponse 0-----------------------
#                                                            fin
# ------------------------------------------------ réponse 0-----------------------


#----------------------------------------- partie initialitation des valeurs ---------------- 
#                   debut
#----------------------------------------- partie initialitation des valeurs ---------------- 


doctype = generate_doctype()
body = generate_body_one()
header = generate_header() 
footer = generate_footer("Copyright©2023")

#----------------------------------------- partie initialitation des valeurs ---------------- 
#                   fin
#----------------------------------------- partie initialitation des valeurs ---------------- 



#----------------------------------------- partie finale des valeurs ---------------- 
#                   debut
#----------------------------------------- partie finale des valeurs ---------------- 
html_up =  html_pricing 
htmlp =  html_heros + html_features + html_up    

# Affichage de la réponse
if mood == "5":
    print("Je suis content de l'entendre !")
    nav = generate_nav_5() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "6":
    print("Je suis content de l'entendre !")
    nav = generate_nav_6() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "7":
    print("Je suis content de l'entendre !")
    nav = generate_nav_7() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "8":
    print("Je suis content de l'entendre !")
    nav = generate_nav_8() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")


# Affichage de la réponse
if mood == "9":
    print("Je suis content de l'entendre !")
    nav = generate_nav_9() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")



# Affichage de la réponse
if mood == "10":
    print("Je suis content de l'entendre !")
    nav = generate_nav_10() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")



# Affichage de la réponse
if mood == "11":
    print("Je suis content de l'entendre !")
    nav = generate_nav_11() 
else:
    print("Je suis désolé de l'apprendre. Est-ce que tu veux en parler ?")
