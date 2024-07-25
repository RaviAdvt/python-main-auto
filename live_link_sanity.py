from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path= ".env")
# main = os.getenv(""mainbaseurl"")
mainbaseurl = "https://dev-main-master1.vedant.life"
email1 = "rr79@g.cc" # clear undertaking of this user before start test, and create new session
password1 = email1

class RecorderTest(BaseCase):
    def test_login_and_undertaking(self):
        self.open(mainbaseurl)
        self.click("div#main-website-right-menu-btn div")
        # self.click('a[href="/en/login?page=https%3A%2F%2Fdev-main-master2.vedant.life%2F"]') this line is replaced by below line
        self.click_link_text("Login")
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", email1)
        self.type("input#password", password1)
        self.click("button#main-website-sign-in-btn")
        self.click("div#main-website-nav-item-in-place-live span")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) div")
        self.click('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/div[1]/span[1]')
        self.check_if_unchecked("input#form-field-disclaimer-undertaking")
        self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(2) a span")
    
    
    def test_login_and_join(self):
        self.open(mainbaseurl)
        self.click("div#main-website-right-menu-btn svg")
        self.click_link_text("Login")
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", email1)
        self.type("input#password", password1)
        self.click("button#main-website-sign-in-btn")
        self.click("div#main-website-nav-item-in-place-live span")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) div")
        self.click('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]/span[1]')


    def test_livelink_login_join(self):
        self.open(mainbaseurl)
        self.click("div#main-website-nav-item-in-place-live div")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) span")
        self.click('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/div[1]/span[1]')

        # self.click("div#svelte > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > button")
        self.click('button:contains("Log In")')
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", email1)
        self.type("input#password", password1)
        self.click("button#main-website-sign-in-btn")
        self.click('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]/span[1]')

        # self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(2) div:nth-of-type(2) a span")

    def test_login_from_gitasamagam_page_and_join(self):
        self.open(mainbaseurl)
        self.click("div#main-website-nav-item-in-place-live")
        self.click("div#main-website-nav-item-in-place-live div:nth-of-type(2) span")
        self.click("div#svelte div:nth-of-type(2) div:nth-of-type(2) div div:nth-of-type(4) div:nth-of-type(4) span span")
        self.click('button:contains("Sign In with Email")')
        self.type("input#main-website-input-username", email1)
        self.type("input#password", password1)
        self.click("button#main-website-sign-in-btn")
        self.click('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]/div[1]')

