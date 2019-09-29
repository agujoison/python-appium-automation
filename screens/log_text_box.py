class LogTextBox(object):

    add_button_id = 'add'
    text_log_box_id = 'text'

    def __init__(self, driver):
        self.driver = driver

    def add_text_log(self):
        self.driver.find_element_by_id(self.add_button_id).click()

    def get_text_log(self):
        return self.driver.find_element_by_id(self.text_log_box_id).text.strip()