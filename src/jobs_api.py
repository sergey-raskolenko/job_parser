from abc import ABC, abstractmethod
import requests


class JobsAPI(ABC):
    @abstractmethod
    def get_formatted_data(self, user_request):
        pass

    @abstractmethod
    def get_list_of_vacancies(self):
        pass
