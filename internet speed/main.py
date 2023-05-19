from netspeed import Netspeed
from twitterbot import Twitterbot


speed = Netspeed()

if not speed.down_speed > 0 or not speed.up_speed > 0:
    bot = Twitterbot()
    bot.complain(message="")



