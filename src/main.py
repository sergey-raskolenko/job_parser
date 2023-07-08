from jobs_api import HeadHunterAPI, SuperJobAPI
from file_handler import JsonHandler
from vacancy import Vacancy


def main():
    """
    Функция-меню для взаимодействия с пользователем, включает в себя различные варианты событий
    """
    # Создание экземпляров классов для работы с API и файлом
    hh = HeadHunterAPI()
    sj = SuperJobAPI()
    file = JsonHandler()

    # Вход в меню
    print("Добро пожаловать в парсер вакансий.")
    while True:

        service_input = input("Выберите сервис для поиска:\n"
                              "1 - HeadHunter\n"
                              "2 - SuperJob\n"
                              "3 - Оба сервиса\n"
                              "0 - Выход\n"
                              "Пользовательский ввод: ")

        # Обработка условий ввода пользователя
        if service_input == '0':
            print("До скорой встречи!")
            break
        elif service_input not in ('0', '1', '2', '3'):
            print("Введено не корректное значение. Повторите ввод.")
            continue
        else:
            keyword_input = input("Введите ключевое слово для поиска: ")

        if service_input == '1':
            raw_vacancy_list = hh.get_vacancies(keyword_input)
            file.add_vacancies(raw_vacancy_list)
            print(f"Вакансий в {file.filename} файл записано: {len(raw_vacancy_list)}")
        elif service_input == '2':
            raw_vacancy_list = sj.get_vacancies(keyword_input)
            file.add_vacancies(raw_vacancy_list)
            print(f"Вакансий в {file.filename} файл записано: {len(raw_vacancy_list)}")
        elif service_input == '3':
            raw_vacancy_list = hh.get_vacancies(keyword_input) + sj.get_vacancies(keyword_input)
            file.add_vacancies(raw_vacancy_list)
            print(f"Вакансий в {file.filename} файл записано: {len(raw_vacancy_list)}")

        # Внутренний уровень меню для взаимодействия с вакансиями и файлом
        while True:
            vacancy_input = input("Что Вы хотите сделать с полученными вакансиями?\n"
                                  "1 - Вывести все вакансии\n"
                                  "2 - Вывести ТОП 10 высокооплачиваемых вакансий\n"
                                  "3 - Вывести вакансии из конкретного города\n"
                                  "4 - Вывести вакансии по наличию ключевого слова в названии\n"
                                  "5 - Очистить файл с вакансиями\n"
                                  "0 - Выход\n"
                                  "Пользовательский ввод: ")

            # Обработка условий ввода пользователя
            if vacancy_input == '0':
                print("До скорой встречи!")
                break
            elif vacancy_input not in ('0', '1', '2', '3', '4', '5'):
                print("Введено не корректное значение. Повторите ввод.")
                continue
            elif vacancy_input == '1':
                for item in file.get_vacancies():
                    print(Vacancy(item))
            elif vacancy_input == '2':
                for item in file.get_10_highly_paid():
                    print(Vacancy(item))
            elif vacancy_input == '3':
                area_input = input("Введите город для фильтрации вакансий: ")
                for item in file.get_vacancies_by_area(area_input):
                    print(Vacancy(item))
            elif vacancy_input == '4':
                name_keyword_input = input("Введите ключевое слово для поиска в названии вакансии: ")
                for item in file.get_vacancies_by_keyword(name_keyword_input):
                    print(Vacancy(item))
            elif vacancy_input == '5':
                file.clear_file()
                print("Файл успешно очищен")
                break


if __name__ == '__main__':
    main()
