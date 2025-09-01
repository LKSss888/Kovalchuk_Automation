import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import Config
from models import Base

@pytest.fixture(scope='session')
def engine():
    """Фикстура для создания движка БД"""
    return create_engine(Config.SQLALCHEMY_DATABASE_URI)

@pytest.fixture(scope='session')
def tables(engine):
    """Фикстура для создания таблиц"""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture
def db_session(engine, tables):
    """Фикстура для сессии БД с откатом изменений после теста"""
    connection = engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def test_student_data():
    """Тестовые данные студента"""
    return {
        "name": "Иван Иванов",
        "email": "ivan@example.com",
        "age": 20
    }