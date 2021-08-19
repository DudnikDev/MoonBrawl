from Utils.Writer import Writer
from database.DataBase import DataBase
from Packets.Messages.Server.LoginFailed4 import NError
from Packets.Messages.Server.CustomError import LoginFailedMessage

class SetNameResponse(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(201)
        self.writeString(self.player.name + "\nt.me/moonbrawl")
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(-1)
        self.writeVint(-1)
        self.writeVint(0)
        self.writeVint(0)
        #self.player.err_code = 13
        #LoginFailedMessage(self.client, self.player, "Сервер на тех. работах до 15:10 по МСК").send()
        if "pedikdev" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "pedik" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "pеdіk" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "pedіk" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "реdіk" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "рedik" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "педик" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        elif "пeдик" in self.player.name:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Не устаналивай такой ник\nПредупреждение: Если вы часто будете пытаться ставить такой ник, вы будете забанены в MoonBrawl!").send()
            DataBase.replaceValue(self, 'ban', 1)
            print("PEDIK NIK KICKED!!!")
        else:
            try:
                DataBase.replaceValue(self, 'name', self.player.name + "\nt.me/moonbrawl")
                try:
                    DataBase.replaceValueLD(self, 'name', self.player.name + "\nt.me/moonbrawl")
                except:
                	print("[ERROR] DB.WRITE.NAME.LEADERBOARD")
                print("[ANALYTICS] Token", self.player.Token, "setted name", self.player.name)
            except UnicodeEncodeError:
                print("[ERROR] INCORRECT NICK, RESETING...")
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "500").send()
