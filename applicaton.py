from model.pages.registration_page import RegistrationPage


class Application:
    def __init__(self):
        self.registration_page = RegistrationPage()

app = Application()