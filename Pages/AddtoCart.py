class AddtoCart1():
    def __init__(self, driver):
        self.driver = driver

        # These are the three locators on this page
        self.search_box_xpath = "//input[@id='gh-ac']"
        self.search_button_xpath = "//input[@id='gh-btn']"
        self.item_xpath = "//a[contains(text(),'Portable Type-C Mobile Phone Mini Cooling Fan Supe')]"
        self.select_item_xpath = "//select[@id='msku-sel-1']"
        self.addtocart_button_xpath = "//a[@id='isCartBtn_btn']"
        self.logout_arrow_xpath = "//button[@id='gh-ug']"
        self.logout_button_xpath = "//a[contains(text(),'Sign out')]"

    def search_item(self, searchbox):
        self.driver.find_element_by_xpath(self.search_box_xpath).clear()
        self.driver.find_element_by_xpath(self.search_box_xpath).send_keys(searchbox)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    def addtoCart(self):
        self.driver.find_element_by_xpath(self.item_xpath).click()
        self.driver.find_element_by_xpath(self.select_item_xpath).click()
        self.driver.find_element_by_xpath(self.addtocart_button_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_arrow_xpath).click()
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()