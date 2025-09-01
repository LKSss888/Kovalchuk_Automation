class Config:
    # Данные из pgAdmin
    DB_USER = "postgres"          # пользователь
    DB_PASSWORD = ""              # Пароль (если есть)
    DB_HOST = "localhost"         # Обычно localhost
    DB_PORT = "5432"              # Обычно 5432
    DB_NAME = "postgres"          # база данных
    
    # URL для pg8000
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"