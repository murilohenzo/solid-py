from solid.models.user_lsp import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)