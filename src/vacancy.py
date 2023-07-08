class Vacancy:
    """
    Класс для описания вакансии
    """
    __slots__ = ('__site', '__name', '__url', '__area', '__employer', '__salary', '__published_time')

    def __init__(self, data: dict):
        """
        Конструктор для создания экземпляра класса Vacancy
        Args:
            data: dict: Отформатированные данные о вакансии от сервиса поиска вакансий
        Attributes:
            site: str
            name: str
            url: str
            area: str
            employer: str
            salary: int
            published_time: str
        """

        if isinstance(data.get('name'), str) and isinstance(data.get('url'), str) \
                and isinstance(data.get('area'), str) and isinstance(data.get('employer'), str) \
                and isinstance(data.get('published_at'), str) and isinstance(data.get('salary'), int):
            self.__site = data.get('site')
            self.__name = data.get('name')
            self.__url = data.get('url')
            self.__area = data.get('area')
            self.__employer = data.get('employer')
            self.__salary = data.get('salary')
            self.__published_time = data.get('published_at')
        else:
            raise TypeError("Не верный тип входных данных")

    def __str__(self) -> str:
        return f'{"-"*100}\n' \
               f'Сервис поиска: {self.__site}\n' \
               f'Вакансия: {self.__name}\n' \
               f'Работодатель: {self.__employer}\n' \
               f'Зарплата: {self.__salary}\n' \
               f'Город: {self.__area}\n' \
               f'Ссылка: {self.__url}\n' \
               f'Дата публикации: {self.__published_time}\n' \
               f'{"-"*100}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(site={self.__site}, name={self.__name}, url={self.__url}, ' \
               f'args={self.__area}, employer={self.__employer}, salary={self.__salary}, ' \
               f'published_time={self.__published_time})'

    def __lt__(self, other) -> bool:
        return self.__salary <= other.__salary

    def __gt__(self, other) -> bool:
        return self.__salary >= other.__salary

    @property
    def site(self):
        return self.__site

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def area(self):
        return self.__area

    @property
    def employer(self):
        return self.__employer

    @property
    def salary(self):
        return self.__salary

    @property
    def published_time(self):
        return self.__published_time
