from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://dev-main-master1.vedant.life/")
        self.click("div#main-website-nav-item-in-place-live div")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) span")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > button")
        self.click('button:contains("Log In")')
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", "livelink@g.cc")
        self.type("input#password", "livelink@g.cc")
        self.click("button#main-website-sign-in-btn")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(2) div:nth-of-type(2) a span")
