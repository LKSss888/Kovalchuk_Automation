from sqlalchemy import create_engine
from config import Config

def test_connection():
    try:
        print("Пытаемся подключиться к БД...")
        print(f"URL: {Config.SQLALCHEMY_DATABASE_URI}")
        
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        with engine.connect() as connection:
            result = connection.execute("SELECT version()")
            print("✅ Подключение успешно!")
            print(f"Версия PostgreSQL: {result.scalar()}")
            
            # Проверим пользователя
            result = connection.execute("SELECT current_user")
            print(f"Текущий пользователь: {result.scalar()}")
            
            # Проверим базы данных
            result = connection.execute("SELECT datname FROM pg_database WHERE datistemplate = false")
            print("Доступные базы данных:")
            for row in result:
                print(f"  - {row[0]}")
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        print("Проверьте данные в config.py")

if __name__ == "__main__":
    test_connection()