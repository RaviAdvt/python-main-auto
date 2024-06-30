from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://dev-main-master1.vedant.life/")
        self.click('span:contains("Menu")')
        self.click('a[href="/en/login?page=https%3A%2F%2Fdev-main-master1.vedant.life%2F"] span')
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", "rt2@g.cc")
        self.type("input#password", "rt2@g.cc")
        self.click("button#main-website-sign-in-btn")
        self.click("div#main-website-nav-item-in-place-live span")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) div:nth-of-type(2) span")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(4) div:nth-of-type(2) div:nth-of-type(4) button")
        self.type("input#form-field-age", "20")
        self.select_option_by_text("select#form-field-gender", "Male")
        self.select_option_by_text("select#form-field-listening-time", "1 to 6 months")
        self.select_option_by_text("select#form-field-profession", "Construction or Real Estate")
        self.select_option_by_text("select#form-field-state", "Jammu and Kashmir")
        self.check_if_unchecked("input#form-field-disclaimer")
        self.click("div#form-field-search-city")
        self.click("div#form-field-search-Anantnag-city-option-desktop")
        self.click('span:contains("Submit")')
