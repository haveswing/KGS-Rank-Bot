import sys
import time
import telepot

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print (flavor, summary)
    
    chat_id = msg['from']['id']
    user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
def rank(self, msg):
    chat_id = msg['from']['id']
    user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
    self.sendMessage(chat_id, input("Insert a KGS username to see the rating graph:"), parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    kgsUser = self.input
    graphUrl = "https://www.gokgs.com/servlet/graph/" + kgsUser + "-en_US.png"
    print(graphUrl)
    
    self.sendPhoto(chat_id, graphUrl, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
def __init__(self, msg):
    chat_id = msg['from']['id']
    user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
    if command == "/rank":
        rank(self)
    else:
        print("Unknown command.")


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot("269117423:AAH83p9Qhllcu9KbloxeUzglOfIWw-Orwvg")
bot.message_loop(handle)
print ("Listening ...")

# Keep the program running.
while 1:
    time.sleep(10)
