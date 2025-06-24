import allure
from selene import browser, command, have, be

from QAguru_20_homework_9.moodel import User
from QAguru_20_homework_9.resourses import resource_path


class RegistrationPage:
    def register_user(self, user: User):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.driver.execute_script("""
                document.querySelectorAll('.Google-Ad').forEach(el => el.remove());
            """)
        with allure.step("Ввести имя"):
            browser.element('#firstName').type(user.first_name)
        with allure.step("Ввести фамилию"):
            browser.element('#lastName').type(user.last_name)
        with allure.step("Ввести электронную почту"):
            browser.element('#userEmail').type(user.email)
        with allure.step("Выбрать пол"):
            browser.element(f"//label[contains(text(),'{user.gender.value}')]").click()
        with allure.step("Ввести номер телефона"):
            browser.element('#userNumber').type(user.mobile)
        with allure.step("Выбрать дату рождения"):
            day, month_year = user.birthday.split(sep=' ')
            month, year = month_year.split(sep=',')
            browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).should(be.visible).click()
            browser.element(".react-datepicker__year-select").type(f"{year}").click()
            browser.element(".react-datepicker__month-select").type(f"{month}").click()
            browser.element(f".react-datepicker__day--0{day}").click()
        with allure.step("Выбрать предмет"):
            browser.element('#subjectsInput').perform(command.js.scroll_into_view).should(be.visible).type(user.subject[:2]).press_enter()
        with allure.step("Выбрать хобби"):
            browser.element(f"//label[contains(text(),'{user.hobby.value}')]").perform(command.js.scroll_into_view).should(be.visible).click()
        with allure.step("Загрузить аватар"):
            browser.element('#uploadPicture').perform(command.js.scroll_into_view).should(be.visible).send_keys(resource_path(user.picture_name))
        with allure.step("Ввести адрес"):
            browser.element('#currentAddress').perform(command.js.scroll_into_view).type(user.adress)
        with allure.step("Выбрать штат"):
            browser.element("//div[@id='stateCity-wrapper']/descendant::input[1]").perform(command.js.scroll_into_view).should(be.visible).type(user.state.value).press_enter()
        with allure.step("Выбрать город"):
            browser.element("//div[@id='stateCity-wrapper']/descendant::input[2]").perform(command.js.scroll_into_view).should(be.visible).type(user.city).press_enter()
        with allure.step("Подтвердить"):
            browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_filled(self, user: User):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}', user.email, user.gender.value, user.mobile, user.birthday, user.subject,
                             user.hobby.value, user.picture_name, user.adress, f'{user.state.value} {user.city}'))
