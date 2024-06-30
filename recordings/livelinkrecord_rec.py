from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://dev-main-master1.vedant.life/")
        self.click("div#main-website-right-menu-btn div")
        self.click('a[href="/en/login?page=https%3A%2F%2Fdev-main-master1.vedant.life%2F"]')
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", "livelink@g.cc")
        self.type("input#password", "livelink@g.cc")
        self.click("button#main-website-sign-in-btn")
        self.click("div#main-website-nav-item-in-place-live div")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) div")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > button")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(5) div span:nth-of-type(2) svg")
        self.open_if_not_url("https://dev-main-master1.vedant.life/en/gita")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > button")
        self.check_if_unchecked("input#form-field-disclaimer-undertaking")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(2) a span")
