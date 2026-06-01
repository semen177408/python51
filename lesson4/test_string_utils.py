import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты позитивные
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("Skypro", "Skypro"),  # с заглавной
    ("s", "S"),  # один символ
    ("привет", "Привет"),  # на кириллице
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Тесты негативные
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("?hello", "?hello"),  # с спецсимвол в начале
    ("123", "123"),  # только цифры
    ("   test", "   test"),  # с пробелом в начале
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Тесты на граничные случаи
@pytest.mark.edge
def test_capitalize_none():
    with pytest.raises(AttributeError):  # или другое ожидаемое исключение
        string_utils.capitalize(None)


@pytest.mark.edge
def test_capitalize_long_string():
    long_str = "a" * 1000
    expected = "A" + "a" * 999
    assert string_utils.capitalize(long_str) == expected


# Позитивные тесты
@pytest.mark.positive
def test_trim_positive():
    assert string_utils.trim("   hello") == "hello"  # Пробелы только в начале
    assert string_utils.trim("hello") == "hello"  # Нет пробелов в начале
    # Пробелы в начале и внутри (удалиться только в начале)
    assert string_utils.trim("   hello world") == "hello world"
    assert string_utils.trim("") == ""  # Пустая строка
    assert string_utils.trim("     ") == ""  # Только пробелы
    assert string_utils.trim(" hello") == "hello"  # Один пробел в начале


# Негативные тесты
@pytest.mark.negative
def test_trim_negative():
    # Пробелы в конце (не должны удалять)
    assert string_utils.trim("hello   ") == "hello   "
    # Пробелы в начале и конце
    assert string_utils.trim("   hello   ") == "hello   "
    # Табуляция вместо пробела (не обрабатывается)
    assert string_utils.trim("\thello") == "\thello"
    # Смешанные пробелы и табуляции в начале
    assert string_utils.trim(" \t hello") == "\t hello"
    with pytest.raises(Exception):
        string_utils.trim(None)  # None вместо строки (должен вызывать ошибку)
    with pytest.raises(Exception):
        string_utils.trim(123)  # Число вместо строки (должен вызывать ошибку)


# Позитивные тесты (6 шт) - ожидаем True
@pytest.mark.positive
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S")  # Символ в начале строки
    assert string_utils.contains("SkyPro", "y")  # Символ в середине строки
    assert string_utils.contains("SkyPro", "o")  # Символ в конце строк
    # Несколько одинаковых символов
    assert string_utils.contains("abracadabra", "a")
    assert string_utils.contains("Hello World", " ")  # Символ - пробел
    assert string_utils.contains("abc123", "2")  # Символ - цифра


# Негативные тесты (6 шт) - ожидаем False
@pytest.mark.negative
def test_contains_negative():
    assert not string_utils.contains("SkyPro", "U")  # Символ отсутствует
    assert not string_utils.contains("", "a")  # Пустая строка
    assert not string_utils.contains("SkyPro", "s")  # Разные регистры
    assert not string_utils.contains("Hello", "$")  # Спецсимвол отсутствует
    assert not string_utils.contains("SkyPro", "PRO")  # Строка вместо символа
    assert not string_utils.contains("", "&")  # Пустая строка и пустой символ


# Позитивные тесты (6 шт.)
@pytest.mark.positive
def test_delete_symbol_positive():
    # Удаление одного символа в середине строки
    result = string_utils.delete_symbol("SkyPro", "k")
    assert result == "SyPro"
    # Удаление подстроки из нескольких символов
    result = string_utils.delete_symbol("SkyPro", "Pro")
    assert result == "Sky"
    # Удаление символа в начале строки
    result = string_utils.delete_symbol("Hello world", "H")
    assert result == "ello world"
    # Удаление символа в конце строки
    result = string_utils.delete_symbol("Hello world", "d")
    assert result == "Hello worl"
    # Удаление символа, встречающегося несколько раз
    result = string_utils.delete_symbol("abracadabra", "a")
    assert result == "brcdbr"
    # Удаление подстроки, равной всей строке
    result = string_utils.delete_symbol("Hello", "Hello")
    assert result == ""


# Негативные тесты (6 шт.)
@pytest.mark.negative
def test_delete_symbol_negative():
    result = string_utils.delete_symbol("", "a")  # Передача пустой строки
    assert result == ""  # Ничего не удаляется, возвращается пустая строка
    # Передача пустого символа для удаления
    result = string_utils.delete_symbol("Hello", "")
    assert result == "Hello"  # Пустая строка не заменяется
    # Удаление символа, которого нет в строке
    result = string_utils.delete_symbol("Hello", "x")
    assert result == "Hello"  # Строка не меняется

    result = string_utils.delete_symbol("123456", "3")  # Строка из цифр
    assert result == "12456"
    # Специальные символы в строке
    result = string_utils.delete_symbol("Hello!@#$World", "!")
    assert result == "Hello@#$World"
    # Пробельные символы
    result = string_utils.delete_symbol("Hello world Python", " ")
    assert result == "HelloworldPython"
