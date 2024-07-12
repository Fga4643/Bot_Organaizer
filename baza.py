import sqlite3

import config

import telebot
from telebot import types
from config import token, pars, chisa
import datetime 

bot = telebot.TeleBot(token) 

class SQLt():
    def __init__(self):
        self.connection = sqlite3.connect("data.db")
        self.cursor = self.connection.cursor()
    def nachalo(self):
        with self.connection:
            self.cursor.execute('''CREATE TABLE user (id_telegram int)''')
            self.cursor.execute("ALTER TABLE user ADD column 'id_group' 'str'")
            self.cursor.execute("ALTER TABLE user ADD column 'zamet' 'str'")
            self.cursor.execute("ALTER TABLE user ADD column 'pmes' 'int'")
            self.cursor.execute("ALTER TABLE user ADD column 'budil' 'int'")
            self.cursor.execute("ALTER TABLE user ADD column 'zader' 'int'")
            self.cursor.execute("ALTER TABLE user ADD column 'date_zam' 'str'")
            self.cursor.execute("ALTER TABLE user ADD column 'token' 'int'")
            self.cursor.execute("ALTER TABLE user ADD column 'toker' 'int'")
            self.cursor.execute("ALTER TABLE user ADD column 'koker' 'int'")
            self.cursor.execute('''CREATE TABLE zamet (id_zamet str)''')
            self.cursor.execute("ALTER TABLE zamet ADD column 'zametka' 'str'")
            self.cursor.execute("ALTER TABLE zamet ADD column 'privaz' 'str'")
            self.cursor.execute("ALTER TABLE zamet ADD column 'id_telegram' 'int'")
            self.cursor.execute("ALTER TABLE zamet ADD column 'date' 'str'")
    def new_user(self, id_telegram,id_group):
        with self.connection:
            self.cursor.execute(f"INSERT INTO user (id_telegram,id_group,zamet,pmes,budil,zader,date_zam,token,toker,koker)"
                                f"VALUES ({id_telegram},\"{id_group}\",0,0,0,0,\"\",0,0,0)")         
    
    def get_id_group(self, id_telegram):
        with self.connection:
            return self.cursor.execute(f"SELECT id_group from user where id_telegram ={id_telegram}").fetchone()[0]
        
    def get_id_budil(self, id_telegram):
        with self.connection:
            return self.cursor.execute(f"SELECT budil from user where id_telegram ={id_telegram}").fetchone()[0]        
        
    def counts_users_for(self, message):
        with self.connection:
            return self.cursor.execute(f"SELECT count(*) FROM user WHERE id_telegram = {message.chat.id}").fetchone()[0]     
    
    
    def set_id_group(self, user_id, id_group):
        with self.connection:
            self.cursor.execute(f"UPDATE user SET id_group = \"{id_group}\" where id_telegram = {user_id}") 
            
    def counts_zamet_for(self, user_id):
        with self.connection:
            return self.cursor.execute(f"SELECT count(*) FROM zamet WHERE id_telegram = {user_id}").fetchone()[0] 
        
    def new_zametka(self,id_zamet, user_id, zametka,date):
        with self.connection:
            d=datetime.date.today()
            self.cursor.execute(f"INSERT INTO zamet (id_zamet,id_telegram,zametka,date)"
                                f"VALUES (\"{id_zamet}\",{user_id},\"{zametka}\",\"{date}\")") 
    def set_new_zametka(self,id_zamet, zametka):
        with self.connection:
            self.cursor.execute(f"UPDATE zamet SET zametka = \"{zametka}\" where id_zamet = \"{id_zamet}\"")           
    def get_zametka_dates(self, user_id):
        with self.connection:
                    return self.cursor.execute(f"SELECT date_zam FROM user WHERE id_telegram = {user_id}").fetchone()[0]
    def set_zametka_dates(self, user_id, date):
        with self.connection:
            self.cursor.execute(f"UPDATE user SET date_zam = \"{date}\" where id_telegram = {user_id}")   
            
    def count_select(self):
        with self.connection:
            return self.cursor.execute(f"SELECT COUNT (*) FROM user").fetchone()[0]    
            
    def get_date_zam(self, user_id, date):
        with self.connection:
            return self.cursor.execute(f"SELECT date FROM zamet WHERE id_telegram = {user_id}").fetchone()[0]           
    
    def get_zametka(self,id_zamet) :
        with self.connection:
            return self.cursor.execute(f"SELECT zametka FROM zamet WHERE id_zamet = \"{id_zamet}\"").fetchone()[0]          
    
    def set_pmes(self,pmes,id_telegram):
        with self.connection:
            self.cursor.execute("UPDATE user SET pmes = ? WHERE id_telegram = ?",(str(pmes),str(id_telegram)))    
    
    def pmes(self,id_telegram):
        with self.connection:
            return self.cursor.execute(f"SELECT pmes from user where id_telegram ={id_telegram}").fetchone()[0]    
    
    def get_budil(self,id_telegram):
        with self.connection:
            return self.cursor.execute(f"SELECT budil from user where id_telegram ={id_telegram}").fetchone()[0] 
    
    def get_zaderzh(self,id_telegram):
        with self.connection:
            try:
                return self.cursor.execute(f"SELECT zader from user where id_telegram ={id_telegram}").fetchone()[0] 
            except:
                return None
    def set_budil(self,id_telegram, budil):
        with self.connection:
            self.cursor.execute("UPDATE user SET budil = ? WHERE id_telegram = ?",(budil,id_telegram))
            
    def set_zader(self,id_telegram, zader):
        with self.connection:
            self.cursor.execute("UPDATE user SET zader = ? WHERE id_telegram = ?",(zader,id_telegram))    
        
    def budilka(self,budil):
        with self.connection:
            try:
                return self.cursor.execute(f"SELECT id_telegram from user where budil ={budil}").fetchone()[0] 
            except:
                return None
    def get_kek(self,id_telegram) :
        with self.connection:
            return self.cursor.execute(f"SELECT koker FROM user WHERE id_telegram = \"{id_telegram}\"").fetchone()[0]          
    
    def set_kek(self,kek,id_telegram):
        with self.connection:
            self.cursor.execute("UPDATE user SET koker = ? WHERE id_telegram = ?",(kek,id_telegram))           
        
    def close(self):
        self.connection.close()    