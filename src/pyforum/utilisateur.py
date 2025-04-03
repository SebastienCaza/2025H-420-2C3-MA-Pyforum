class Utilisateur:
    id_counter = 1  

    def __init__(self, nom_utilisateur, email, mot_de_passe):
        self.id = Utilisateur.id_counter
        Utilisateur.id_counter += 1
        self.nom_utilisateur = nom_utilisateur
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.forums = []  
    
        