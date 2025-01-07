class BasePage:
    def __init__(self, page):
        self.page = page

class ResetDBPage(BasePage):
    def navigate(self):
        self.page.goto("/reset_db")

    def reset_db(self):
        proceed_button = self.page.locator("button:has-text('proceed')")
        proceed_button.click()

class AddTeamPage(BasePage):
    def navigate(self):
        self.page.goto("/add_team")

    def add_team(self, team_name):
        name_input = self.page.locator('#id_name')
        name_input.fill(team_name)
        self.page.click("text='Add'")

class TeamManagement(BasePage):
    def navigate(self):
        self.page.goto("/teams")

    def delete_team(self):
        self.page.click("text='Delete'")
        self.page.click("text='Proceed'")   

class AddEmployeePage(BasePage):
    def navigate(self):
        self.page.goto("/add_employee")

    def add_employee(self, user_name, user_mail, adress_line1, city, zip_code, hiring_date, job_title):
        name_input = self.page.locator('#id_name')
        name_input.fill(user_name)
        mail_input = self.page.locator('#id_email')
        mail_input.fill(user_mail)

        adress_input = self.page.locator('#id_address_line1')
        adress_input.fill(adress_line1)
        city_input = self.page.locator('#id_city')
        city_input.fill(city)
        zip_input = self.page.locator('#id_zip_code')
        zip_input.fill(zip_code)

        date_input = self.page.locator('#id_hiring_date')
        date_input.fill(hiring_date)
        job_input = self.page.locator('#id_job_title')
        job_input.fill(job_title)

        self.page.click("text='Add'")

class EditEmployeePage(BasePage):
    def navigate(self):
        self.page.goto("/employees")
        self.page.click("text='Edit'")

    def update_address(self, adress_line2):
        self.page.click("text='Update address'")
        adress_input2 = self.page.locator('#id_address_line2')
        adress_input2.fill(adress_line2)
        self.page.click("text='Update'")