import time

import reels.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Insta(webdriver.Edge):

    def __init__(self, teardown=False):
        super(Insta, self).__init__()
        self.teardown = teardown

    def __quit__(self):
        if self.teardown:
            self.close()

    def login_page(self):
        self.get(const.URL)

    def username(self, name):
        user = self.find_element(By.XPATH, "//input[@aria-label='Phone number, username or email address']")
        user.click()
        user.clear()
        user.send_keys(name)

    def password(self, pwd):
        passwd = self.find_element(By.XPATH, "//input[@aria-label='Password']")
        passwd.click()
        passwd.clear()
        passwd.send_keys(pwd)

    def login_btn(self):
        self.find_element(By.XPATH, '//div[text()="Log in"]').click()

    def save_login_info_prompt(self):
        save_btn = self.find_element(By.XPATH, '//div[text()="Not now" and @role="button"]')
        if save_btn.is_displayed():
            save_btn.click()

    def enable_notification(self):
        notification = self.find_element(By.XPATH, '//button[text()="Not Now"]')
        if notification.is_displayed():
            notification.click()

    def homepage(self):
        self.find_element(By.XPATH, '//div[text()="Home"]').click()

    def reels_btn(self):
        self.find_element(By.XPATH, '//a[@href="/reels/"]').click()

    def audio_btn(self):
        self.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Audio is muted'])[1]").click()

    def periodic_scroll(self):
        for _ in range(10):
            time.sleep(30)
            ActionChains(self).send_keys(Keys.ARROW_DOWN).perform()

    def share_btn(self):
        self.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Direct'])[1]").click()

    def logout_btn(self):
        self.find_element(By.XPATH, '//div[text()="More"]').click()
        self.find_element(By.XPATH, '//span[text()="Log out"]').click()


