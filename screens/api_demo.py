class ApiDemo(object):

    text_button_id = 'Text'

    def __init__(self, driver):
        self.driver = driver

    def open_text_option(self):
        self.driver.find_element_by_accessibility_id(self.text_button_id).click()
