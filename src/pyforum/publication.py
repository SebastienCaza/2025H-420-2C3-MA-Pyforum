class Publication:
    def __init__(self, id, titre, contenu, auteur_id, forum_id):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.auteur_id = auteur_id
        self.forum_id = forum_id
        self.commentaires = []

    def ajouter_commentaire(self, commentaire):
        self.commentaires.append(commentaire)

    def __str__(self):
        return f"Publication(id={self.id}, titre='{self.titre}', contenu='{self.contenu}', auteur_id={self.auteur_id}, forum_id={self.forum_id})"