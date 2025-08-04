import json

import allure
from allure_commons.types import AttachmentType

from applicaton import Application

from selene_main_homework.data.hobbies import Hobbies
from selene_main_homework.data.users import Users
from resource import picture_path
import requests

def test_submit_form(browser):
    app = Application(browser)
    user = Users(first_name = 'Test', last_name = 'Test', email = 'test@qa.qa', gender = 'Male', telephone = '9179996543', birthday_month = 'March',  birthday_year = '1992', birthday_day = '17', subject= 'Computer Science', hobby= Hobbies.SPORT.value, picture='test.jpg', addr = '1110 Park Ave Apt 5R', state = 'NCR', city = 'Delhi')

    #arrange
    app.registration_page.open()

    #act
    app.registration_page.type_first_name(user.first_name)
    app.registration_page.type_last_name(user.last_name)
    app.registration_page.type_email(user.email)
    app.registration_page.select_gender(user.gender)
    app.registration_page.type_telephone(user.telephone)
    app.registration_page.select_birthday(user.birthday_month, user.birthday_year, user.birthday_day)
    app.registration_page.type_subject(user.subject)
    app.registration_page.select_hobbie(user.hobby)
    app.registration_page.upload_picture(picture_path(user.picture))
    app.registration_page.type_address(user.addr)
    app.registration_page.select_state(user.state)
    app.registration_page.select_city(user.city)
    app.registration_page.submit()

    #assert
    app.registration_page.should_have_submitted(f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.telephone}',
            f'{user.birthday_day} {user.birthday_month},{user.birthday_year}',
            f'{user.subject}',
            f'{user.hobby}',
            f'{user.picture}',
            f'{user.addr}',
            f'{user.state} {user.city}')

def test_submit_form_shorter(browser):
    app = Application(browser)
    user = Users(first_name = 'Test', last_name = 'Test', email = 'test@qa.qa', gender = 'Male', telephone = '9179996543', birthday_month = 'March',  birthday_year = '1992', birthday_day = '17', subject= 'Computer Science', hobby= Hobbies.SPORT.value, picture='test.jpg', addr = '1110 Park Ave Apt 5R', state = 'NCR', city = 'Delhi')

    #arrange
    app.registration_page.open()

    #act
    app.registration_page.fill_form_user_input(user)

    #assert
    app.registration_page.should_have_submitted_user_input(user)

def test_rest_api_homework():
    #arrange

    #act
    response = requests.post(f'https://demowebshop.tricentis.com/addproducttocart/catalog/{13}/{1}/{1}')
    body = response.json()

    #assert
    assert response.status_code == 200
    assert body['success'] == True
    assert body['message'] == 'The product has been added to your \u003ca href=\"/cart\"\u003eshopping cart\u003c/a\u003e'
    allure.attach(body=json.dumps(response.json()), name='Response', attachment_type=AttachmentType.TEXT, extension='txt')