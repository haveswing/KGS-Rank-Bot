import sys
import time
import urllib
import urllib2
import os
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
        bot.sendMessage(chat_id, 'Welcome to KGS Rank Bot!', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    elif command == '/info':
        bot.sendMessage(chat_id, 'INFO\nHERE', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
def rank(msg):
    print 'Rank graph request:'
    chat_id = msg['chat']['id']
    # user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    print 'ID= ', chat_id
    
    kgsUser = msg['text'][6:]
    print 'Requested username= ', msg['text'][6:]
    graphFile = kgsUser + '-en_US.png'
    graphUrl = 'https://www.gokgs.com/servlet/graph/' + kgsUser + '-en_US.png'
    print 'File= ' + graphFile
    print 'Url= ' + graphUrl
    
    theGraph = urllib2.urlopen(graphUrl)
    
    # if msg = 
    
    bot.sendPhoto(chat_id, ('rankgraph.png', theGraph), caption=('KGS rank graph for ' + kgsUser + '.'))
    
    print 'Done, request fulfilled.'
    
TOKEN = sys.argv[0]  # get token from command-line (was 1)

# bot = telepot.Bot('tokenhere')
bot = telepot.Bot(os.environ.get('TOKEN_VARIABLE'))
bot.message_loop(handle)
bot.setWebhook()  # unset webhook by supplying no parameter
print 'KGS Rank Bot is listening...'

# Keep the program running.
while 1:
    time.sleep(10)
