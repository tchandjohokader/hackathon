import pywhatkit
import speech_recognition as sr
import pyttsx3 as ttx
import datetime
listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')

nb_pan=int(5)
nb_bra=int(5)
nb_mon=int(5)
nb_polo=int(5)
nb_chau=int(5)
def parler(text):
    engine.say(text)
    engine.runAndWait()
parler("Bonjour ;je m'appel çiçi ;et je serai votre assistante vocal ")
parler("Que voulez vous faire;; commander ou autre")
def ecouter():
    try:
        with sr.Microphone() as source:
            print("parler maitenant")
            listener.adjust_for_ambient_noise(source)
            listener.pause_threshold = 0.5
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            command.lower()
    except:
        pass
    return command
def lancer_assistance():
    commande= ecouter()
    print(commande)
    if str(commande) == "commander":
        text='Quelle article voulez-vous?'
        parler(text)
        vanne=ecouter()
        print(vanne)
        if str(vanne) =="une chaussure":
            parler('Quelle marque ; de chaussure  ; voulez vous?')
            type_chaussure=ecouter()
            parler('Quelle couleur ; de chaussure ; voulez vous?')
            couleur=ecouter()
            parler('Quelle est; votre pointure')
            pointure=ecouter()
            parler('combien ; de chaussure ; voulez vous?')
            quantite=ecouter()
            parler('vous voulez ;' + quantite +';'+ 'chaussure de couleur ;' + couleur + 'de pointure ;' + pointure)
            if type_chaussure =="zara" or type_chaussure=="dior" or type_chaussure=="nike" or type_chaussure=="adidas" and quantite <= nb_chau and couleur=="bleu":
                parler("la commande est la")
            else:
                parler("nous ne disposont pas de ce produit")
        elif str(vanne) == "un pantalon":
            parler('Quelle marque ; de pantalon ; voulez vous?')
            type_chaussure=ecouter()
            parler('Quelle couleur ; de pantalon ; voulez vous?')
            couleur = ecouter()
            parler('Quelle taille ; de pantalon ; voulez vous?')
            taille = ecouter()
            parler('combien ; de pantalon ; voulez vous?')
            quantite = ecouter()
            parler('vous voulez ;' + quantite +';'+ 'pantalon de couleur ;' + couleur + 'de taille ;' + taille)
            if type_chaussure =="zara" or type_chaussure=="dior" or type_chaussure=="nike" or type_chaussure=="adidas" and quantite <= nb_chau and couleur=="bleu":
                parler("la commande est la")
            else:
                parler("nous ne disposont pas de ce produit")
        elif str(vanne) == "un polo":
            parler('Quelle marque ; de polo ; voulez vous?')
            type_chaussure = ecouter()
            parler('Quelle couleur ; de polo ; voulez vous?')
            couleur = ecouter()
            parler('Quelle taille ; de polo ; voulez vous?')
            taille = ecouter()
            parler('combien de  ; pantalon ; voulez vous?')
            quantite = ecouter()
            parler('vous voulez ;' + quantite +';'+ 'polo de couleur ;' + couleur + 'de taille ;' + taille)
            if type_chaussure =="zara" or type_chaussure=="dior" or type_chaussure=="nike" or type_chaussure=="adidas" and quantite <= nb_chau and couleur=="bleu" or couleur=="blanc":
                parler("la commande est la")
            else:
                parler("nous ne disposont pas de ce produit")
        elif str(vanne) == "une montre":
            parler('Quelle marque ; de montre ; voulez vous?')
            type_chaussure = ecouter()
            parler('Quelle couleur ; de montre ; voulez vous?')
            couleur = ecouter()
            parler('combien de  ; montre ; voulez vous?')
            quantite = ecouter()
            parler('vous voulez ;' + quantite +';'+ 'montre de couleur ;' + couleur)
            if type_chaussure =="zara" or type_chaussure=="dior" or type_chaussure=="nike" or type_chaussure=="adidas" and quantite <= nb_chau and couleur=="bleu":
                parler("la commande est la")
            else:
                parler("nous ne disposont pas de ce produit")
        elif str(vanne) == "un bracelet":
            parler('Quelle marque ; de bracelet ; voulez vous?')
            type_chaussure = ecouter()
            parler('Quelle couleur ; de bracelet ; voulez vous?')
            couleur = ecouter()
            parler('combien de  ; bracelet ; voulez vous?')
            quantite = ecouter()
            parler('vous voulez ;' + quantite +';'+ 'bracelet de couleur ;' + couleur)
            if type_chaussure =="zara" or type_chaussure=="dior" or type_chaussure=="casio" or type_chaussure=="rolex" and quantite <= nb_chau and couleur=="bleu" or couleur=="or"\
                    or couleur=="argent":
                parler("la commande est la")
            else:
                parler("nous ne disposont pas de ce produit")
        else:
            parler(' desoler; nous ne disposons pas de cette article')
        if parler() =="nous ne disposont pas de ce produit":
            parler('Quelle est votre nom')
            nom = ecouter()
            parler('ou habitez vous')
            lieu = ecouter()
            parler('Quelle est votre numero de téléphone')
            numero = ecouter()
            parler('Quelle jours voulez vous etre livrais ')
            jour_livre = ecouter()
            parler('voulez vous finaliser votre commande')
            po = ecouter()
            if po == 'oui':
                pywhatkit.playonyt('cinetpay')
            else:
                parler('ok merci beaucoup à une prochaine foi')
        else:
            pass
    else:
        parler('alors je ne pourai pas vous aider car je suis un programme destiné au payement ; ; de facto a la commande')
    return quantite
def prix(pri):
    no=lancer_assistance()
    pric=pri*no
    parler('le prix a payer est'+pric)
lancer_assistance()
prix(2000)