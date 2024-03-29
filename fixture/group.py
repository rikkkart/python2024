from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_groups_page(self):
        wd = self.app.wd
        # return group page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # delete group
        wd.find_element(By.NAME, "delete").click()
        self.return_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification form
        wd.find_element(By.NAME, "update").click()
        self.return_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
