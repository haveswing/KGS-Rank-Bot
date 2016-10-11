import sys
import time
import telepot

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print (flavor, summary)


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot("269117423:AAH83p9Qhllcu9KbloxeUzglOfIWw-Orwvg")
bot.message_loop(handle)
print ("ping")

# Keep the program running.
while 1:
    time.sleep(10)
