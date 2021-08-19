from random import choice
from string import ascii_uppercase
import json
import time
import os
from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Packets.Messages.Server.DoNotDistrubServer import DoNotDistrubServer
from Packets.Messages.Server.GameroomData import GameroomData
from Packets.Messages.Server.CustomError import LoginFailedMessage
from Packets.Messages.Client.Club.MyAllianceMessage import MyAllianceMessage

from Packets.Messages.Server.LoginFailed import LoginFailed
from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from database.DataBase import DataBase

class Login(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.HighID = self.read_int()
        self.player.LowID = self.read_int()
        self.player.Token = self.read_string()
        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()
        self.fingerprintsha = self.read_string()
        self.unk = self.read_int()
        unk2 = self.read_int()
        androidid = self.read_int()
        osver = self.read_int()
        model = self.read_int()
        print("[ANALYTICSLOGIN]")
        print("Major - ", self.major)
        print("androidid - ", androidid)
        print("OSVer - ", osver)
        print("SHA -", self.fingerprintsha)
        print("Unk - ", self.unk)
        print("Unk2 - ", unk2)
        print("model - ", model)

    def process(self):
        #self.player.err_code = 16
        #LoginFailedMessage(self.client, self.player, "SERVER CLOSE 3\n\nТех работы! Попробуйте зайти позже!").send()
        #if self.build != 270:
        	#self.player.err_code = 8
        	#LoginFailedMessage(self.client, self.player, "Доступно обновление! Скачайте в телеграмме!\nMoonBrawl has a update! Download it from our telegram channel!").send()
        if self.major != 27:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "SERVER ERROR 513\n\nНеизвестная версия клиента").send()
        elif self.fingerprintsha != "c8n2ix82kr5nxgg":
            self.player.err_code = 8
            LoginFailedMessage(self.client, self.player, "Доступно обновление! Скачай в нашем Telegram канале @moonbrawl!\n\nUpdate is avaliable! Download new apk in telegram channel @moonbrawl!").send()
            pass
        try:
            lg = open("loginstatus.txt")
            flg = lg.read()
            print("LOGINSTATUS - ", flg)
            if flg == "1":
                self.player.err_code = 10
                LoginFailedMessage(self.client, self.player, "1").send()
                pass
            elif flg == "2":
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Сервер временно отключён!").send()
                pass
            elif flg == "3":
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Сервер перегружен!").send()
                pass
        except:
            print("ERROR CHECK LOGIN STATUS!!!!!!")
        #self.player.err_code = 10
        #LoginFailedMessage(self.client, self.player, "1").send()
        #pass
        time.sleep(0.3)
        if self.player.LowID != 0:
            LoginOk(self.client, self.player).send()
            try:
                DataBase.loadAccount(self)
            except:
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "SERVER ERROR 508\nВаш аккаунт, возможно, повреждён, переустановите MoonBrawl, или обратитесь к @pedikdev в Telegram для восстановления аккаунта!").send()
            print("[LOAD] load account", self.player.Token, "token")
            self.unlockedld = 1
            try:
                print("[LOAD_ANALYTICS]", self.player.name, "name")
            except UnicodeEncodeError:
            	print("[ERROR] 501 By Token", self.player.Token)
            	self.player.err_code = 1
            	defaultnick = "MoonBrawl"
            	LoginFailedMessage(self.client, self.player, "SERVER ERROR 501\n\nОшибка в обработке вашего ника, вы использовали запрещённые символы?\nВаш ник был сброшен на MoonBrawl! Перезайдите!\nЕсли ошибка не исчезнет, сбросьте MoonBrawl до заводских настроек или напишите @pedikdev в Telegram!").send()
            	DataBase.replaceValue(self, 'name', defaultnick + "\nt.me/moonbrawl")
            	try:
            	    DataBase.replaceValueLD(self, 'name', defaultnick + "\nt.me/moonbrawl")
            	except:
                    print("ld nick change err")
            print("[LOAD_ANALYTICS]", self.player.gems, "gems")
            print("[LOAD_ANALYTICS]", self.player.ban, "ban")
            if self.player.ban == 1:
            	self.player.err_code = 11
            	LoginFailedMessage(self.client, self.player, "SERVER ERROR 506\n\nТы был заблокирован в MoonBrawl! - https://t.me/moonbrawl\n\nПроизошла ошибка? Напишите pedikdev! - t.me/pedikdev").send()
            	pass
            OwnHomeData(self.client, self.player).send()
            MyAllianceMessage(self.client, self.player).send()
            if self.player.DoNotDistrub == 1:
                DoNotDistrubServer(self.client, self.player).send()
            if self.player.roomID > 0:
                GameroomData(self.client, self.player).send()
        else:
            self.player.LowID = Helpers.randomID(self)
            self.player.HighID = 0
            self.player.Token = Helpers.randomStringDigits(self)
            LoginOk(self.client, self.player).send()
            OwnHomeData(self.client, self.player).send()
            MyAllianceMessage(self.client, self.player).send()