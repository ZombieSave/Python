class ParseState:
    """хранилище состояний прокрутки списков подписок для каждого пользователя"""
    __continue_parse_friendships = "continue_parse_friendships"
    __max_id = "max_id"
    __next_max_id = None
    __user_id = "user_id"
    __parse_state = []
    __increment = 12

    def __init__(self, insta_users: []):
        for insta_user in insta_users:
            self.__parse_state.append({self.__user_id: insta_user["userId"],  # пользователь состояния
                                       self.__continue_parse_friendships: True,  # если список после прокрутки не пуст то True
                                       self.__max_id: 0,  # счётчик прокрутки элементов списка подписок
                                       self.__next_max_id: None})  # id следующего шага прокрутки списка подписчиков

    def reset(self, user_id):
        state = self.__get_state(user_id)
        state[self.__continue_parse_friendships] = True
        state[self.__max_id] = 0
        state[self.__next_max_id] = None

    def get_continue_parse_friendships(self, user_id):
        """состояние списка прокрутки (конец/не конец)"""
        state = self.__get_state(user_id)
        return state[self.__continue_parse_friendships]

    def get_max_id(self, user_id):
        """состояние прокрутки списка подписок пользователя"""
        state = self.__get_state(user_id)
        return state[self.__max_id]

    def get_next_max_id(self, user_id):
        """состояние прокрутки списка подписчиков пользователя"""
        state = self.__get_state(user_id)
        return state[self.__next_max_id]

    def set_state(self, user_id, continue_parse_friendships: bool, next_max_id):
        """сохранение текущего состояния списков"""
        state = self.__get_state(user_id)
        state[self.__continue_parse_friendships] = continue_parse_friendships
        state[self.__max_id] += self.__increment
        state[self.__next_max_id] = next_max_id

    def __get_state(self, user_id):
        state = list(filter(lambda x: x[self.__user_id] == user_id, self.__parse_state))
        return state[0]
