import pytest
from sqlalchemy.exc import IntegrityError
from models import Student

class TestDatabaseOperations:
    """Тесты для операций с базой данных"""
    
    def test_add_student(self, db_session, test_student_data):
        """Тест добавления студента"""
        student = Student(**test_student_data)
        db_session.add(student)
        db_session.commit()
        
        result = db_session.query(Student).filter_by(email=test_student_data["email"]).first()
        assert result is not None
        assert result.name == test_student_data["name"]
    
    def test_update_student(self, db_session, test_student_data):
        """Тест обновления студента"""
        student = Student(**test_student_data)
        db_session.add(student)
        db_session.commit()
        
        student.age = 21
        db_session.commit()
        
        updated_student = db_session.query(Student).filter_by(email=test_student_data["email"]).first()
        assert updated_student.age == 21
    
    def test_soft_delete_student(self, db_session, test_student_data):
        """Тест мягкого удаления студента"""
        from datetime import datetime
        
        student = Student(**test_student_data)
        db_session.add(student)
        db_session.commit()
        
        student.is_active = False
        student.deleted_at = datetime.now()
        db_session.commit()
        
        deleted_student = db_session.query(Student).filter_by(email=test_student_data["email"]).first()
        assert deleted_student.is_active == False