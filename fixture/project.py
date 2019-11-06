from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.app.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # if session is expired - relogin
        # self.relogin()
        self.fill_in_the_fields(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    def fill_in_the_fields(self, project):
        self.change_field_value("project_name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def relogin(self):
        pass
