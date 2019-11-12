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
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def get_project_list(self):
        wd = self.app.wd
        self.app.open_manage_projects_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath\
                    ("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"):
            id = element.get_attribute('href').split("id=", 1)[1]
            name = element.text
            self.project_cache.append(Project(id=id, name=name))
        return list(self.project_cache)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.app.open_manage_projects_page()
        self.open_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def open_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath\
            ("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()

    def relogin(self):
        pass
