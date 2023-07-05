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
        self.__site = data.get('site')
        self.__name = data.get('name')
        self.__url = data.get('url')
        self.__area = data.get('area')
        self.__employer = data.get('employer')
        self.__salary = data.get('salary')
        self.__published_time = data.get('published_time')

    def __str__(self):
        return f'{self.__site}: {self.__name}\n{self.__url}'

    def __repr__(self):
        return f'{self.__class__.__name__}(site={self.__site}, name={self.__name}, url={self.__url}, ' \
               f'args={self.__area}, employer={self.__employer}, salary={self.__salary}, ' \
               f'published_time={self.__published_time})'

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
