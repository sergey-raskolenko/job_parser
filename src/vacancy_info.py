from abc import ABC, abstractmethod


class VacancyInfo(ABC):
    """
    Абстрактный базовый клас для получения информации о вакансии
    """
    @abstractmethod
    def get_name(self):
        """Абстрактный метод для получения имени вакансии"""
        pass

    @abstractmethod
    def get_url(self):
        """Абстрактный метод для получения адреса вакансии"""
        pass

    @abstractmethod
    def get_area(self):
        """Абстрактный метод для получения места работы из вакансии"""
        pass

    @abstractmethod
    def get_employer(self):
        """Абстрактный метод для получения компании-работодателя из вакансии"""
        pass

    @abstractmethod
    def get_salary(self):
        """Абстрактный метод для получения зарплаты из вакансии"""
        pass

    @abstractmethod
    def get_published_time(self):
        """Абстрактный метод для получения даты публикации вакансии"""
        pass
