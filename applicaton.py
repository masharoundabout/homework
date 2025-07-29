from model.pages.registration_page import RegistrationPage


class Application():
    def __init__(self, browser):
        self.registration_page = RegistrationPage(browser)