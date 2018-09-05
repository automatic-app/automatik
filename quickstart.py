from instapy import InstaPy

session = InstaPy(username='', password='', headless_browser=True)

session.login()

session.set_simulation(enabled=False)
session.follow_user_followers(['supremenewyork'], amount=50, sleep_delay=30, randomize=False, interact=False)

session.end()
