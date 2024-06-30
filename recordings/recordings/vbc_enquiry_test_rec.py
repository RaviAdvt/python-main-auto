from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://dev-main-master1.vedant.life/")
        self.click("div#main-website-nav-item-in-place-live span")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) div:nth-of-type(2)")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(4) div:nth-of-type(2) div:nth-of-type(4) button")
        self.type("input#form-field-name", "Ravib")
        self.type("input#form-field-email", "testrec@g.cc")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(5) > div > div > div > div:nth-of-type(3)")
        self.type("input#form-field-phone", "4512369870")
        self.type("input#form-field-age", "20")
        self.select_option_by_text("select#form-field-gender", "Male")
        self.select_option_by_text("select#form-field-listening-time", "Less than a month")
        self.select_option_by_text("select#form-field-profession", "Medical Professional")
        self.select_option_by_text("select#form-field-state", "Jammu and Kashmir")
        self.check_if_unchecked("input#form-field-disclaimer")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(5) > div > div:nth-of-type(3) > div")
