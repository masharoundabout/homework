import os

import allure
from selene import browser, have, command

from resource import picture_path


class RegistrationPage:
    def __init__(self):
        pass

    @allure.feature("Fill registration form")
    @allure.step('Open registration page')
    def open(self):
        browser.open('/automation-practice-form')

    @allure.feature("Fill registration form")
    @allure.step('Type first name')
    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    @allure.feature("Fill registration form")
    @allure.step('Type last name')
    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    @allure.feature("Fill registration form")
    @allure.step('Type email')
    def type_email(self, value):
        browser.element('#userEmail').type(value)

    @allure.feature("Fill registration form")
    @allure.step('Select gender')
    def select_gender(self, value):
        browser.all('[for^=gender-radio]').element_by(have.text(value)).perform(command.js.scroll_into_view)
        browser.all('[for^=gender-radio]').element_by(have.text(value)).click()

    @allure.feature("Fill registration form")
    @allure.step('Type telephone')
    def type_telephone(self, value):
        browser.element('#userNumber').type(value)

    @allure.feature("Fill registration form")
    @allure.step('Select birthday')
    def select_birthday(self, month_value, year_value, day_value):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month_value)
        browser.element('.react-datepicker__year-select').send_keys(year_value)
        browser.element(f'.react-datepicker__day--0{day_value}').click()

    @allure.feature("Fill registration form")
    @allure.step('Type subject')
    def type_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    @allure.feature("Fill registration form")
    @allure.step('Select hobby')
    def select_hobbie(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).perform(command.js.scroll_into_view)
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).click()

    @allure.feature("Fill registration form")
    @allure.step('Upload picture')
    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(
            os.path.abspath(value))

    @allure.feature("Fill registration form")
    @allure.step('Type address')
    def type_address(self, value):
        browser.element('#currentAddress').type(value)

    @allure.feature("Fill registration form")
    @allure.step('Select state')
    def select_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()

    @allure.feature("Fill registration form")
    @allure.step('Select city')
    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()

    @allure.feature("Fill registration form")
    @allure.step('Submit form')
    def submit(self):
        browser.element('#submit').submit()

    @allure.feature("Fill registration form")
    @allure.step('Fill form without dataclass')
    def fill_form(self, first_name, last_name, email, gender, telephone, birthday_month, birthday_year, birthday_day,
                  subject, hobbie, picture, addr, state, city):
        self.type_first_name(first_name)
        self.type_last_name(last_name)
        self.type_email(email)
        self.select_gender(gender)
        self.type_telephone(telephone)
        self.select_birthday(birthday_month, birthday_year, birthday_day)
        self.type_subject(subject)
        self.select_hobbie(hobbie)
        self.upload_picture(picture)
        self.type_address(addr)
        self.select_state(state)
        self.select_city(city)
        self.submit_registartion_form()

    @allure.feature("Fill registration form")
    @allure.step('Fill form with dataclass')
    def fill_form_user_input(self, user):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.select_gender(user.gender)
        self.type_telephone(user.telephone)
        self.select_birthday(user.birthday_month, user.birthday_year, user.birthday_day)
        self.type_subject(user.subject)
        self.select_hobbie(user.hobby)
        self.upload_picture(picture_path(user.picture))
        self.type_address(user.addr)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit()

    @allure.feature("Fill registration form")
    @allure.step('Check submission without dataclass')
    def should_have_submitted(self, name, email, gender, telephone, birthday, subject, hobbie, picture, addr, state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{name}',
                f'{email}',
                f'{gender}',
                f'{telephone}',
                f'{birthday}',
                f'{subject}',
                f'{hobbie}',
                f'{picture}',
                f'{addr}',
                f'{state}',
            )
        )

    @allure.feature("Fill registration form")
    @allure.step('Check submission with dataclass')
    def should_have_submitted_user_input(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                f'{user.email}',
                f'{user.gender}',
                f'{user.telephone}',
                f'{user.birthday_day} {user.birthday_month},{user.birthday_year}',
                f'{user.subject}',
                f'{user.hobby}',
                f'{user.picture}',
                f'{user.addr}',
                f'{user.state} {user.city}',
            )
        )
