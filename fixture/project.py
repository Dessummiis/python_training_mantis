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

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.open_manage_projects_page()
            self.project_cache = []
        #     for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
        #         cells = element.find_elements_by_tag_name("td")
        #         lastname_text = element.find_element_by_xpath(".//td[2]").text
        #         firstname_text = element.find_element_by_xpath(".//td[3]").text
        #         address = element.find_element_by_xpath(".//td[4]").text
        #         id = element.find_element_by_name("selected[]").get_attribute("value")
        #         all_emails = cells[4].text
        #         all_phones = cells[5].text
        #         self.contact_cache.append(Contact(first_name=firstname_text, last_name=lastname_text, address=address,
        #                                           id=id, all_phones=all_phones,
        #                                           all_emails=all_emails))
        # return list(self.contact_cache)
                #TODO


    def relogin(self):
        pass
