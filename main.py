liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
listeNageur = []
listeNages = []
commande = ''


def cmd_individu(listeNageur):
    """Ajoute un nouveau najeur"""
    prénom = input("Prénom du nouveau nageur ? ")
    id = len(listeNageur)+1
    listeNageur.append( (id,prénom ))
    print(listeNageur)


def cmd_nouvelle_nage(lsiteNages):
    """Ajoute une nouvelle nage au logiciel"""
    # à continuer



def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    print("liste des nageurs: ", listeNageur)
    a = input("Nageur n° ? ")
    b = input("quelle nage ? ")
    c = input("combien de longueur ? ")
    liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  nage   |  longueur")
    print("---------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print("Performances de ", tmp)
    print("  nage   |  longueur")
    print("--------------------")
    for elt in liste:
        if elt[0]== tmp:
            print(f" {elt[1]:8}|  {elt[2]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quel nage ? ")
    print("Nage ", tmp)
    print(" Nageur     |  longueur")
    print("------------------------")
    for elt in liste:
        if elt[1]== tmp:
            print(f" {elt[0]:11}|  {elt[2]}")

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    else:
        return True

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        tmp = line.split(',')
        liste.append(tuple(tmp))
    fichier.close()



isAlive = True
while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
        continue
    if commande == 'individu':
        cmd_individu(listeNageur)
        continue

    if commande == 'nouvelle nage':
        cmd_nouvelle_nage(listeNages)
        continue

    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == 'nageur':
        cmd_nageur(liste)
        continue

    if commande == 'nage':
        cmd_nage(liste)
        continue

    if commande == 'save':
        cmd_save(liste, 'save.csv')
        continue

    if commande == 'load':
        cmd_load(liste, 'save.csv')
        continue

    if commande == 'exit':
        isAlive = cmd_exit(liste)
        continue

    print(f"Commande {commande} inconnue")