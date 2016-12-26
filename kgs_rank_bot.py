import sys
import time
import telepot

def __init__(self):
    print 'KGS Rank Bot started.'

def handle(msg):
    flavor = telepot.flavor(msg)

    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)
    
    chat_id = msg['chat']['id']
    # user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
    if command.startswith('/rank '):
        rank(msg)
    elif command == '/start':
        bot.sendMessage(chat_id, "Welcome to KGS Rank Bot!", parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    elif command == '/info':
        bot.sendMessage(chat_id, "INFO\nHERE", parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
def rank(msg):
    chat_id = msg['chat']['id']
    # user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    
    kgsUser = msg['text'][6:]
    graphUrl = 'www.gokgs.com/servlet/graph/' + kgsUser + '-en_US.png'
    print graphUrl
    
    # bot.sendPhoto(chat_id, graphUrl, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    bot.sendPhoto(chat_id, graphUrl)
    
TOKEN = sys.argv[0]  # get token from command-line

bot = telepot.Bot("269117423:AAH83p9Qhllcu9KbloxeUzglOfIWw-Orwvg")
bot.message_loop(handle)
bot.setWebhook()  # unset webhook by supplying no parameter
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
