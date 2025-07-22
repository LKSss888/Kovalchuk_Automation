#Задание 1. Решить задачу
#Дано: Реализация класса в файле string_processor.py


class StringProcessor:
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return "."
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith("."):
            processed_text += "."
        return processed_text


# Цель тестирования: Проверить, что метод process класса StringProcessor корректно преобразует входную строку:
# Первая буква строки должна быть заглавной. Если строка не заканчивается точкой, то она должна быть добавлена в конце.
# Создайте минимум 3 позитивных и 2 негативных теста.

# Решение:

import pytest
from string_processor import StringProcessor

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello."),
        ("Hello", "Hello."),
        ("hello world", "Hello world."),
    ],
)
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output