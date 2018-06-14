import numpy as np

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

        self.sommets = noms_sommets.copy()

        #init des valeurs des sommets à 0
        i = 0
        while i < nb_sommets:
            self.sommets_value.append(0)
            i = i + 1

    #afficher la matrice avec format sans virgule pour les nombres entiers
    def afficher(self):

        #afficher ligne labelle
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
        self.sommets_value[0] = 0
        i = 1
        while(i < self.nb_sommets):
            self.sommets_value[i] = value
            i = i + 1

    def get_chemin_maximum(self):
        # la difficulté rencontrée ici était la gestion des retours dans le cas ou le sommet successeur
        # est d'un indice inférieur à l'indice courant. Il ne faut pas qu'a chaque fois qu'il rencontre ce cas, il fasse un retour.
        # sinon l'algorithme boucle.
        # Nous avons donc utilisé un tableau de booléens initialisé à False et dont la valeur de l'indice passe à True
        # quand nous devons revenir en arrière la première fois.
        
        self.init_sommets_value(0)       
        n = self.nb_sommets
        retour = n*[False]
            
                        
        i = 0
        while (i < n ):
            xi=self.sommets[i]
            xj=self.successeur(xi)
            k = 0
            while (k < len(xj)):
                #print("le(s) successeur(s) de ",xi, " : ", xj[k])
                #print("la valeur de l'arc est :",self.get_arc_value(xi,xj[k]))
                #print("valeur du sommet",xi,  " : ",self.get_sommet_value(xi))
                #print("valeur du sommet",xj[k], " : ",self.get_sommet_value(xj[k]))
                if self.get_sommet_value(xj[k]) - self.get_sommet_value(xi) < self.get_arc_value(xi,xj[k]):
                    self.set_sommet_value(xj[k], self.get_sommet_value(xi) + self.get_arc_value(xi,xj[k]))
                j = self.get_ind_sommet(xj[k])
                #print (i)
                #print (j)
                k =k+1
                if j<i and retour[i]==False:
                    k=len(xj) # pour sortir du while
                    retour[i] = True
                    #print("Etat du tableau des retours : ", retour)
                    i=j-1
            i=i+1
        
        i = 0
        while (i < n ):
            xi=self.sommets[i]
            print("valeur du sommet",xi,  " : ",self.get_sommet_value(xi))
            i = i+1
        print("----------------------- MAXI -------------------------------")

    def get_chemin_minimum(self):
         # la difficulté rencontrée ici était la gestion des retours dans le cas ou le sommet successeur
        # est d'un indice inférieur à l'indice courant. Il ne faut pas qu'a chaque fois qu'il rencontre ce cas, il fasse un retour.
        # sinon l'algorithme boucle.
        # Nous avons donc utilisé un tableau de booléens initialisé à False et dont la valeur de l'indice passe à True
        # quand nous devons revenir en arrière la première fois.
        
        self.init_sommets_value(1000)       
        n = self.nb_sommets
        retour = n*[False]
            
                        
        i = 0
        while (i < n ):
            xi=self.sommets[i]
            xj=self.successeur(xi)
            k = 0
            while (k < len(xj)):
                #print("le(s) successeur(s) de ",xi, " : ", xj[k])
                #print("la valeur de l'arc est :",self.get_arc_value(xi,xj[k]))
                #print("valeur du sommet",xi,  " : ",self.get_sommet_value(xi))
                #print("valeur du sommet",xj[k], " : ",self.get_sommet_value(xj[k]))
                if self.get_sommet_value(xj[k]) - self.get_sommet_value(xi) > self.get_arc_value(xi,xj[k]):
                    self.set_sommet_value(xj[k], self.get_sommet_value(xi) + self.get_arc_value(xi,xj[k]))
                j = self.get_ind_sommet(xj[k])
                #print (i)
                #print (j)
                k =k+1
                if j<i and retour[i]==False:
                    k=len(xj) # pour sortir du while
                    retour[i] = True
                    #print("Etat du tableau des retours : ", retour)
                    i=j-1
            i=i+1
        
        i = 0
        while (i < n ):
            xi=self.sommets[i]
            print("valeur du sommet",xi,  " : ",self.get_sommet_value(xi))
            i = i+1
        print("----------------------- MINI -------------------------------")
    def get_path(self):
        n = self.nb_sommets
        i = n-1
        path =[]
        while (i >= 0 ):
            xi=self.sommets[i]
            xj=self.predecesseur(xi)
            if xi=="x0":
                path.append(xi)
                break
            k = 0
            while (k < len(xj)):
                #print("le(s) predecesseur(s) de ",xi, " : ", xj[k])
                #print("la valeur de l'arc est :",self.get_arc_value(xj[k],xi))
                #print("valeur du sommet",xi,  " : ",self.get_sommet_value(xi))
                #print("valeur du sommet",xj[k], " : ",self.get_sommet_value(xj[k]))
                if self.get_sommet_value(xi)==self.get_sommet_value(xj[k]) + self.get_arc_value(xj[k],xi):
                    j = self.get_ind_sommet(xj[k])
                    #print ("on passe par", xi)
                    path.append(xi)
                    i = j+1
                    k=len(xj)
                k =k+1
            

            i=i-1
        i=len(path)-1
        while (i >= 0):
            print(path[i])
            i = i-1
        
        
      
# def graphes sommets
G = Graphe_np(8,["x0", "x1","x2","x3","x4","x5","x6", "x7"])
# def arcs
G.add_arcs([["x0","x1"],["x0","x2"],["x0","x3"]])
G.add_arcs([["x1","x4"],["x1","x5"]])
G.add_arcs([["x2","x1"],["x2","x3"],["x2","x5"]])
G.add_arcs([["x3","x6"]])
G.add_arcs([["x4","x7"]])
G.add_arcs([["x5","x4"],["x5","x6"],["x5","x7"]])
G.add_arcs([["x6","x7"]])

# init valeur sommets à - infini !EXCEPTION pour le t0, initialisé à 0 !
#G.init_sommets_value(-1000)

# init valeur arcs
G.set_arc_value("x0","x1",5)
G.set_arc_value("x0","x2",2)
G.set_arc_value("x0","x3",4)
G.set_arc_value("x1","x4",5)
G.set_arc_value("x1","x5",3)
G.set_arc_value("x2","x1",4)
G.set_arc_value("x2","x3",3)
G.set_arc_value("x2","x5",7)
G.set_arc_value("x3","x6",6)
G.set_arc_value("x4","x7",3)
G.set_arc_value("x5","x4",2)
G.set_arc_value("x5","x6",3)
G.set_arc_value("x5","x7",12)
G.set_arc_value("x6","x7",5)

#affichages
#G.afficher()
#print("arcs value",G.arcs_value)
#print("sommets value",G.sommets_value)
G.get_chemin_maximum()
G.get_path()
G.get_chemin_minimum()
G.get_path()


