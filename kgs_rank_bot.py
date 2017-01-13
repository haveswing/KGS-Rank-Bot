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
    
    elif command == '/rank@kgsrankbot':
        howtorank(msg)
    
    elif command == '/start':
        start(msg)
    
    elif command == '/start@kgsrankbot':
        start(msg)
    
    elif command == '/info':
        info(msg)
    
    elif command == '/info@kgsrankbot':
        info(msg)
    
    elif command == '/top100':
        top100(msg)
    
    elif command == '/top100@kgsrankbot':
        top100(msg)
        
    elif command == '/topgames':
        topgames(msg)
        
    elif command == '/topgames@kgsrankbot':
        topgames(msg)        
    
    elif command == '/analyze':
        howtoanalyze(msg)
        
    elif command == '/analyze@kgsrankbot':
        howtoanalyze(msg)
        
    elif command.startswith('/analyze '):
        analyze(msg)
    
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
        bot.sendPhoto(220280982, ('rankgraphlog.png', theGraphLog), caption=('Rank graph delivered: ' + kgsUser + '.'))
        
        print 'Processing rankgraph.png ...'
        print 'Processing rankgraphlog.png ...'
        print 'Done, request fulfilled.'
        
def start(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    if chat_id == 220280982:
        print chat_id, 'started KGS Rank Bot.'
        bot.sendMessage(chat_id, 'Hello! Here KGS Rank Bot, may the sente be with you.', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    else:
        print chat_id, 'started KGS Rank Bot.'
        bot.sendMessage(220280982, 'A player started KGS Rank Bot.')
        bot.sendMessage(chat_id, 'Hello! Here KGS Rank Bot, may the sente be with you.', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    
def howtorank(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print chat_id, 'request how to rank.'
    bot.sendMessage(chat_id, 'Use this command directly with the KGS username.\ne.g.: "/rank haveswing".', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

def info(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    if chat_id == 220280982:
        print chat_id, 'request info.'
        dev = urllib2.urlopen('https://www.gokgs.com/servlet/graph/haveswing-en_US.png')
        bot.sendMessage(chat_id, 'COMMANDS:\n/rank - Get the rank graph of a KGS player.\n/analyze - Get KGS Analytics of a player.\n/top100 - Top 100 KGS players.\n/topgames - Top rated games of the month.\n/info - About the bot...\n\nKGS RANK BOT ON GITHUB:\nhttps://github.com/haveswing/KGS-Rank-Bot\n\nKGS HOMEPAGE:\nhttps://www.gokgs.com/\n\nKGS ANALYTICS HOMEPAGE:\nhttp://kgs.gosquares.net/\n\nKGS TOP GAMES BY:\nhttps://orb.at/top100games.html', parse_mode=None, disable_web_page_preview=True, disable_notification=None, reply_to_message_id=None, reply_markup=None)
        bot.sendPhoto(chat_id, ('haveswing.png', dev), caption=('Developed by haveswing.\nantonio.romaggioli@gmail.com'))
    else:
        print chat_id, 'request info.'
        bot.sendMessage(220280982, 'A player asked KGS Rank Bot info.')
        dev = urllib2.urlopen('https://www.gokgs.com/servlet/graph/haveswing-en_US.png')
        bot.sendMessage(chat_id, 'COMMANDS:\n/rank - Get the rank graph of a KGS player.\n/analyze - Get KGS Analytics of a player.\n/top100 - Top 100 KGS players.\n/topgames - Top rated games of the month.\n/info - About the bot...\n\nKGS RANK BOT ON GITHUB:\nhttps://github.com/haveswing/KGS-Rank-Bot\n\nKGS HOMEPAGE:\nhttps://www.gokgs.com/\n\nKGS ANALYTICS HOMEPAGE:\nhttp://kgs.gosquares.net/\n\nKGS TOP GAMES BY:\nhttps://orb.at/top100games.html', parse_mode=None, disable_web_page_preview=True, disable_notification=None, reply_to_message_id=None, reply_markup=None)
        bot.sendPhoto(chat_id, ('haveswing.png', dev), caption=('Developed by haveswing.\nantonio.romaggioli@gmail.com'))

def top100(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    if chat_id == 220280982:
        print chat_id, 'request top100.'
        bot.sendMessage(chat_id, 'Top 100 KGS Players:\nhttps://www.gokgs.com/top100.jsp', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    else:
        print chat_id, 'request top100.'
        bot.sendMessage(220280982, 'A player request KGS Top 100.')
        bot.sendMessage(chat_id, 'Top 100 KGS Players:\nhttps://www.gokgs.com/top100.jsp', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

def topgames(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    if chat_id == 220280982:
        print chat_id, 'request top games.'
        bot.sendMessage(chat_id, 'Top 100 KGS games of the month:\nhttps://orb.at/top100games.html', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    else:
        print chat_id, 'request top100.'
        bot.sendMessage(220280982, 'A player request KGS Top Games.')
        bot.sendMessage(chat_id, 'Top 100 KGS games of the month:\nhttps://orb.at/top100games.html', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

def howtoanalyze(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    if chat_id == 220280982:
        print chat_id, 'request KGS analytics.'
        bot.sendMessage(chat_id, 'Use this command directly with the KGS username.\ne.g.: "/analyze haveswing".', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    else:
        print chat_id, 'request KGS analytics.'
        bot.sendMessage(220280982, 'A player request KGS Analytics.')
        bot.sendMessage(chat_id, 'Use this command directly with the KGS username.\ne.g.: "/analyze haveswing".', parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

def analyze(msg):
    print 'KGS Analytics requested:'
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'ID= ', chat_id
    
    kgsUserAnalyze = msg['text'][9:]
    print 'Requested username= ', msg['text'][9:]
    analyzeUrl = 'http://kgs.gosquares.net/index.rhtml.en?id=' + kgsUserAnalyze
    print 'Analytics Url= ' + analyzeUrl
    print 'Done, Analytics delivered.'
    
    if chat_id == 220280982:
        bot.sendMessage(chat_id, 'KGS Analytics for ' + kgsUserAnalyze + ':\n' + analyzeUrl)
    else:
        bot.sendMessage(220280982, 'KGS Analytics delivered: ' + kgsUserAnalyze + '.\n' + analyzeUrl)
        bot.sendMessage(chat_id, 'KGS Analytics for ' + kgsUserAnalyze + ':\n' + analyzeUrl) 
    
        
TOKEN = sys.argv[0]

bot = telepot.Bot(os.environ.get('TOKEN_VARIABLE'))
bot.message_loop(handle)
bot.setWebhook()
print 'KGS Rank Bot is listening...'

while 1:
    time.sleep(10)
