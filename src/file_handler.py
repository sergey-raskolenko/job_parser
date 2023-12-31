from abc import ABC, abstractmethod
import json


class FileHandler(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancies(self, data: list):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_10_highly_paid(self):
        pass

    @abstractmethod
    def get_vacancies_by_area(self, area_input):
        pass

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword):
        pass

    @abstractmethod
    def clear_file(self):
        pass


class JsonHandler(FileHandler):
    """
    Класс для работы с файлом
    """
    def __init__(self):
        self.__filename = "vacancies.json"

    @property
    def filename(self):
        return self.__filename

    def add_vacancies(self, data: list):
        """
        Запись данных о вакансиях в файл
        """
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_vacancies(self) -> list:
        """
        Возвращает все найденные вакансии
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_10_highly_paid(self) -> list:
        """
        Возвращает 10 самых высокооплачиваемых вакансий и перезаписывает их в файл
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        new_data = sorted(data, key=lambda item: item.get('salary'), reverse=True)[:10]
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
        return new_data

    def get_vacancies_by_area(self, area_input) -> list:
        """
        Возвращает список вакансий в определенном городе  и перезаписывает их в файл
        :param area_input: Пользовательский ввод города
        :return: Список вакансий в нужном городе
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        new_data = [item for item in data if item.get('area').lower() == area_input.lower()]
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
        return new_data

    def get_vacancies_by_keyword(self, keyword) -> list:
        """
        Возвращает вакансии в названии которых присутствует ключевое слово  и перезаписывает их в файл
        :param keyword: Пользовательский ввод слова
        :return: Список вакансий с ключевым словом в названии
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        new_data = [item for item in data if keyword.lower() in item.get('name').lower()]
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
        return new_data

    def clear_file(self):
        """
        Очищает файл от записанной ранее информации
        """
        with open(self.__filename, 'w', encoding='utf-8') as file:
            file.write('')
