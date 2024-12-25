from database.sqlalchemy_base import Base  # Импорт базового класса для моделей
from .database import database, setup_database, get_session  # Основной класс базы и утилиты
from .models.person import Person  # Импорт модели Person
from .models.program import Program  # Импорт модели Program
from .models.person_program import PersonProgram  # Импорт модели PersonProgram
from .models.personal_info import PersonalInfo  # Импорт модели PersonalInfo

__all__ = [
    "Base",  # Для миграций и определения моделей
    "database",  # Класс для управления подключением
    "setup_database",  # Настройка базы данных для Dispatcher
    "get_session",  # Получение сессии базы данных
    "Person",  # Модель Person
    "Program",  # Модель Program
    "PersonProgram",  # Модель PersonProgram
    "PersonalInfo",  # Модель PersonalInfo
]
