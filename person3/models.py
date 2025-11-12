APP_NAME = "MyApp"
VERSION = "1.0.0"

class BaseModel:
    def __init__(self, id):
        self.id = id
    
    def save(self):
        return f"Объект {self.id} сохранен"
