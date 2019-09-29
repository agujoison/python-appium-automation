class TextDemo:

    log_text_box_button_id = 'LogTextBox'

    def __init__(self, driver):
        self.driver = driver

    def open_log_text_box_option(self):
        self.driver.find_element_by_accessibility_id(self.log_text_box_button_id).click()