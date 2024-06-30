from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://dev-main-master1.vedant.life/")
        self.click("div#main-website-nav-item-in-place-live span")
        self.click("div#main-website-nav-item-in-place-live")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) div:nth-of-type(2) span")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(4) div:nth-of-type(2) div:nth-of-type(4) button")
        self.type("input#form-field-name", "Ravi")
        self.type("input#form-field-email", "testrecord@g.cc")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(5) div div:nth-of-type(3) div:nth-of-type(2)")
        self.type("input#form-field-phone", "7745154012")
        self.click("input#form-field-phone")
        self.type("input#form-field-age", "20")
        self.select_option_by_text("select#form-field-gender", "Male")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(5) div div:nth-of-type(6)")
        self.select_option_by_text("select#form-field-listening-time", "1 to 6 months")
        self.select_option_by_text("select#form-field-profession", "Agriculture/Farming")
        self.select_option_by_text("select#form-field-country", "Honduras")
        self.check_if_unchecked("input#form-field-disclaimer")
        self.select_option_by_text("select#form-field-country", "India")
        self.select_option_by_text("select#form-field-state", "Himachal Pradesh")
        self.click("div#form-field-search-city div")
        self.click('span:contains("Kullu")')
        self.click('span:contains("Submit")')
