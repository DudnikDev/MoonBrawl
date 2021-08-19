from Utils.Reader import BSMessageReader
from Logic.Player import Players
from Packets.Messages.Server.Btpa import BTPa
from Packets.Messages.Server.Btpb import BTPb
from Packets.Messages.Server.Btpc import BTPc
from Packets.Messages.Server.Btpd import BTPd
from Packets.Messages.Server.Btpe import BTPe
from Packets.Messages.Server.Btpf import BTPf
#from Logic.Battle import LogicBattle
import time
import random
from Packets.Messages.Server.CustomError import LoginFailedMessage

from threading import Thread

class CancelMatchMaking(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self):
        print("Launch battlePlayersPodbr")
        BTPa(self.client, self.player).send()
        time.sleep(random.random())
        BTPb(self.client, self.player).send()
        time.sleep(random.random())
        BTPc(self.client, self.player).send()
        time.sleep(random.random())
        BTPd(self.client, self.player).send()
        time.sleep(random.random())
        BTPe(self.client, self.player).send()
        time.sleep(random.random())
        BTPf(self.client, self.player).send()
        time.sleep(3)
        self.player.err_code = 1
        LoginFailedMessage(self.client, self.player, "Бои ещё не реализованы!\n\nДля поднятия кубков можно использовать дружеские бои!").send()
        #battle = LogicBattle(self.client, self.player)
        #battle.start()