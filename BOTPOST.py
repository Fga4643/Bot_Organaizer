import telebot
import requests
from telebot import types
from telebot.types import InputMediaPhoto
from config import token
import json
from random import randint
import threading
from config import user, token, pars, button1, button2, button3, button4, pars_day, chisa,all_para, settings, nazad, btn1, btn2, btn3, btn4, moi_zametki, budil, zaderch, perv_para, admins, soglas
from baza import SQLt
import datetime 
import time
def kuda(target):
    pmes=bot.send_message(target, 'ДЗЫЫЫЫЫЫНЬ🔔')
    time.sleep(5)
    for i in range(5):
        try:
            bot.delete_message(target, pmes.message_id)
        except:
            pass          
        pmes=bot.send_message(target, 'ДЗЫЫЫЫЫЫНЬ🔔')
        time.sleep(5)
        try:
            bot.delete_message(target, pmes.message_id)
        except:
            pass        
def kostil():
    while True:
        try:
            BD=SQLt()
            a=datetime.datetime.now()
            timer=a.hour*60+a.minute
            while BD.budilka(timer)!="0":
                ider=int(BD.budilka(timer))
                if BD.get_zaderzh(ider)!=0:
                    t2 = threading.Thread(target=kuda(ider))
                    BD.set_budil(ider, perv_para(datetime.date.today().isoweekday()+1,pars(BD.get_id_group(ider)),chisa())-int(BD.get_zaderzh(ider)))
                    t2.start()
                else:
                    BD.set_budil(ider, 0)
                    BD.close()                    
            BD.close()
        except:
            try:
                BD=SQLt()
                a=datetime.datetime.now()
                timer=a.hour*60+a.minute                
                ider=int(BD.budilka(timer))
                BD.set_budil(ider, perv_para(datetime.date.today().isoweekday()+1,pars(BD.get_id_group(ider)),chisa())-int(BD.get_zaderzh(ider)))
                BD.close()
            except:
                BD.close()
                pass
            pass
        time.sleep(60)    
try:
    BD = SQLt()
    BD.nachalo()
    BD.close()
except:
    pass
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    BD = SQLt()
    if BD.counts_users_for(message) == 0:
        BD.close()
        bot.send_message(message.chat.id, 'Привет! Я помогаю студентам МГТУ узнать их расписание!\n⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б')
        bot.register_next_step_handler(message, get_user_group)
    else:
        gh = open('photo/Nachalo.jpg', "rb")
        BD = SQLt()
        bot.send_photo(message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
        BD.close()
@bot.message_handler(content_types=['text'])
def main_message(message):
    BD = SQLt()
    print(message)
    
    if message.text == nazad:
        gh = open('photo/Nachalo.jpg', "rb")
        bot.send_photo(message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
        BD.close()     
    elif message.text == "123":
        bot.send_message(message.chat.id, BD.get_id_group(message.chat.id))
        a=datetime.datetime.now()
        timer=a.hour*60+a.minute        
        BD.set_budil(message.chat.id,timer+1)
        bot.send_message(message.chat.id, BD.get_id_budil(message.chat.id))
        BD.close()
    elif message.text == "#$%#$:@#$%^&@" and message.chat.id in admins:
        bot.send_message(message.chat.id, "Я слушаю")
        t2 = threading.Thread(target=kostil())
        t2.start()            
    elif message.text=="Test_dzin":
        t2 = threading.Thread(target=kuda(message.chat.id))
        t2.start()
  
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == button1:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes = bot.send_message(call.message.chat.id,str(pars_day(datetime.date.today().isoweekday(),pars(BD.get_id_group(call.message.chat.id)),chisa())),reply_markup=user()) 
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()   
        elif call.data == button2:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes = bot.send_message(call.message.chat.id,str(pars_day(datetime.date.today().isoweekday()+1,pars(BD.get_id_group(call.message.chat.id)),chisa())),reply_markup=user())
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()
        elif call.data == button3:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            q=all_para(pars(BD.get_id_group(call.message.chat.id))).split("%#%")
            for i in range(len(q)-1):
                bot.send_message(call.message.chat.id,str(q[i])) 
            gh = open('photo/Nachalo.jpg', "rb")
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()     
        elif call.data == button4:
            gh = open('photo/Nachalo.jpg', "rb")
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Что вам угодно?", reply_markup=settings())
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()
        elif call.data == btn1:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass            
            if BD.get_zaderzh(call.message.chat.id)==0:
                pmes=bot.send_message(call.message.chat.id, 'Это не обычный будильник, а магический!🧙🏻\n В нем не нужно вписывать дату и время когда он зазвонит, он сделает это за n минут до первой пары в дне!‍',reply_markup=budil())
                BD.set_pmes(pmes.message_id,call.message.chat.id)
            else:
                pmes=bot.send_message(call.message.chat.id, 'Здраствуйте, вы можете отменить будильник и сменить время до будильника',reply_markup=zaderch())
                BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()
        elif call.data == btn2:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_message(call.message.chat.id, 'Введите имя вашей заметки одним словом, после чего отправьте')
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            bot.register_next_step_handler(call.message, new_name_zametka)
            BD.close()
        elif call.data == btn3:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_message(call.message.chat.id, '⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б')
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            bot.register_next_step_handler(call.message, reset_user_group)
            BD.close()
        elif call.data == btn4:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_message(call.message.chat.id, 'Какую вам показать?', reply_markup=moi_zametki(call.message.chat.id,BD.get_zametka_dates(call.message.chat.id)))
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()        
        elif call.data == '🔙 Назад':
            gh = open('photo/Nachalo.jpg', "rb")
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()
        elif "#1@3$" in call.data and "😉" not in call.data and "😡" not in call.data:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            gh = open('photo/Nachalo.jpg', "rb")
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Ваша заметка:\n"+str(BD.get_zametka(call.data)), reply_markup=nazad(call.data))
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()  
        elif "#1@3$" in call.data and "😉" in call.data:
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            gh = open('photo/Nachalo.jpg', "rb")
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Вы уверены?", reply_markup=soglas(call.data[1:]))
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()  
        elif "#1@3$" in call.data and "😡" in call.data:
            BD = SQLt()
            BD.set_new_zametka(call.data[:-1],"")
            d=list(BD.get_zametka_dates(call.message.chat.id).split())
            d[int(call.data.split("#1@3$")[1][:-1])-1]="%^&@#"
            q=" ".join(d)
            BD.set_zametka_dates(call.message.chat.id,q)
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_message(call.message.chat.id, 'Какую вам показать?', reply_markup=moi_zametki(call.message.chat.id,BD.get_zametka_dates(call.message.chat.id)))
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()          
        elif call.data=="😉Назад😉":
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass
            pmes=bot.send_message(call.message.chat.id, 'Какую вам показать?', reply_markup=moi_zametki(call.message.chat.id,BD.get_zametka_dates(call.message.chat.id)))
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close() 
        elif call.data=="Назад":
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass    
            gh = open('photo/Nachalo.jpg', "rb")
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
            BD.set_pmes(pmes.message_id,call.message.chat.id)
            BD.close()  
        elif call.data=="ZADERSCH":
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass               
            pmes=bot.send_message(call.message.chat.id, 'Введите за сколько вас оповестить‍')
            BD.set_kek(call.message.chat.id,1)
            BD.set_pmes(pmes.message_id,call.message.chat.id) 
            bot.register_next_step_handler(call.message, budilnik)
            BD.close()
        elif call.data=="SNAT":
            BD = SQLt()
            try:
                bot.delete_message(call.message.chat.id, BD.pmes(call.message.chat.id))
            except:
                pass               
            BD.set_zader(call.message.chat.id, int(0))
            gh = open('photo/Nachalo.jpg', "rb")
            pmes=bot.send_photo(call.message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
            BD.set_pmes(pmes.message_id,call.message.chat.id)            
            BD.close()
            

@bot.message_handler(content_types=['text'])
def get_user_group(message):
    try:
        if "-" in message.text and message.text.count("-")==1:
            a=pars(message.text.upper())
            if a==[]:
                bot.send_message(message.chat.id, "⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б")
                bot.register_next_step_handler(message, get_user_group)
            else:
                BD=SQLt()
                BD.new_user(message.chat.id,message.text.upper())
                bot.send_message(message.chat.id, "⌨️ Спасибо что используете нас!\n И помните, империя заботится о вас)")
                bot.register_next_step_handler(message, main_message)
                gh = open('photo/Nachalo.jpg', "rb")
                pmes=bot.send_photo(message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
                BD.set_pmes(pmes,message.chat.id)                
                BD.close()

        else:
            bot.send_message(message.chat.id, "⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б")
            bot.register_next_step_handler(message, get_user_group)

    except:
            bot.send_message(message.chat.id, "⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б")
            bot.register_next_step_handler(message, get_user_group)
    
@bot.message_handler(content_types=['text'])
def budilnik(message):
    try:
        if message.text.isdigit() and int(message.text)!=0:
            BD=SQLt()
            bot.send_message(message.chat.id, "⏱️ Будильник установлен")
            BD.set_zader(message.chat.id, int(message.text))
            BD.set_budil(message.chat.id, perv_para(datetime.date.today().isoweekday()+1,pars(BD.get_id_group(message.chat.id)),chisa()-int(message.text)))
            gh = open('photo/Nachalo.jpg', "rb")
            pmes=bot.send_photo(message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
            BD.set_pmes(pmes,message.chat.id)                
            BD.close()
        elif message.text.isdigit() and int(message.text)==0:
            bot.send_message(message.chat.id, "⏱️ Не ломайте магию! Для 0 задержки существуют обычные будильники! ⏱")
            bot.register_next_step_handler(message, budilnik)            
        else:
            bot.send_message(message.chat.id, "⏱️ Введите сколько за сколько минут вас оповестить! ⏱")
            bot.register_next_step_handler(message, budilnik)

    except Exception as e:
        raise

@bot.message_handler(content_types=['text'])
def reset_user_group(message):
    try:
        if "-" in message.text and message.text.count("-")==1:
            a=pars(message.text.upper())
            if a==[]:
                bot.send_message(message.chat.id, "⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б")
                bot.register_next_step_handler(message, reset_user_group)
            else:
                BD=SQLt()
                BD.set_id_group(message.chat.id,message.text.upper())
                bot.send_message(message.chat.id, "⌨️ Спасибо что используете нас!\n И помните, империя заботится о вас)")
                bot.register_next_step_handler(message, main_message) 
                gh = open('photo/Nachalo.jpg', "rb")                
                pmes=bot.send_photo(message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
                BD.set_pmes(pmes,message.chat.id)   
                BD.close()

        else:
            bot.send_message(message.chat.id, "⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б")
            bot.register_next_step_handler(message, reset_user_group)

    except:
            bot.send_message(message.chat.id, "⌨️ Введите Вашу кафедру:\n‼️Формат: ИУ5-35Б")
            bot.register_next_step_handler(message, get_user_group)


@bot.message_handler(content_types=['text'])
def new_name_zametka(message):
    try:
        if len(message.text.split())==1:
            try:
                BD=SQLt()
                BD.set_zametka_dates(message.chat.id,str(BD.get_zametka_dates(message.chat.id))+" "+str(message.text))
                BD.new_zametka(str(message.chat.id)+"#1@3$"+str(BD.counts_zamet_for(message.chat.id)+1),message.chat.id,"Тут пусто", str(datetime.date.today()))
                bot.send_message(message.chat.id, "Введите саму заметку, одним сообщением:")
                BD.close()
                bot.register_next_step_handler(message, new_zametka)      
            except: 
                bot.send_message(message.chat.id, "Что-то пошло не так, пробуйте снова")
                bot.send_message(message.chat.id, "Введите имя вашей заметки одним словом, после чего отправьте")
                bot.register_next_step_handler(message, new_name_zametka)
        else:
            bot.send_message(message.chat.id, "Введите имя вашей заметки одним словом, после чего отправьте")
            bot.register_next_step_handler(message, new_name_zametka)

    except:
            bot.send_message(message.chat.id, "Введите имя вашей заметки одним словом, после чего отправьте")
            bot.register_next_step_handler(message, new_name_zametka)    



@bot.message_handler(content_types=['text'])
def new_zametka(message):
    try:
        BD=SQLt()
        BD.set_new_zametka(str(message.chat.id)+"#1@3$"+str(BD.counts_zamet_for(message.chat.id)),message.text)
        bot.send_message(message.chat.id, "⌨️ Спасибо что используете нас!\n И помните, империя заботится о вас)")
        bot.register_next_step_handler(message, main_message)  
        gh = open('photo/Nachalo.jpg', "rb")
        bot.send_photo(message.chat.id, gh, caption="Добрый день, у вас все хорошо?", reply_markup=user())
        BD.close()        
    except Exception as e:
        raise
    


        
if __name__ == '__main__':
    bot.polling(none_stop=True)