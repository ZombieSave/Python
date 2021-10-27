# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
# требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

# Flickr API https://www.flickr.com/services/api/ сервис фото и видео материалов. Требует регистрации, после чего
# позволяет сгенерить key.
# Выбран метод получения доступных на странице блог-сервисов. Метод возвращает xml, сохраняем в lickr.xml.
# json в чистом виде не возвращает, оборачивает JavaScript-функцией jsonFlickrApi({...}).
# Без передачи key в строке запроса получаем кастомную ошибку 100 - Invalid API Key (Key has invalid format)
# <?xml version="1.0" encoding="utf-8" ?>
# <rsp stat="fail">
# 	<err code="100" msg="Invalid API Key (Key has invalid format)" />
# </rsp>

import requests

url = f"https://www.flickr.com/services/rest/"
method = "flickr.blogs.getServices"
key = "29163ac4c9cfd7835cdbd4fc804b5a49"
params = {"method": method,
          "api_key": key}
response = requests.get(url, params)
data = response.content
print(data)

with open(f"flickr.xml", "wb") as file:
    file.write(data)


