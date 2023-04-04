from reels.insta_reels import Insta
from reels.acc_info import AccInfo
import time

user = AccInfo.username()
passwd = AccInfo.password(user)

with Insta() as bot:
    bot.implicitly_wait(15)
    bot.login_page()
    bot.maximize_window()
    bot.username(user)
    bot.password(passwd)
    bot.login_btn()
    bot.save_login_info_prompt()
    bot.enable_notification()
    # bot.homepage()
    bot.reels_btn()
    time.sleep(60)
    bot.logout_btn()

    time.sleep(5)
