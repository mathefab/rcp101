import numpy as np

class Pile:
    def __init__(self):
        self.liste = []

    def push(self, element):
        self.liste.append(element)

    def pop(self):
        return self.liste.pop()

    # Y a t 'il des éléments dans la pile
    def isEmpty(self):
        if len(self.liste) == 0:
            return 1
        return 0
    
    # effacer la pile
    def clear(self):
        self.liste.clear()

    # obtenir le dernier élément sans le retirer de la pile 
    def last(self):
        return self.liste[len(self.liste) - 1]

    def afficher(self):
        print("Pile :",self.liste)

#afficher la matrice avec format sans virgule pour les nombres entiers
def matbin_afficher(mat, n):

    i = 0
    print("  ", end = '')
    while i < n:
        print("--", end = '')
        i = i + 1
    print("-")
       
    i = 0
    for l in mat:
        print('|', end = '')
        is_debut = 1
        for e in l:
            if is_debut == 1:
                is_debut = 0
            else:
                print(' ', end='')

            print (int(e), end='')
            
        print('|')
        i = i  + 1

    i = 0
    print("  ", end = '')
    while i < n:
        print("--", end = '')
        i = i + 1
    print("-")


class Graphe_np:
    def __init__(self, nb_sommets, noms_sommets):
        self.sommets = []
        self.arcs = []

        self.sommets_value = []
        self.arcs_value = []
        
        self.matrice = np.zeros( (nb_sommets,nb_sommets), dtype=np.bool_ )
        self.nb_sommets = nb_sommets

        #ajout d'une pile
        self.pile = Pile()

        #ajout liste sommets pré-visite et post-visite
        self.previsite = []
        self.postvisite = []

        self.sommets = noms_sommets.copy()

        #init des valeurs des sommets à 0
        i = 0
        while i < nb_sommets:
            self.sommets_value.append(0)
            self.previsite.append(0)
            self.postvisite.append(0)
            i = i + 1

    #afficher la matrice avec format sans virgule pour les nombres entiers
    def afficher(self):

        #afficher ligne label
        i = 0
        print("  ",  end = '')
        while i < self.nb_sommets:
            print(" ", self.sommets[i], sep = '', end = '')
            
            i = i + 1
        print("")

        i = 0
        print("  ", end = '')
        while i < self.nb_sommets:
            print("--", end = '')
            i = i + 1
        print("-")
           
        i = 0
        for l in self.matrice:
            print(self.sommets[i], '|', end = '')
            is_debut = 1
            for e in l:
                if is_debut == 1:
                    is_debut = 0
                else:
                    print(' ', end='')

                print (int(e), end='')

            print('|')
            i = i  + 1

        i = 0
        print("  ", end = '')
        while i < self.nb_sommets:
            print("--", end = '')
            i = i + 1
        print("-")

    # obtenir l'indice d'un sommet depuis son nom
    def get_ind_sommet(self, label):
        i = 0
        while i < self.nb_sommets:
            if self.sommets[i] == label:
                return i
            i = i + 1
        return -1
            
    #ajouter un arc depuis le nom de 2 sommets
    def add_arc(self, label_sommet1, label_sommet2):
        i = 0
        ind_s1 = self.get_ind_sommet(label_sommet1)
        ind_s2 = self.get_ind_sommet(label_sommet2)

        self.arcs.append([self.sommets[ind_s1],self.sommets[ind_s2]])
        self.matrice[ind_s1][ind_s2] = True
        # ajout value à l'arc
        self.arcs_value.append(0)

    # ajouter une liste d'arcs [["A","B"],["A","C"],...]
    def add_arcs(self, liste_arcs):
        for arc in liste_arcs:
            self.add_arc(arc[0], arc[1])

    

    # recherche d'une boucle sur un sommet dans le graphe
    def is_boucle(self):
        M = self.matrice
        n = self.nb_sommets
        
        i = 0
        while (i < n):
            if M[i][i] == True:
                return 1
            i = i + 1
        return 0

    # successeur d'un nom de sommet
    def successeur(self, label_sommet):
        M = self.matrice
        n = self.nb_sommets
        ind = self.get_ind_sommet(label_sommet)

        liste = []
        
        i = 0
        while (i < n ):
            if (M [ind][i] == True ):
                #print(i)
                liste.append(self.sommets[i])
            i = i + 1
        return liste
        
    # predecesseur d'un nom de sommet
    def predecesseur(self, label_sommet):
        M = self.matrice
        n = self.nb_sommets
        ind = self.get_ind_sommet(label_sommet)

        liste = []
                             
        i = 0
        while (i < n ):
            if (M [i][ind] == True):
                #print(i)
                liste.append(self.sommets[i])
            i = i + 1

        return liste

    def fermeture_tran(self):
        #ajout matrice diagonale
        mi = self.matrice.copy()
        i = 0
        while i < self.nb_sommets:
            mi[i][i] = True
            i = i + 1
            
        if self.nb_sommets > 1:
            mi_p = mi.dot(mi)
            print("puissance ", 2 );
            matbin_afficher(mi_p,self.nb_sommets)

            i = 3
            while(i < self.nb_sommets):
                mi_p = mi.dot(mi_p)
                print("puissance ", i );
                matbin_afficher(mi_p,self.nb_sommets)
                i = i + 1

            return mi_p

        else:
            return mi

    def get_arc_indice(self, label_sommet1, label_sommet2):
        i = 0
        find = False
        while i < len(self.arcs):
            if(self.arcs[i][0]==label_sommet1 and self.arcs[i][1]==label_sommet2):
                find = True
                break
            i = i + 1
        
        if find == True:
            return i
        else:
            return -1

    def set_arc_value(self, label_sommet1, label_sommet2, value):
        i = self.get_arc_indice(label_sommet1,label_sommet2)
        if i == -1:
            return False

        self.arcs_value[i] = value
        return True
    
    def get_arc_value(self, label_sommet1, label_sommet2):
        i = self.get_arc_indice(label_sommet1,label_sommet2)
        if i == -1:
            return False

        return self.arcs_value[i] 
        return True

    def set_sommet_value(self, label_sommet, value):
        i = self.get_ind_sommet(label_sommet)
        if i == -1:
            return False

        self.sommets_value[i] = value
        return True

    def get_sommet_value(self, label_sommet):
        i = self.get_ind_sommet(label_sommet)
        if i == -1:
            return False

        return self.sommets_value[i] 

    def init_sommets_value(self, value):
        i = 0
        while(i < self.nb_sommets):
            self.sommets_value[i] = value
            i = i + 1

    # obtenir le prochain sommet non visité
    # retourne le nom du sommet
    #   ou False si aucun sommet non visité
    def get_sommets_non_visite(self):
        i = 0
        while(i < self.nb_sommets):
            if self.sommets_value[i] != 0:
                i = i + 1
            else:
                return self.sommets[i]
        return False

    def parcours_profondeur(self):
        self.pile.clear()

        #initialisation du graphe parcours en profondeur
        GP = Graphe_np(self.nb_sommets,self.sommets)
        
        #initialisation des indices
        indice_pre_visite = 1
        indice_post_visite = 1

        s = self.get_sommets_non_visite()
        while s != False:
            self.set_sommet_value(s, 1)

            # ordre previsite
            i = self.get_ind_sommet(s)
            self.previsite[i] = indice_pre_visite 
            indice_pre_visite = indice_pre_visite + 1
            
            print("sommet previsité s :", s)
            self.pile.push(s)

            while self.pile.isEmpty() != 1:
                x = self.pile.last()
                self.pile.afficher()

                #print("sommet x :", s)

                # recherche du 1er successeur de x non visité
                successeur_x = self.successeur(x)
                print("successeur de ", x, ":", successeur_x)
                print ("etat sommets: ", self.sommets)
                print ("etat sommets: ", self.sommets_value)
              
                
                is_successeur_non_visite = False
                if len(successeur_x) > 0:
                    for y in successeur_x:
                        #print("  successeur :",  y)
                        # 1er sommet non visité
                        if self.get_sommet_value(y) == 0:
                            print("sommet ", x, ',' ,"1er sommet successeur non visité :",  y, "pré-visité")
                            # ordre previsite
                            i = self.get_ind_sommet(y)
                            self.previsite[i] = indice_pre_visite 
                            indice_pre_visite = indice_pre_visite + 1
                            self.set_sommet_value(y, 1)

                            self.pile.push(y)
                            is_successeur_non_visite = True
                            break

                if is_successeur_non_visite == False:
                    # supprimer x de la pile
                    print("post visite de ", x)
                    self.pile.pop()

                    # ordre postvisite
                    i = self.get_ind_sommet(x)
                    self.postvisite[i] = indice_post_visite 
                    indice_post_visite = indice_post_visite + 1

                    #si z  sommet en haut de pile
                    # alors backtrack de x vers z
                    # l'arc (z,x) existe dans le graphe résultant du parcours en profondeur
                    if self.pile.isEmpty() != 1:
                        z = self.pile.last()
                        print("graphe profondeur ajout de l'arc: (",z,",",x,")")
                        GP.add_arc(z,x)



            # boucler s'il existe encore des sommets non visité   
            s = self.get_sommets_non_visite()

        print("Ordre pré-visite :", self.previsite)
        print("Ordre post-visite :", self.postvisite)

        print("Graphe parcours en profondeur")
        GP.afficher()
        return (GP)
    
    def get_composante_fortement_connexes(self):
        
        n = self.nb_sommets
        inv_matrice = self.matrice.copy()
        # tableau des post visite en copie
        max_postvisite = self.postvisite.copy()
        # tableau constructeur du nouvel ordre des sommets
        # on crée un tableau des sommets à parcourir à partir des postvisit du premier
        # parcours en profondeur
        sommets_ord = []
        comp_connexe = []

       # une premiere double boucle pour déterminer l'ordre des sommets à traiter
        i = 0    
        while i < n:
            maximum = max(max_postvisite)
            j=0
            while j<n:
                if maximum == max_postvisite[j]:
                    print("Le max est : ", maximum)
                    print ("pour le sommet : ", self.sommets[j])
                    max_postvisite[j] = 0
                    sommets_ord.append(self.sommets[j])
                    
                j = j+1
            i=i+1

        # Affichage de vérifications
       
        print(self.sommets)
        print("Ordre pré-visite :", self.previsite)
        print("Ordre post-visite :", self.postvisite)
        print("tableau des maximums :", max_postvisite)
        print("Nouvel ordre des sommets", sommets_ord)

        # on créer un graphe : avec le nouvel ordre des sommets
        Ginv = Graphe_np(self.nb_sommets,sommets_ord)

        # une deuxième double boucle pour intervertir les valeurs de la matrice
        i = 0
        
        while i < n:
            j = 0
            while j < n:
                    #intervertion valeur des lignes et colonnes pour obtenir une matice
                    inv_matrice[j,i]=int(self.matrice[i,j])
                    j=j+1
            i = i + 1
            
        # une troisième double boucle pour créer les arcs
        i = 0

        while i < n:
            j = 0
            while j < n:
                    if inv_matrice[i,j]==True:
                        # si inv matrice = 1 alors faire un arc...
                        Ginv.add_arcs([[self.sommets[i], self.sommets[j]]])
                    j=j+1
            i = i + 1
            
        print("--------Voici le graphe inversé---------")
        Ginv.afficher()
        print("--------On lance le parcours en profondeur sur ce graphe inversé-------")
        Gres = Ginv.parcours_profondeur()
        #Cette partie concerne la lecture du résultat du parcours en profondeur
       #un tableau pour récupérer les composantes connexes 2 à 2
        comp_connex = n*[]

        i = 0
        indice = i
        while i < n:

            j = 0
            
            while j < n:
                if Gres.matrice[i][j]==True:
                    comp_connex.append([])
                    comp_connex[indice].append(sommets_ord[i])
                    comp_connex[indice].append(sommets_ord[j])
                    indice = indice + 1
                j = j + 1
            i = i + 1
        
        print("--------Voici les composantes connexes de ce graphe---------") 


        # recherche d'un sommet
        final=n*[]
        i = 0
        indice = i
        #initialisation du tableau final des composantes fortement connexes
        final.append([])
        final[indice].append(comp_connex[i][0])
        final[indice].append(comp_connex[i][1])
        ajoute=True

        
        # on boucle sur les couples de sommets du parcours en profondeur
        # on agglomère les sommets afin de trouver des ensembles de composantes fortement connexes
        while i<len(comp_connex):
            found = False
            lookfor = comp_connex[i][1]
            j=0
           
            while j<len(comp_connex):
                if comp_connex[j][0]==lookfor:
                    found=True
                    if ajoute == False:
                        final.append([])
                        final[indice].append(comp_connex[i][0])
                        final[indice].append(comp_connex[i][1])
                        ajoute=True
                    final[indice].append(comp_connex[j][1])
                j=j+1
            if found == False:
                ajoute = False
                indice = indice+1             
            i = i + 1

        
        i = 0
        indice = i
        
        while i<len (final):
            print("C",indice, " = ",final[i])
            indice = indice + 1
            i = i + 1
        #on termine par afficher les sommets isolés
        print("--------et les sommets isolés---------")
        indice=0
        singleton = True
        while indice < n:
            i=0
            singleton = True
            while i<len (final):
                j=0
                while j<len (final[i]):
                    if sommets_ord[indice]==final[i][j]:
                        singleton=False
                    j = j+ 1
                i= i + 1
            if singleton==True:print("Sommet isolé : ",sommets_ord[indice])
            indice=indice+1

      
# def graphes sommets
G = Graphe_np(8,["A", "B","C","D","E","F","G", "H"])
# def arcs de l'ennoncé
G.add_arcs([["A","B"],["A","C"]])
G.add_arcs([["B","F"]])
G.add_arcs([["F", "C"],["F","G"]])
G.add_arcs([["E","A"],["E","D"]])
G.add_arcs([["D","H"]])
G.add_arcs([["H","D"],["H","G"]])
# pour tester avec un autre graphe
'''G.add_arcs([["A","B"],["A","H"]])
G.add_arcs([["B","C"],["B","D"]])
G.add_arcs([["C", "A"],["C","H"]])
G.add_arcs([["D","C"]])
G.add_arcs([["E","F"]])
G.add_arcs([["F","G"]])
G.add_arcs([["G","D"],["G","E"]])'''

# initialisation des états des sommets à 0
G.init_sommets_value(0)

#affichages
G.afficher()
G.parcours_profondeur()
G.get_composante_fortement_connexes()




