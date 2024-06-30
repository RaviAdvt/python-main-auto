from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://dev-main-master1.vedant.life/")
        self.click("div#main-website-right-menu-btn div")
        self.click('a[href="/en/login?page=https%3A%2F%2Fdev-main-master1.vedant.life%2F"] svg path')
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", "rt12@g.cc")
        self.type("input#password", "rt12@g.cc")
        self.click("button#main-website-sign-in-btn")
        self.click("div#main-website-nav-item-in-place-live")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) span")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(4) div:nth-of-type(3) button")
        self.type("input#form-field-phone", "7896352401")
        self.type("input#form-field-age", "20")
        self.select_option_by_text("select#form-field-gender", "Male")
        self.select_option_by_text("select#form-field-listening-time", "Less than a month")
        self.select_option_by_text("select#form-field-profession", "Video or Photo-Editing")
        self.select_option_by_text("select#form-field-state", "Laddakh")
        self.click("div#form-field-search-city div")
        self.select_option_by_text("select#form-field-state", "Haryana")
        self.click("div#form-field-search-city div")
        self.click('span:contains("Bahadurgarh")')
        self.check_if_unchecked("input#form-field-disclaimer")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(5) > div > div:nth-of-type(3) > div")
