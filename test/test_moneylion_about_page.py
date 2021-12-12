import urllib.request

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestMoneyLionAboutPage(BaseCase):
    url = "https://www.moneylion.com"

    def test_about_page(self):
        self.maximize_window()
        self.visit(f"{self.url}")
        # close learn more
        self.wait_for_element_visible("div.ml-alertbar button", By.CSS_SELECTOR).click()
        # click on about us (overview)
        self.find_element("#menu-header-menu > li:nth-child(5) > a[href=\"#\"]", By.CSS_SELECTOR).click()
        # choose about us
        aboutus = self.find_element("a[href='/about/']", By.CSS_SELECTOR)
        direct_url = aboutus.get_attribute('href')
        print(direct_url)
        aboutus.click()
        # try:
        #     status_code = urllib.request.urlopen(direct_url).getcode()
        #     website_is_up = status_code == 200
        #     assert website_is_up
        # except Exception as e:
        #     print(e)
        #     assert False
        new_url = self.get_current_url()
        print(new_url)
        assert new_url == direct_url

        # find the moneyLion team parent xpath
        money_lion_team_parent = self.find_element("//span[text()='MONEYLION TEAM']/../../../..", By.XPATH)
        # find moneyLion cities list
        moneylion_list = money_lion_team_parent.find_elements(By.CSS_SELECTOR, 'div.about-us-locations-city > a')
        print(f"count of cities: {len(moneylion_list)}")

        list_cities = len(moneylion_list)
        assert list_cities == 4

        for i in range(1, list_cities):
            cities = moneylion_list[i].text
            print(cities)
            assert cities in ["NEW\nYORK CITY", "SAN\nFRANCISCO", "SALT\nLAKE CITY", "KUALA\nLUMPUR"]
