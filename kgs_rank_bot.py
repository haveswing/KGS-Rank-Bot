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
    command = msg['text']
    
    if command.startswith('/rank '):
        rank(msg)
    elif command == '/rank':
        howtorank(msg)
    elif command == '/start':
        bot.sendMessage(chat_id, 'Welcome to KGS Rank Bot!', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    elif command == '/info':
        print chat_id, 'request info.'
        bot.sendMessage(chat_id, 'INFO\nHERE', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    elif command == 'top100':
        print chat_id, 'request top100.
        bot.sendMessage(chat_id, 'Top 100 KGS Players:\nhttps://www.gokgs.com/top100.jsp', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
        
def rank(msg):
    print 'Rank graph request:'
    chat_id = msg['chat']['id']
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

def howtorank(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print chat_id, 'request how to rank.'
    bot.sendMessage(chat_id, 'Use this command directly with the KGS username.\ne.g.: "/rank ChoChikun".', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    

TOKEN = sys.argv[0]

bot = telepot.Bot(os.environ.get('TOKEN_VARIABLE'))
bot.message_loop(handle)
bot.setWebhook()
print 'KGS Rank Bot is listening...'

while 1:
    time.sleep(10)
