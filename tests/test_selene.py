from applicaton import app
from selene_main_homework.data.hobbies import Hobbies
from selene_main_homework.data.users import Users
from resource import picture_path

def test_submit_form():
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

def test_submit_form_shorter():

    user = Users(first_name = 'Test', last_name = 'Test', email = 'test@qa.qa', gender = 'Male', telephone = '9179996543', birthday_month = 'March',  birthday_year = '1992', birthday_day = '17', subject= 'Computer Science', hobby= Hobbies.SPORT.value, picture='test.jpg', addr = '1110 Park Ave Apt 5R', state = 'NCR', city = 'Delhi')

    # arrange
    app.registration_page.open()

    # act
    app.registration_page.fill_form_user_input(user)

    # assert
    app.registration_page.should_have_submitted_user_input(user)