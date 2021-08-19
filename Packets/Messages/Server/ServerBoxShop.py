from Utils.Writer import Writer
import random
from database.DataBase import DataBase
from Packets.Messages.Server.CustomError import LoginFailedMessage
import time

class ServerBoxShop(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        gems_list = [6 , 12 , 16 , 24, 32]
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(13)
        self.writeVint(2)
        GoldValue = random.randrange(25, 85)
        self.writeVint(GoldValue)
        newGold = self.player.gold + GoldValue
        DataBase.replaceValue(self, 'gold', newGold)
        self.writeVint(0)
        self.writeVint(7)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        gems_rwd = random.choice(gems_list)
        self.writeVint(gems_rwd)
        self.writeVint(0)
        self.writeVint(8) #reward
        newGems = self.player.gems + gems_rwd
        DataBase.replaceValue(self, 'gems', newGems)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(-1)
        self.writeVint(-1)
        self.writeVint(0)
        self.writeVint(0)