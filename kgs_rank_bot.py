import sys
import time
import telepot

def __init__(self):
    print 'KGS Rank Bot started.'

def handle(self, msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)
    
    chat_id = msg['from']['id']
    user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
    if command.startswith('/rank '):
        rank(msg)
    elif command == '/start':
        self.sendMessage(chat_id, "Welcome to KGS Rank Bot!", parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    elif command == '/info':
        self.sendMessage(chat_id, "INFO_HERE", parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
def rank(self, msg):
    chat_id = msg['from']['id']
    user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
    kgsUser = msg['text'][6:]
    graphUrl = "https://www.gokgs.com/servlet/graph/" + kgsUser + "-en_US.png"
    print graphUrl
    
    self.sendPhoto(chat_id, graphUrl, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
    
TOKEN = sys.argv[0]  # get token from command-line

bot = telepot.Bot("269117423:AAH83p9Qhllcu9KbloxeUzglOfIWw-Orwvg")
bot.message_loop(handle)
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
