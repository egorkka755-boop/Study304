class UserService:
    def __init__(self):
        self.users = []
    
    def add_user(self, username):
        self.users.append(username)
        return f"Пользователь {username} добавлен"
    
    def get_users(self):
        return self.users

class AuthService:
    def login(self, username, password):
        if username and password:
            return f"Пользователь {username} авторизован"
        return "Ошибка авторизации"
