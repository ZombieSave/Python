import scrapy
import logging
from scrapy.http import HtmlResponse
import re
from instaParser.fields import Fields
from instaParser.items import InstaparserItem
from instaParser.parseState import ParseState


class InstaSpider(scrapy.Spider):
    name = 'insta'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com']
    login_request_url = "https://www.instagram.com/accounts/login/ajax/"
    insta_users = [{Fields.username: "trygfjfg", Fields.userId: 50338216673},
                   {Fields.username: "peremennikov", Fields.userId: 4145861687},
                   {Fields.username: "zombie_save", Fields.userId: 50105783705}]
    login = "zombie_save"
    full_name = "zombie save"
    password = "#PWD_INSTAGRAM_BROWSER:10:1637182169:AchQAJaHFl4sJaeVrm8tZ9NBzIa+wT6aGUD7WRhmH6r3ze0ifV3cFChNpDVJI0jiVbnyGlcB+AwQkURlRDx6BpNrnG5hHbk/r2cq6pbdGTrqJMv8IUtyfZ2ob5fZ/0tJBqKFfVmPDnt9DDNXLg=="

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__logger = logging.getLogger()
        self.parse_state = ParseState(self.insta_users)

    def parse(self, response: HtmlResponse, **kwargs):
        X_CSRFToken = self.fetch_csrf_token(response.text)

        try:
            yield scrapy.FormRequest(
                self.login_request_url,
                method="POST",
                callback=self.login_response_callback,
                headers={"X-CSRFToken": X_CSRFToken},
                formdata={Fields.username: self.login,
                          "enc_password": self.password})
        except Exception as ex:
            self.__logger.error(f"Ошибка авторизации: {ex}")

    def login_response_callback(self, response: HtmlResponse):
        try:
            j_data = response.json()
            current_user_id = j_data.get(Fields.userId)

            if j_data.get("authenticated"):
                self.__logger.info(f"{self.login} успешно авторизован")
                # сохраняем текущего пользователя
                yield InstaparserItem(userId=current_user_id,
                                      friend_id=current_user_id,
                                      username=self.login,
                                      full_name=self.full_name,
                                      profile_pic_url=None)

                for insta_user in self.insta_users:
                    user_id = insta_user[Fields.userId]
                    self.__logger.info(f"Получение даных пользователя {insta_user[Fields.username]}")

                    # получение списка подписок
                    while self.parse_state.get_continue_parse_friendships(user_id):
                        yield self.friendship_scroll(response, user_id, Fields.following)

                    self.parse_state.reset(user_id)  # сбрасываем состояние прокрутки для данного пользователя

                    # получение списка подписчиков
                    while self.parse_state.get_continue_parse_friendships(user_id):
                        yield self.friendship_scroll(response, user_id, Fields.followers)
            else:
                self.__logger.warning(f"Отказано в авторизации")
        except Exception as ex:
            self.__logger.error(f"Ошибка получения подписок/подписчиков: {ex}")

    def friendship_scroll(self, response: HtmlResponse, userId, category):
        """прокрутка списка подписок/подписчиков"""
        base_url = f"https://i.instagram.com/api/v1/friendships/{userId}/"
        # собираем следующий url прокрутки
        if category == Fields.following:
            max_id = self.parse_state.get_max_id(userId)
            max_param = f"max_id={max_id}"
        elif category == Fields.followers:
            next_max_id = self.parse_state.get_next_max_id(userId)
            max_param = "" if next_max_id is None else f"max_id={next_max_id}"

        return response.follow(url=f"{base_url}{category}/?count=12&{max_param}",
                               callback=self.scroll_response_callback,
                               headers={"User-Agent": "Instagram 155.0.0.37.107"},
                               cb_kwargs={Fields.userId: userId, Fields.category: category})

    def scroll_response_callback(self, response: HtmlResponse, userId, category):
        data = response.json()
        users = data.get("users")
        next_max_id = data.get("next_max_id")  # следующий id прокрутки подписчиков (id подписок меняется внутри состояния)
        # проверяем что список подписок не пуст или next_max_id и сохраняем в состояние для данного пользователя
        has_users = len(users) > 0
        get_continue_parse_friendships = has_users if category == Fields.following else next_max_id is not None
        self.parse_state.set_state(userId, get_continue_parse_friendships, next_max_id)

        if has_users:
            for user in users:
                yield InstaparserItem(userId=userId,
                                      friend_id=user.get("pk"),
                                      username=user.get(Fields.username),
                                      full_name=user.get(Fields.full_name),
                                      profile_pic_url=user.get(Fields.profile_pic_url))

    def fetch_csrf_token(self, text):
        ''' Get csrf-token for auth '''
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')
