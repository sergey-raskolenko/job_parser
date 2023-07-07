import os
from abc import ABC, abstractmethod
from datetime import datetime
import requests


class JobsAPI(ABC):
    """
    Абстрактный базовый класс для работы с сервисами поиска работы
    """
    @abstractmethod
    def __init__(self):
        """
        Абстрактный конструктор со значениями входных параметров запроса
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword_input: str) -> list:
        """
        Абстрактный метод для получения списка словарей вакансий
        :param keyword_input: Ключевое слово пользователя для поиска
        :return: Список словарей из вакансий
        """
        pass

    @staticmethod
    @abstractmethod
    def get_formatted_data(item: dict) -> dict:
        """
        Абстрактный статический метод для обработки словаря вакансии и формирования
        нового для вакансии словаря со стандартизированными ключами
        :param item: Словарь вакансии с полной информацией от API
        :return: Словарь с необходимой информацией
        """
        pass


class HeadHunterAPI(JobsAPI):
    """
        Класс, описывающий сервис поиска работы HeadHunter
    """
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies/'
        self.__params = {'per_page': 100, 'area': '113'}

    @staticmethod
    def get_formatted_data(item) -> dict:
        if item.get('salary') is None:
            slr = 0
        elif item.get('salary').get('from'):
            slr = item.get('salary').get('from')

        else:
            slr = 0
        vcn_info = {'site': 'HeadHunter',
                    'name': item.get('name'),
                    'url': item.get('alternate_url'),
                    'employer': item.get('employer').get('name'),
                    'published_at': datetime.fromisoformat(item.get('published_at')).date().strftime("%d/%m/%Y"),
                    'area': item.get('area').get('name'), 'salary': slr
                    }
        return vcn_info

    def get_vacancies(self, keyword_input):
        print(f"Поиск вакансий на HeadHunter по кодовому слову: {keyword_input} ")
        self.__params['text'] = f'name:{keyword_input.lower()}'
        response = requests.get(self.__url, params=self.__params).json()
        self.__params['page'] = 0
        vacancy_list = []
        while self.__params.get('page') != response.get('pages'):
            response = requests.get(self.__url, params=self.__params).json()
            for item in response.get('items'):
                vacancy_list.append(self.get_formatted_data(item))
            print('.', end='')
            self.__params['page'] += 1
        else:
            print('')
        return vacancy_list


class SuperJobAPI(JobsAPI):
    """
    Класс, описывающий сервис поиска работы SuperJob
    """
    def __init__(self):
        self.__url = 'https://api.superjob.ru/2.0/vacancies'
        self.__params = {"count": 100}
        self.__headers = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}

        # "keyword": 'python',

    @staticmethod
    def get_formatted_data(item) -> dict:
        if item.get('payment_from') not in (None, ''):
            slr = item.get('payment_from')
        else:
            slr = 0
        vcn_info = {'site': 'SuperJob',
                    'name': item.get('profession'),
                    'url': item.get('link'),
                    'employer': item.get('client').get('title'),
                    'published_at': datetime.fromtimestamp(item.get('date_published')).strftime("%d/%m/%Y"),
                    'area': item.get('town').get('title'), 'salary': slr
                    }
        return vcn_info

    def get_vacancies(self, keyword_input):
        print(f"Поиск вакансий на SuperJob по кодовому слову: {keyword_input} ")
        vacancy_list = []
        self.__params["keyword"] = {keyword_input.lower()}
        for i in range(5):
            self.__params['page'] = i
            print('.', end='')
            rsp = requests.get(self.__url, headers=self.__headers, params=self.__params).json()
            for item in rsp.get('objects'):
                vacancy_list.append(self.get_formatted_data(item))
        else:
            print('')
        return vacancy_list
