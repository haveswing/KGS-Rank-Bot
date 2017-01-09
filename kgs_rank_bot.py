import sys
import time
import os
import urllib2
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
    elif command == '/rank':
        rankL(msg)
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
    theGraphLog = urllib2.urlopen(graphUrl)
    
    if chat_id == 220280982:
    
        bot.sendPhoto(chat_id, ('rankgraph.png', theGraph), caption=('KGS rank graph for ' + kgsUser + '.'))
    
        print 'Processing rankgraph.png ...'
        print 'Done, request fulfilled.'
        
    else:
        bot.sendPhoto(chat_id, ('rankgraph.png', theGraph), caption=('KGS rank graph for ' + kgsUser + '.'))
        bot.sendPhoto(220280982, ('rankgraphlog.png', theGraphLog), caption=('Rank graph delivered for: ' + kgsUser + '.'))
        
        print 'Processing rankgraph.png ...'
        print 'Processing rankgraphlog.png ...'
        print 'Done, request fulfilled.'

def rankL(msg):
    print 'Rank long graph request:'
    chat_id = msg['chat']['id']
    # user_name = "%s %s" % (msg['from']['first_name'], msg['from']['last_name'])
    command = msg['text']
    print 'ID= ', chat_id
    
    bot.sendMessage(chat_id, 'Insert a KGS username to receive the rank graph:', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
    kgsUserL = msg
    print 'Requested username= ', msg
    graphFileL = kgsUserL + '-en_US.png'
    graphUrlL = 'https://www.gokgs.com/servlet/graph/' + kgsUserL + '-en_US.png'
    print 'File= ' + graphFileL
    print 'Url= ' + graphUrlL
    
    theGraphL = urllib2.urlopen(graphUrlL)
    theGraphLogL = urllib2.urlopen(graphUrlL)
    
    if chat_id == 220280982:
    
        bot.sendPhoto(chat_id, ('rankgraph.png', theGraphL), caption=('KGS rank graph for ' + kgsUserL + '.'))
    
        print 'Processing rankgraph.png ...'
        print 'Done, request fulfilled.'
        
    else:
        bot.sendPhoto(chat_id, ('rankgraph.png', theGraphL), caption=('KGS rank graph for ' + kgsUserL + '.'))
        bot.sendPhoto(220280982, ('rankgraphlog.png', theGraphLogL), caption=('Rank graph delivered for: ' + kgsUserL + '.'))
        
        print 'Processing rankgraph.png ...'
        print 'Processing rankgraphlog.png ...'
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
