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