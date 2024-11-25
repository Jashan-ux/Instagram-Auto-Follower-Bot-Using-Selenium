from insta_followers import InstaFollower

SIMILAR_ACCOUNT = "my_ayurvedic_life"
USERNAME = "ayuxxxxxx01"
PASSWORD = "xxxxxxx"



bot = InstaFollower()
try:
    bot.login(USERNAME, PASSWORD)
    bot.find_followers(SIMILAR_ACCOUNT)
    bot.follow()
finally:
    bot.quit()






