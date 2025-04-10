class Utilisateur():

    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.forums = []

    
    def __str__(self):
        return f"Utilisateur(id={self.id}, username='{self.username}')"
