from .base_page import BasePage

#Задаем класс для работы с тестами
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)