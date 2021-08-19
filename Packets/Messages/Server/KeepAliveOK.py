from Utils.Writer import Writer
import random
from Packets.Messages.Server.CustomError import LoginFailedMessage
from Packets.Messages.Server.MPR import MaintenancePred


class KeepAliveOk(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20108
        self.player = player

    def encode(self):
        try:
            f = open("status.txt")
            fd = f.read()
            print("STATUS - ", fd)
            if fd == "1":
                MaintenancePred(self.client, self.player).send()
                print("[TX] KeepAlive PLUS tex!")
            elif fd == "2":
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Тех работы начались!").send()
            elif fd == "3":
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Сервер неожиданно отключился!").send()
            elif fd == "4":
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Сервер выдал сбой!").send()
            elif fd == "5":
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Плановая перезагрузка!").send()
            else:
                print("[TX] KeepAlive")
        except:
        #MaintenancePred(self.client, self.player).send()
            print("[TX] KeepAlive PLUS ERRREAD")