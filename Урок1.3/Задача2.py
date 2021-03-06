# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def user_data(**kwargs):
    print(f"Имя: {kwargs['first_name']}, Фамилия: {kwargs['last_name']}, год рождения: {kwargs['birth_year']}, "
          f"город проживания: {kwargs['city']}, email: {kwargs['email']}, телефон: {kwargs['phone']}")


user_data(last_name="Ульянов",
          first_name="Владимир",
          email="lenin@mail.ru",
          city="Ленинград",
          phone="+79037472760",
          birth_year="1870")
