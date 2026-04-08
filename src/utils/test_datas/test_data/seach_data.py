from src.models.search_input import SearchInput

SEARCH_INPUTS = (
    SearchInput('Grey jacket', 'Grey jacket', 'Тест с полным запросом'),
    SearchInput('grey jacket', 'Grey jacket', 'Регистр не важен'),
    SearchInput('  Grey jacket  ', 'Grey jacket', 'Пробелы'),
    SearchInput('Grey jacket!', 'Grey jacket', 'Символы'),
)