class DatabaseService:
    def connect(self):
        return "Подключение к базе данных установлено"
    
    def disconnect(self):
        return "Подключение закрыто"

class LoggingService:
    def info(self, message):
        print(f"INFO: {message}")
    
    def error(self, message):
        print(f"ERROR: {message}")
