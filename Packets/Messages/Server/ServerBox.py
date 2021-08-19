from Utils.Writer import Writer
import random
from database.DataBase import DataBase
from Packets.Messages.Server.CustomError import LoginFailedMessage
import time

class ServerBox(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        reward_list = [2 , 3 , 8]
        box = [1 , 2 , 3 , 4] # 1 - коины 2 - коины гемы 3 - коины бравлер 4 - коины бравлер гемы
        boxch = random.choice(box)
        #boxch = 4
        skipbrawler = 0
        gems_list = [3 , 6 , 9 , 12]
        if self.player.boxID == 10:
            print(boxch)
            #if self.player.alreadyopening == 1:
                #time.sleep(2)
            #self.player.alreadyopening = 1
            #print(self.player.alreadyopening)
            if boxch == 1:
                self.writeVint(203)
                self.writeVint(0)
                self.writeVint(1)
                self.writeVint(12)
                self.writeVint(1)
                GoldValue = random.randrange(25, 95)
                self.writeVint(GoldValue)
                newGold = self.player.gold + GoldValue
                DataBase.replaceValue(self, 'gold', newGold)
                self.writeVint(0)
                self.writeVint(7)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1)
            if boxch == 2:
                self.writeVint(203)
                self.writeVint(0)
                self.writeVint(1)
                self.writeVint(12)
                self.writeVint(2)
                GoldValue = random.randrange(25, 95)
                self.writeVint(GoldValue)
                newGold = self.player.gold + GoldValue
                DataBase.replaceValue(self, 'gold', newGold)
                self.writeVint(0)
                self.writeVint(7)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1)
                value = random.randrange(2, 15)
                gems_rwd = random.choice(gems_list)
                self.writeVint(gems_rwd)
                self.writeVint(0)
                reward = random.choice(reward_list)
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
            if boxch == 3:
                rndbrw = random.randrange(1, 45)
                if rndbrw == 1:
                    if self.player.coltunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'coltunlocked', 1)
                    self.player.coltunlocked = 1
                    
                elif rndbrw == 2:
                    if self.player.bullunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bullunlocked', 1)
                    self.player.bullunlocked = 1
                elif rndbrw == 3:
                    if self.player.brockunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'brockunlocked', 1)
                    self.player.brockunlocked = 1
                elif rndbrw == 4:
                    if self.player.ricounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'ricounlocked', 1)
                    self.player.ricounlocked = 1
                elif rndbrw == 5:
                    if self.player.spikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'spikeunlocked', 1)
                    self.player.spikeunlocked = 1
                elif rndbrw == 6:
                    if self.player.barleyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'barleyunlocked', 1)
                    self.player.barleyunlocked = 1
                elif rndbrw == 7:
                    if self.player.jessieunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jessieunlocked', 1)
                    self.player.jessieunlocked = 1
                elif rndbrw == 8:
                    if self.player.nitaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'nitaunlocked', 1)
                    self.player.nitaunlocked = 1
                elif rndbrw == 9:
                    if self.player.dynamikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                    self.player.dynamikeunlocked = 1
                elif rndbrw == 10:
                    if self.player.elprimounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'elprimounlocked', 1)
                    self.player.elprimounlocked = 1
                elif rndbrw == 11:
                    if self.player.mortisunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mortisunlocked', 1)
                    self.player.mortisunlocked = 1
                elif rndbrw == 12:
                    if self.player.crowunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'crowunlocked', 1)
                    self.player.crowunlocked = 1
                elif rndbrw == 13:
                    if self.player.pocounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pocounlocked', 1)
                    self.player.pocounlocked = 1
                elif rndbrw == 14:
                    if self.player.bounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bounlocked', 1)
                    self.player.bounlocked = 1
                elif rndbrw == 15:
                    if self.player.piperunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'piperunlocked', 1)
                    self.player.piperunlocked = 1
                elif rndbrw == 16:
                    if self.player.pamunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pamunlocked', 1)
                    self.player.pamunlocked = 1
                elif rndbrw == 17:
                    if self.player.taraunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'taraunlocked', 1)
                    self.player.taraunlocked = 1
                elif rndbrw == 18:
                    if self.player.darrylunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'darrylunlocked', 1)
                    self.player.darrylunlocked = 1
                elif rndbrw == 19:
                    if self.player.pennyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pennyunlocked', 1)
                    self.player.pennyunlocked = 1
                elif rndbrw == 20:
                    if self.player.frankunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'frankunlocked', 1)
                    self.player.frankunlocked = 1
                elif rndbrw == 21:
                    if self.player.geneunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'geneunlocked', 1)
                    self.player.geneunlocked = 1
                elif rndbrw == 22:
                    if self.player.tickunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'tickunlocked', 1)
                    self.player.tickunlocked = 1
                elif rndbrw == 23:
                    if self.player.leonunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'leonunlocked', 1)
                    self.player.leonunlocked = 1
                elif rndbrw == 24:
                    if self.player.rosaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'rosaunlocked', 1)
                    self.player.rosaunlocked = 1
                elif rndbrw == 25:
                    if self.player.carlunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'carlunlocked', 1)
                    self.player.carlunlocked = 1
                elif rndbrw == 26:
                    if self.player.bibiunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bibiunlocked', 1)
                    self.player.bibiunlocked = 1
                elif rndbrw == 27:
                    if self.player.bitunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bitunlocked', 1)
                    self.player.bitunlocked = 1
                elif rndbrw == 28:
                    if self.player.sandyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sandyunlocked', 1)
                    self.player.sandyunlocked = 1
                elif rndbrw == 29:
                    if self.player.beaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'beaunlocked', 1)
                    self.player.beaunlocked = 1
                elif rndbrw == 30:
                    if self.player.emzunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'emzunlocked', 1)
                    self.player.emzunlocked = 1
                elif rndbrw == 31:
                    if self.player.mrpunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mrpunlocked', 1)
                    self.player.mrpunlocked = 1
                elif rndbrw == 32:
                    if self.player.maxunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'maxunlocked', 1)
                    self.player.maxunlocked = 1
                elif rndbrw == 33:
                    skipbrawler = 1
                elif rndbrw == 34:
                    if self.player.jackyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jackyunlocked', 1)
                    self.player.jackyunlocked = 1
                elif rndbrw == 35:
                    if self.player.galeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'galeunlocked', 1)
                    self.player.galeunlocked = 1
                elif rndbrw == 36:
                    if self.player.naniunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'naniunlocked', 1)
                    self.player.naniunlocked = 1
                elif rndbrw == 37:
                    if self.player.sproutunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sproutunlocked', 1)
                    self.player.sproutunlocked = 1
                elif rndbrw == 38:
                    skipbrawler = 1
                elif rndbrw == 39:
                    skipbrawler = 1
                elif rndbrw == 40:
                    skipbrawler = 1
                elif rndbrw == 41:
                    skipbrawler = 1
                elif rndbrw == 42:
                    skipbrawler = 1
                elif rndbrw == 43:
                    skipbrawler = 1
                elif rndbrw == 44:
                    skipbrawler = 1
                elif rndbrw == 45:
                    skipbrawler = 1
                if skipbrawler == 1:
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(1)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                if skipbrawler != 1:
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(2)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    # бравлер
                    self.writeVint(1)
                    self.writeScId(16, rndbrw)
                    self.writeVint(1)
                    self.writeHexa('''00 00 00''')
                    for i in range(13):
                        self.writeVint(0)
            if boxch == 4:
                #label .braw
                rndbrw = random.randrange(1, 45)
                print("Box - 4, loading...")
                if rndbrw == 1:
                    if self.player.coltunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'coltunlocked', 1)
                    self.player.coltunlocked = 1
                    
                elif rndbrw == 2:
                    if self.player.bullunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bullunlocked', 1)
                    self.player.bullunlocked = 1
                elif rndbrw == 3:
                    if self.player.brockunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'brockunlocked', 1)
                    self.player.brockunlocked = 1
                elif rndbrw == 4:
                    if self.player.ricounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'ricounlocked', 1)
                    self.player.ricounlocked = 1
                elif rndbrw == 5:
                    if self.player.spikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'spikeunlocked', 1)
                    self.player.spikeunlocked = 1
                elif rndbrw == 6:
                    if self.player.barleyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'barleyunlocked', 1)
                    self.player.barleyunlocked = 1
                elif rndbrw == 7:
                    if self.player.jessieunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jessieunlocked', 1)
                    self.player.jessieunlocked = 1
                elif rndbrw == 8:
                    if self.player.nitaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'nitaunlocked', 1)
                    self.player.nitaunlocked = 1
                elif rndbrw == 9:
                    if self.player.dynamikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                    self.player.dynamikeunlocked = 1
                elif rndbrw == 10:
                    if self.player.elprimounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'elprimounlocked', 1)
                    self.player.elprimounlocked = 1
                elif rndbrw == 11:
                    if self.player.mortisunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mortisunlocked', 1)
                    self.player.mortisunlocked = 1
                elif rndbrw == 12:
                    if self.player.crowunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'crowunlocked', 1)
                    self.player.crowunlocked = 1
                elif rndbrw == 13:
                    if self.player.pocounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pocounlocked', 1)
                    self.player.pocounlocked = 1
                elif rndbrw == 14:
                    if self.player.bounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bounlocked', 1)
                    self.player.bounlocked = 1
                elif rndbrw == 15:
                    if self.player.piperunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'piperunlocked', 1)
                    self.player.piperunlocked = 1
                elif rndbrw == 16:
                    if self.player.pamunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pamunlocked', 1)
                    self.player.pamunlocked = 1
                elif rndbrw == 17:
                    if self.player.taraunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'taraunlocked', 1)
                    self.player.taraunlocked = 1
                elif rndbrw == 18:
                    if self.player.darrylunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'darrylunlocked', 1)
                    self.player.darrylunlocked = 1
                elif rndbrw == 19:
                    if self.player.pennyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pennyunlocked', 1)
                    self.player.pennyunlocked = 1
                elif rndbrw == 20:
                    if self.player.frankunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'frankunlocked', 1)
                    self.player.frankunlocked = 1
                elif rndbrw == 21:
                    if self.player.geneunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'geneunlocked', 1)
                    self.player.geneunlocked = 1
                elif rndbrw == 22:
                    if self.player.tickunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'tickunlocked', 1)
                    self.player.tickunlocked = 1
                elif rndbrw == 23:
                    if self.player.leonunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'leonunlocked', 1)
                    self.player.leonunlocked = 1
                elif rndbrw == 24:
                    if self.player.rosaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'rosaunlocked', 1)
                    self.player.rosaunlocked = 1
                elif rndbrw == 25:
                    if self.player.carlunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'carlunlocked', 1)
                    self.player.carlunlocked = 1
                elif rndbrw == 26:
                    if self.player.bibiunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bibiunlocked', 1)
                    self.player.bibiunlocked = 1
                elif rndbrw == 27:
                    if self.player.bitunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bitunlocked', 1)
                    self.player.bitunlocked = 1
                elif rndbrw == 28:
                    if self.player.sandyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sandyunlocked', 1)
                    self.player.sandyunlocked = 1
                elif rndbrw == 29:
                    if self.player.beaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'beaunlocked', 1)
                    self.player.beaunlocked = 1
                elif rndbrw == 30:
                    if self.player.emzunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'emzunlocked', 1)
                    self.player.emzunlocked = 1
                elif rndbrw == 31:
                    if self.player.mrpunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mrpunlocked', 1)
                    self.player.mrpunlocked = 1
                elif rndbrw == 32:
                    if self.player.maxunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'maxunlocked', 1)
                    self.player.maxunlocked = 1
                elif rndbrw == 33:
                    skipbrawler = 1
                elif rndbrw == 34:
                    if self.player.jackyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jackyunlocked', 1)
                    self.player.jackyunlocked = 1
                elif rndbrw == 35:
                    if self.player.galeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'galeunlocked', 1)
                    self.player.galeunlocked = 1
                elif rndbrw == 36:
                    if self.player.naniunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'naniunlocked', 1)
                    self.player.naniunlocked = 1
                elif rndbrw == 37:
                    if self.player.sproutunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sproutunlocked', 1)
                    self.player.sproutunlocked = 1
                elif rndbrw == 38:
                    skipbrawler = 1
                elif rndbrw == 39:
                    skipbrawler = 1
                elif rndbrw == 40:
                    skipbrawler = 1
                elif rndbrw == 41:
                    skipbrawler = 1
                elif rndbrw == 42:
                    skipbrawler = 1
                elif rndbrw == 43:
                    skipbrawler = 1
                elif rndbrw == 44:
                    skipbrawler = 1
                elif rndbrw == 45:
                    skipbrawler = 1
                if skipbrawler == 1:
                    print("Box - 4, Sended! SkipBrawler - 1")
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(2)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    value = random.randrange(2, 15)
                    gems_rwd = random.choice(gems_list)
                    self.writeVint(gems_rwd)
                    self.writeVint(0)
                    reward = random.choice(reward_list)
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
                if skipbrawler != 1:
                    print("Box - 4, Sended! SkipBrawler - 0")
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(3)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(1)
                    self.writeScId(16, rndbrw)
                    self.writeVint(1)
                    #self.writeHexa('''00 00 00''')
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    gems_rwd = random.choice(gems_list)
                    self.writeVint(gems_rwd)
                    value = random.randrange(2, 15)
                    self.writeVint(3) #гемы и билеты маленьких ящиков
                    self.writeVint(0)
                    reward = random.choice(reward_list)
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
        if self.player.boxID == 5:
            newBrawlBox = self.player.brawlBoxes - 100
            #DataBase.replaceValue(self, 'brawlBoxes', newBrawlBox)

            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(10)
            self.writeVint(2)
            GoldValue = random.randrange(25, 95)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            value = random.randrange(2, 15)
            gems_rwd = random.choice(gems_list)
            self.writeVint(gems_rwd) #гемы и билеты маленьких ящиков
            self.writeVint(0)
            reward = random.choice(reward_list)
            self.writeVint(8) #reward

            #if reward == 8:
            newGems = self.player.gems + gems_rwd
            DataBase.replaceValue(self, 'gems', newGems)
            #elif reward == 3:
                #newTickets = self.player.tickets + value
                #DataBase.replaceValue(self, 'tickets', newTickets)     

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)


        if self.player.boxID == 4:
            newBigBox = self.player.bigBoxes - 10
            #DataBase.replaceValue(self, 'bigBoxes', newBigBox)
            self.writeVint(203)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(12)
            self.writeVint(2)
            GoldValue = random.randrange(10, 80)
            self.writeVint(GoldValue)

            newGold = self.player.gold + GoldValue
            #DataBase.replaceValue(self, 'gold', newGold)

            self.writeVint(0)
            self.writeVint(7)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            gems_rwd = random.choice(gems_list)
            self.writeVint(gems_rwd) #Гемы и тикеты среднего ящика
            self.writeVint(0)
            self.writeVint(8) #reward

            #if reward == 8:
                #newtkn = self.player.brawltokens - 500
                #DataBase.replaceValue(self, 'brawltokens', newtkn)
            newGems = self.player.gems + gems_rwd
            DataBase.replaceValue(self, 'gems', newGems)
            #elif reward == 3:
                #newtkn = self.player.brawltokens - 500
                #DataBase.replaceValue(self, 'brawltokens', newtkn)
                #newTickets = self.player.tickets + value
                #DataBase.replaceValue(self, 'tickets', newTickets)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)


        if self.player.boxID == 3 or self.player.boxID == 9:
            print("BOX ID - 3 or 9")
            print(boxch)
            if boxch == 1:
                self.writeVint(203)
                self.writeVint(0)
                self.writeVint(1)
                self.writeVint(11)
                self.writeVint(1)
                GoldValue = random.randrange(25, 450)
                self.writeVint(GoldValue)
                newGold = self.player.gold + GoldValue
                DataBase.replaceValue(self, 'gold', newGold)
                self.writeVint(0)
                self.writeVint(7)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1)
            if boxch == 2:
                self.writeVint(203)
                self.writeVint(0)
                self.writeVint(1)
                self.writeVint(11)
                self.writeVint(2)
                GoldValue = random.randrange(25, 450)
                self.writeVint(GoldValue)
                newGold = self.player.gold + GoldValue
                DataBase.replaceValue(self, 'gold', newGold)
                self.writeVint(0)
                self.writeVint(7)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1)
                value = random.randrange(2, 15)
                gems_rwd = random.choice(gems_list)
                self.writeVint(gems_rwd)
                self.writeVint(0)
                reward = random.choice(reward_list)
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
            if boxch == 3:
                rndbrw = random.randrange(1, 45)
                if rndbrw == 1:
                    if self.player.coltunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'coltunlocked', 1)
                    self.player.coltunlocked = 1
                    
                elif rndbrw == 2:
                    if self.player.bullunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bullunlocked', 1)
                    self.player.bullunlocked = 1
                elif rndbrw == 3:
                    if self.player.brockunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'brockunlocked', 1)
                    self.player.brockunlocked = 1
                elif rndbrw == 4:
                    if self.player.ricounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'ricounlocked', 1)
                    self.player.ricounlocked = 1
                elif rndbrw == 5:
                    if self.player.spikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'spikeunlocked', 1)
                    self.player.spikeunlocked = 1
                elif rndbrw == 6:
                    if self.player.barleyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'barleyunlocked', 1)
                    self.player.barleyunlocked = 1
                elif rndbrw == 7:
                    if self.player.jessieunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jessieunlocked', 1)
                    self.player.jessieunlocked = 1
                elif rndbrw == 8:
                    if self.player.nitaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'nitaunlocked', 1)
                    self.player.nitaunlocked = 1
                elif rndbrw == 9:
                    if self.player.dynamikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                    self.player.dynamikeunlocked = 1
                elif rndbrw == 10:
                    if self.player.elprimounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'elprimounlocked', 1)
                    self.player.elprimounlocked = 1
                elif rndbrw == 11:
                    if self.player.mortisunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mortisunlocked', 1)
                    self.player.mortisunlocked = 1
                elif rndbrw == 12:
                    if self.player.crowunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'crowunlocked', 1)
                    self.player.crowunlocked = 1
                elif rndbrw == 13:
                    if self.player.pocounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pocounlocked', 1)
                    self.player.pocounlocked = 1
                elif rndbrw == 14:
                    if self.player.bounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bounlocked', 1)
                    self.player.bounlocked = 1
                elif rndbrw == 15:
                    if self.player.piperunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'piperunlocked', 1)
                    self.player.piperunlocked = 1
                elif rndbrw == 16:
                    if self.player.pamunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pamunlocked', 1)
                    self.player.pamunlocked = 1
                elif rndbrw == 17:
                    if self.player.taraunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'taraunlocked', 1)
                    self.player.taraunlocked = 1
                elif rndbrw == 18:
                    if self.player.darrylunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'darrylunlocked', 1)
                    self.player.darrylunlocked = 1
                elif rndbrw == 19:
                    if self.player.pennyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pennyunlocked', 1)
                    self.player.pennyunlocked = 1
                elif rndbrw == 20:
                    if self.player.frankunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'frankunlocked', 1)
                    self.player.frankunlocked = 1
                elif rndbrw == 21:
                    if self.player.geneunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'geneunlocked', 1)
                    self.player.geneunlocked = 1
                elif rndbrw == 22:
                    if self.player.tickunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'tickunlocked', 1)
                    self.player.tickunlocked = 1
                elif rndbrw == 23:
                    if self.player.leonunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'leonunlocked', 1)
                    self.player.leonunlocked = 1
                elif rndbrw == 24:
                    if self.player.rosaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'rosaunlocked', 1)
                    self.player.rosaunlocked = 1
                elif rndbrw == 25:
                    if self.player.carlunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'carlunlocked', 1)
                    self.player.carlunlocked = 1
                elif rndbrw == 26:
                    if self.player.bibiunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bibiunlocked', 1)
                    self.player.bibiunlocked = 1
                elif rndbrw == 27:
                    if self.player.bitunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bitunlocked', 1)
                    self.player.bitunlocked = 1
                elif rndbrw == 28:
                    if self.player.sandyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sandyunlocked', 1)
                    self.player.sandyunlocked = 1
                elif rndbrw == 29:
                    if self.player.beaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'beaunlocked', 1)
                    self.player.beaunlocked = 1
                elif rndbrw == 30:
                    if self.player.emzunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'emzunlocked', 1)
                    self.player.emzunlocked = 1
                elif rndbrw == 31:
                    if self.player.mrpunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mrpunlocked', 1)
                    self.player.mrpunlocked = 1
                elif rndbrw == 32:
                    if self.player.maxunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'maxunlocked', 1)
                    self.player.maxunlocked = 1
                elif rndbrw == 33:
                    skipbrawler = 1
                elif rndbrw == 34:
                    if self.player.jackyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jackyunlocked', 1)
                    self.player.jackyunlocked = 1
                elif rndbrw == 35:
                    if self.player.galeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'galeunlocked', 1)
                    self.player.galeunlocked = 1
                elif rndbrw == 36:
                    if self.player.naniunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'naniunlocked', 1)
                    self.player.naniunlocked = 1
                elif rndbrw == 37:
                    if self.player.sproutunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sproutunlocked', 1)
                    self.player.sproutunlocked = 1
                elif rndbrw == 38:
                    skipbrawler = 1
                elif rndbrw == 39:
                    skipbrawler = 1
                elif rndbrw == 40:
                    skipbrawler = 1
                elif rndbrw == 41:
                    skipbrawler = 1
                elif rndbrw == 42:
                    skipbrawler = 1
                elif rndbrw == 43:
                    skipbrawler = 1
                elif rndbrw == 44:
                    skipbrawler = 1
                elif rndbrw == 45:
                    skipbrawler = 1
                if skipbrawler == 1:
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(11)
                    self.writeVint(1)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                if skipbrawler != 1:
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(11)
                    self.writeVint(2)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    # бравлер
                    self.writeVint(1)
                    self.writeScId(16, rndbrw)
                    self.writeVint(1)
                    self.writeHexa('''00 00 00''')
                    for i in range(13):
                        self.writeVint(0)
            if boxch == 4:
                #label .braw
                rndbrw = random.randrange(1, 45)
                print("Box - 4, loading...")
                if rndbrw == 1:
                    if self.player.coltunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'coltunlocked', 1)
                    self.player.coltunlocked = 1
                    
                elif rndbrw == 2:
                    if self.player.bullunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bullunlocked', 1)
                    self.player.bullunlocked = 1
                elif rndbrw == 3:
                    if self.player.brockunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'brockunlocked', 1)
                    self.player.brockunlocked = 1
                elif rndbrw == 4:
                    if self.player.ricounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'ricounlocked', 1)
                    self.player.ricounlocked = 1
                elif rndbrw == 5:
                    if self.player.spikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'spikeunlocked', 1)
                    self.player.spikeunlocked = 1
                elif rndbrw == 6:
                    if self.player.barleyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'barleyunlocked', 1)
                    self.player.barleyunlocked = 1
                elif rndbrw == 7:
                    if self.player.jessieunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jessieunlocked', 1)
                    self.player.jessieunlocked = 1
                elif rndbrw == 8:
                    if self.player.nitaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'nitaunlocked', 1)
                    self.player.nitaunlocked = 1
                elif rndbrw == 9:
                    if self.player.dynamikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                    self.player.dynamikeunlocked = 1
                elif rndbrw == 10:
                    if self.player.elprimounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'elprimounlocked', 1)
                    self.player.elprimounlocked = 1
                elif rndbrw == 11:
                    if self.player.mortisunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mortisunlocked', 1)
                    self.player.mortisunlocked = 1
                elif rndbrw == 12:
                    if self.player.crowunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'crowunlocked', 1)
                    self.player.crowunlocked = 1
                elif rndbrw == 13:
                    if self.player.pocounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pocounlocked', 1)
                    self.player.pocounlocked = 1
                elif rndbrw == 14:
                    if self.player.bounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bounlocked', 1)
                    self.player.bounlocked = 1
                elif rndbrw == 15:
                    if self.player.piperunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'piperunlocked', 1)
                    self.player.piperunlocked = 1
                elif rndbrw == 16:
                    if self.player.pamunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pamunlocked', 1)
                    self.player.pamunlocked = 1
                elif rndbrw == 17:
                    if self.player.taraunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'taraunlocked', 1)
                    self.player.taraunlocked = 1
                elif rndbrw == 18:
                    if self.player.darrylunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'darrylunlocked', 1)
                    self.player.darrylunlocked = 1
                elif rndbrw == 19:
                    if self.player.pennyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pennyunlocked', 1)
                    self.player.pennyunlocked = 1
                elif rndbrw == 20:
                    if self.player.frankunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'frankunlocked', 1)
                    self.player.frankunlocked = 1
                elif rndbrw == 21:
                    if self.player.geneunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'geneunlocked', 1)
                    self.player.geneunlocked = 1
                elif rndbrw == 22:
                    if self.player.tickunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'tickunlocked', 1)
                    self.player.tickunlocked = 1
                elif rndbrw == 23:
                    if self.player.leonunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'leonunlocked', 1)
                    self.player.leonunlocked = 1
                elif rndbrw == 24:
                    if self.player.rosaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'rosaunlocked', 1)
                    self.player.rosaunlocked = 1
                elif rndbrw == 25:
                    if self.player.carlunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'carlunlocked', 1)
                    self.player.carlunlocked = 1
                elif rndbrw == 26:
                    if self.player.bibiunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bibiunlocked', 1)
                    self.player.bibiunlocked = 1
                elif rndbrw == 27:
                    if self.player.bitunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bitunlocked', 1)
                    self.player.bitunlocked = 1
                elif rndbrw == 28:
                    if self.player.sandyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sandyunlocked', 1)
                    self.player.sandyunlocked = 1
                elif rndbrw == 29:
                    if self.player.beaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'beaunlocked', 1)
                    self.player.beaunlocked = 1
                elif rndbrw == 30:
                    if self.player.emzunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'emzunlocked', 1)
                    self.player.emzunlocked = 1
                elif rndbrw == 31:
                    if self.player.mrpunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mrpunlocked', 1)
                    self.player.mrpunlocked = 1
                elif rndbrw == 32:
                    if self.player.maxunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'maxunlocked', 1)
                    self.player.maxunlocked = 1
                elif rndbrw == 33:
                    skipbrawler = 1
                elif rndbrw == 34:
                    if self.player.jackyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jackyunlocked', 1)
                    self.player.jackyunlocked = 1
                elif rndbrw == 35:
                    if self.player.galeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'galeunlocked', 1)
                    self.player.galeunlocked = 1
                elif rndbrw == 36:
                    if self.player.naniunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'naniunlocked', 1)
                    self.player.naniunlocked = 1
                elif rndbrw == 37:
                    if self.player.sproutunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sproutunlocked', 1)
                    self.player.sproutunlocked = 1
                elif rndbrw == 38:
                    skipbrawler = 1
                elif rndbrw == 39:
                    skipbrawler = 1
                elif rndbrw == 40:
                    skipbrawler = 1
                elif rndbrw == 41:
                    skipbrawler = 1
                elif rndbrw == 42:
                    skipbrawler = 1
                elif rndbrw == 43:
                    skipbrawler = 1
                elif rndbrw == 44:
                    skipbrawler = 1
                elif rndbrw == 45:
                    skipbrawler = 1
                if skipbrawler == 1:
                    print("Box - 4, Sended! SkipBrawler - 1")
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(11)
                    self.writeVint(2)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    value = random.randrange(2, 15)
                    gems_rwd = random.choice(gems_list)
                    self.writeVint(gems_rwd)
                    self.writeVint(0)
                    reward = random.choice(reward_list)
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
                if skipbrawler != 1:
                    print("Box - 4, Sended! SkipBrawler - 0")
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(11)
                    self.writeVint(3)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(1)
                    self.writeScId(16, rndbrw)
                    self.writeVint(1)
                    #self.writeHexa('''00 00 00''')
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    gems_rwd = random.choice(gems_list)
                    self.writeVint(gems_rwd)
                    value = random.randrange(2, 15)
                    self.writeVint(3) #гемы и билеты маленьких ящиков
                    self.writeVint(0)
                    reward = random.choice(reward_list)
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

        if self.player.boxID == 1:
            print("BOX ID - 1")
            print(boxch)
            if boxch == 1:
                self.writeVint(203)
                self.writeVint(0)
                self.writeVint(1)
                self.writeVint(12)
                self.writeVint(1)
                GoldValue = random.randrange(25, 95)
                self.writeVint(GoldValue)
                newGold = self.player.gold + GoldValue
                DataBase.replaceValue(self, 'gold', newGold)
                self.writeVint(0)
                self.writeVint(7)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1)
            if boxch == 2:
                self.writeVint(203)
                self.writeVint(0)
                self.writeVint(1)
                self.writeVint(12)
                self.writeVint(2)
                GoldValue = random.randrange(25, 95)
                self.writeVint(GoldValue)
                newGold = self.player.gold + GoldValue
                DataBase.replaceValue(self, 'gold', newGold)
                self.writeVint(0)
                self.writeVint(7)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1)
                value = random.randrange(2, 15)
                gems_rwd = random.choice(gems_list)
                self.writeVint(gems_rwd)
                self.writeVint(0)
                reward = random.choice(reward_list)
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
            if boxch == 3:
                rndbrw = random.randrange(1, 45)
                if rndbrw == 1:
                    if self.player.coltunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'coltunlocked', 1)
                    self.player.coltunlocked = 1
                elif rndbrw == 2:
                    if self.player.bullunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bullunlocked', 1)
                    self.player.bullunlocked = 1
                elif rndbrw == 3:
                    if self.player.brockunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'brockunlocked', 1)
                    self.player.brockunlocked = 1
                elif rndbrw == 4:
                    if self.player.ricounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'ricounlocked', 1)
                    self.player.ricounlocked = 1
                elif rndbrw == 5:
                    if self.player.spikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'spikeunlocked', 1)
                    self.player.spikeunlocked = 1
                elif rndbrw == 6:
                    if self.player.barleyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'barleyunlocked', 1)
                    self.player.barleyunlocked = 1
                elif rndbrw == 7:
                    if self.player.jessieunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jessieunlocked', 1)
                    self.player.jessieunlocked = 1
                elif rndbrw == 8:
                    if self.player.nitaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'nitaunlocked', 1)
                    self.player.nitaunlocked = 1
                elif rndbrw == 9:
                    if self.player.dynamikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                    self.player.dynamikeunlocked = 1
                elif rndbrw == 10:
                    if self.player.elprimounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'elprimounlocked', 1)
                    self.player.elprimounlocked = 1
                elif rndbrw == 11:
                    if self.player.mortisunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mortisunlocked', 1)
                    self.player.mortisunlocked = 1
                elif rndbrw == 12:
                    if self.player.crowunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'crowunlocked', 1)
                    self.player.crowunlocked = 1
                elif rndbrw == 13:
                    if self.player.pocounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pocounlocked', 1)
                    self.player.pocounlocked = 1
                elif rndbrw == 14:
                    if self.player.bounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bounlocked', 1)
                    self.player.bounlocked = 1
                elif rndbrw == 15:
                    if self.player.piperunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'piperunlocked', 1)
                    self.player.piperunlocked = 1
                elif rndbrw == 16:
                    if self.player.pamunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pamunlocked', 1)
                    self.player.pamunlocked = 1
                elif rndbrw == 17:
                    if self.player.taraunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'taraunlocked', 1)
                    self.player.taraunlocked = 1
                elif rndbrw == 18:
                    if self.player.darrylunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'darrylunlocked', 1)
                    self.player.darrylunlocked = 1
                elif rndbrw == 19:
                    if self.player.pennyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pennyunlocked', 1)
                    self.player.pennyunlocked = 1
                elif rndbrw == 20:
                    if self.player.frankunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'frankunlocked', 1)
                    self.player.frankunlocked = 1
                elif rndbrw == 21:
                    if self.player.geneunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'geneunlocked', 1)
                    self.player.geneunlocked = 1
                elif rndbrw == 22:
                    if self.player.tickunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'tickunlocked', 1)
                    self.player.tickunlocked = 1
                elif rndbrw == 23:
                    if self.player.leonunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'leonunlocked', 1)
                    self.player.leonunlocked = 1
                elif rndbrw == 24:
                    if self.player.rosaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'rosaunlocked', 1)
                    self.player.rosaunlocked = 1
                elif rndbrw == 25:
                    if self.player.carlunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'carlunlocked', 1)
                    self.player.carlunlocked = 1
                elif rndbrw == 26:
                    if self.player.bibiunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bibiunlocked', 1)
                    self.player.bibiunlocked = 1
                elif rndbrw == 27:
                    if self.player.bitunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bitunlocked', 1)
                    self.player.bitunlocked = 1
                elif rndbrw == 28:
                    if self.player.sandyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sandyunlocked', 1)
                    self.player.sandyunlocked = 1
                elif rndbrw == 29:
                    if self.player.beaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'beaunlocked', 1)
                    self.player.beaunlocked = 1
                elif rndbrw == 30:
                    if self.player.emzunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'emzunlocked', 1)
                    self.player.emzunlocked = 1
                elif rndbrw == 31:
                    if self.player.mrpunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mrpunlocked', 1)
                    self.player.mrpunlocked = 1
                elif rndbrw == 32:
                    if self.player.maxunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'maxunlocked', 1)
                    self.player.maxunlocked = 1
                elif rndbrw == 33:
                    skipbrawler = 1
                elif rndbrw == 34:
                    if self.player.jackyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jackyunlocked', 1)
                    self.player.jackyunlocked = 1
                elif rndbrw == 35:
                    if self.player.galeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'galeunlocked', 1)
                    self.player.galeunlocked = 1
                elif rndbrw == 36:
                    if self.player.naniunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'naniunlocked', 1)
                    self.player.naniunlocked = 1
                elif rndbrw == 37:
                    if self.player.sproutunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sproutunlocked', 1)
                    self.player.sproutunlocked = 1
                elif rndbrw == 38:
                    skipbrawler = 1
                elif rndbrw == 39:
                    skipbrawler = 1
                elif rndbrw == 40:
                    skipbrawler = 1
                elif rndbrw == 41:
                    skipbrawler = 1
                elif rndbrw == 42:
                    skipbrawler = 1
                elif rndbrw == 43:
                    skipbrawler = 1
                elif rndbrw == 44:
                    skipbrawler = 1
                elif rndbrw == 45:
                    skipbrawler = 1
                if skipbrawler == 1:
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(1)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                if skipbrawler != 1:
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(2)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    # бравлер
                    self.writeVint(1)
                    self.writeScId(16, rndbrw)
                    self.writeVint(1)
                    self.writeHexa('''00 00 00''')
                    for i in range(13):
                        self.writeVint(0)
            if boxch == 4:
                #label .braw
                rndbrw = random.randrange(1, 45)
                print("Box - 4, loading...")
                if rndbrw == 1:
                    if self.player.coltunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'coltunlocked', 1)
                    self.player.coltunlocked = 1
                    
                elif rndbrw == 2:
                    if self.player.bullunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bullunlocked', 1)
                    self.player.bullunlocked = 1
                elif rndbrw == 3:
                    if self.player.brockunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'brockunlocked', 1)
                    self.player.brockunlocked = 1
                elif rndbrw == 4:
                    if self.player.ricounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'ricounlocked', 1)
                    self.player.ricounlocked = 1
                elif rndbrw == 5:
                    if self.player.spikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'spikeunlocked', 1)
                    self.player.spikeunlocked = 1
                elif rndbrw == 6:
                    if self.player.barleyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'barleyunlocked', 1)
                    self.player.barleyunlocked = 1
                elif rndbrw == 7:
                    if self.player.jessieunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jessieunlocked', 1)
                    self.player.jessieunlocked = 1
                elif rndbrw == 8:
                    if self.player.nitaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'nitaunlocked', 1)
                    self.player.nitaunlocked = 1
                elif rndbrw == 9:
                    if self.player.dynamikeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                    self.player.dynamikeunlocked = 1
                elif rndbrw == 10:
                    if self.player.elprimounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'elprimounlocked', 1)
                    self.player.elprimounlocked = 1
                elif rndbrw == 11:
                    if self.player.mortisunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mortisunlocked', 1)
                    self.player.mortisunlocked = 1
                elif rndbrw == 12:
                    if self.player.crowunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'crowunlocked', 1)
                    self.player.crowunlocked = 1
                elif rndbrw == 13:
                    if self.player.pocounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pocounlocked', 1)
                    self.player.pocounlocked = 1
                elif rndbrw == 14:
                    if self.player.bounlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bounlocked', 1)
                    self.player.bounlocked = 1
                elif rndbrw == 15:
                    if self.player.piperunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'piperunlocked', 1)
                    self.player.piperunlocked = 1
                elif rndbrw == 16:
                    if self.player.pamunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pamunlocked', 1)
                    self.player.pamunlocked = 1
                elif rndbrw == 17:
                    if self.player.taraunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'taraunlocked', 1)
                    self.player.taraunlocked = 1
                elif rndbrw == 18:
                    if self.player.darrylunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'darrylunlocked', 1)
                    self.player.darrylunlocked = 1
                elif rndbrw == 19:
                    if self.player.pennyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'pennyunlocked', 1)
                    self.player.pennyunlocked = 1
                elif rndbrw == 20:
                    if self.player.frankunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'frankunlocked', 1)
                    self.player.frankunlocked = 1
                elif rndbrw == 21:
                    if self.player.geneunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'geneunlocked', 1)
                    self.player.geneunlocked = 1
                elif rndbrw == 22:
                    if self.player.tickunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'tickunlocked', 1)
                    self.player.tickunlocked = 1
                elif rndbrw == 23:
                    if self.player.leonunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'leonunlocked', 1)
                    self.player.leonunlocked = 1
                elif rndbrw == 24:
                    if self.player.rosaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'rosaunlocked', 1)
                    self.player.rosaunlocked = 1
                elif rndbrw == 25:
                    if self.player.carlunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'carlunlocked', 1)
                    self.player.carlunlocked = 1
                elif rndbrw == 26:
                    if self.player.bibiunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bibiunlocked', 1)
                    self.player.bibiunlocked = 1
                elif rndbrw == 27:
                    if self.player.bitunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'bitunlocked', 1)
                    self.player.bitunlocked = 1
                elif rndbrw == 28:
                    if self.player.sandyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sandyunlocked', 1)
                    self.player.sandyunlocked = 1
                elif rndbrw == 29:
                    if self.player.beaunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'beaunlocked', 1)
                    self.player.beaunlocked = 1
                elif rndbrw == 30:
                    if self.player.emzunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'emzunlocked', 1)
                    self.player.emzunlocked = 1
                elif rndbrw == 31:
                    if self.player.mrpunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'mrpunlocked', 1)
                    self.player.mrpunlocked = 1
                elif rndbrw == 32:
                    if self.player.maxunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'maxunlocked', 1)
                    self.player.maxunlocked = 1
                elif rndbrw == 33:
                    skipbrawler = 1
                elif rndbrw == 34:
                    if self.player.jackyunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'jackyunlocked', 1)
                    self.player.jackyunlocked = 1
                elif rndbrw == 35:
                    if self.player.galeunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'galeunlocked', 1)
                    self.player.galeunlocked = 1
                elif rndbrw == 36:
                    if self.player.naniunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'naniunlocked', 1)
                    self.player.naniunlocked = 1
                elif rndbrw == 37:
                    if self.player.sproutunlocked == 1:
                        skipbrawler = 1
                    unlocked = 1
                    if skipbrawler != 1:
                        DataBase.replaceValue(self, 'sproutunlocked', 1)
                    self.player.sproutunlocked = 1
                elif rndbrw == 38:
                    skipbrawler = 1
                elif rndbrw == 39:
                    skipbrawler = 1
                elif rndbrw == 40:
                    skipbrawler = 1
                elif rndbrw == 41:
                    skipbrawler = 1
                elif rndbrw == 42:
                    skipbrawler = 1
                elif rndbrw == 43:
                    skipbrawler = 1
                elif rndbrw == 44:
                    skipbrawler = 1
                elif rndbrw == 45:
                    skipbrawler = 1
                if skipbrawler == 1:
                    print("Box - 4, Sended! SkipBrawler - 1")
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(2)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    value = random.randrange(2, 15)
                    gems_rwd = random.choice(gems_list)
                    self.writeVint(gems_rwd)
                    self.writeVint(0)
                    reward = random.choice(reward_list)
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
                if skipbrawler != 1:
                    print("Box - 4, Sended! SkipBrawler - 0")
                    self.writeVint(203)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(12)
                    self.writeVint(3)
                    GoldValue = random.randrange(25, 95)
                    self.writeVint(GoldValue)
                    newGold = self.player.gold + GoldValue
                    DataBase.replaceValue(self, 'gold', newGold)
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(1)
                    self.writeVint(1)
                    self.writeScId(16, rndbrw)
                    self.writeVint(1)
                    #self.writeHexa('''00 00 00''')
                    self.writeVint(0)
                    self.writeVint(7)
                    self.writeVint(0)
                    self.writeVint(0)
                    self.writeVint(0)
                    gems_rwd = random.choice(gems_list)
                    self.writeVint(gems_rwd)
                    value = random.randrange(2, 15)
                    self.writeVint(3) #гемы и билеты маленьких ящиков
                    self.writeVint(0)
                    reward = random.choice(reward_list)
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
        #self.player.alreadyopening = 0