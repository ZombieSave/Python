class ParseState:
    """хранилище состояний прокрутки списков подписок для каждого пользователя"""
    __continue_followings = "continue_followings"
    __continue_followers = "continue_followers"
    __max_id = "max_id"
    __next_max_id = None
    __user_id = "user_id"
    __parse_state = []

    def __init__(self, insta_users: []):
        for insta_user in insta_users:
            self.__parse_state.append({self.__user_id: insta_user["userId"],  # пользователь состояния
                                       self.__continue_followings: True,  # подписки
                                       self.__continue_followers: True,  # подписчики
                                       self.__max_id: 0,  # счётчик прокрутки элементов списка подписок
                                       self.__next_max_id: None})  # id следующего шага прокрутки списка подписчиков

    def get_continue_scroll_followings(self, user_id):
        """состояние списка прокрутки подписок"""
        state = self.__get_state(user_id)
        return state[self.__continue_followings]

    def get_continue_scroll_followers(self, user_id):
        """состояние списка прокрутки подписчиков"""
        state = self.__get_state(user_id)
        return state[self.__continue_followers]

    def get_max_id(self, user_id):
        """состояние прокрутки списка подписок пользователя"""
        state = self.__get_state(user_id)
        return state[self.__max_id]

    def get_next_max_id(self, user_id):
        """состояние прокрутки списка подписчиков пользователя"""
        state = self.__get_state(user_id)
        return state[self.__next_max_id]

    def set_state_followings(self, user_id, continue_scroll: bool, increment):
        """сохранение текущего состояния списков подписок"""
        state = self.__get_state(user_id)
        state[self.__continue_followings] = continue_scroll
        state[self.__max_id] += increment

    def set_state_followers(self, user_id, continue_scroll: bool, next_max_id):
        """сохранение текущего состояния списков подписчиков"""
        state = self.__get_state(user_id)
        state[self.__continue_followers] = continue_scroll
        state[self.__next_max_id] = next_max_id

    def __get_state(self, user_id):
        state = list(filter(lambda x: x[self.__user_id] == user_id, self.__parse_state))
        return state[0]
