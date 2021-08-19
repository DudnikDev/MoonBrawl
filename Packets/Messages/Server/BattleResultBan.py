from Utils.Writer import Writer
from database.DataBase import DataBase
import time


class BattleResultBan(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(self.player.GameType)
        print("REQUEST BAN RESULT!!!")
        self.writeVint(0) #Battle Tokens 
        self.writeVint(0) #Trophies Value
        self.writeVint(0) #Unknown
        self.writeVint(0) #Doubled Tokens
        self.writeVint(0) #Double Token Event
        self.writeVint(0) #Token Doubler Remaining
        self.writeVint(0) #Championship Lose 
        self.writeVint(0) #Unknown
        self.writeVint(0) #Championship Level Passed
        self.writeVint(0) #Challenge Reward Type (0 = Star Tokens, 1 = Star Tokens)
        self.writeVint(0) #Challenge Reward Ammount
        self.writeVint(0) #Championship Losses Left
        self.writeVint(0) #Championship Maximun Losses
        self.writeVint(0) #Coin Shower Event
        self.writeVint(0) #Underdog (This thing breaks everything)
        self.writeVint(17) #End Screen Type
        self.writeVint(1) # Championship Type
        self.writeVint(2) #Play Again
        
        self.writeVint(6) #Battle End Screen Players
        
        self.writeVint(5)
        self.writeVint(16) # Brawler CsvID
        self.writeVint(self.player.brawlerID)
        self.writeVint(29)
        self.writeVint(self.player.skinID)
        self.writeVint(0) #Trophies
        self.writeVint(0)
        self.writeVint(10) #Power Level
        bool = True
        self.writeBool(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(1) # LowID

        self.writeString(self.player.name)

        self.writeVint(5000)
        self.writeVint(28000000)
        self.writeVint(43000000) #Name Color
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.Bot1)
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(0)
        self.writeVint(10)
        bool = True
        self.writeBool(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(1) # LowID

        self.writeString(self.player.Bot1N)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.Bot2)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        bool = True
        self.writeBool(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(1) # LowID

        self.writeString(self.player.Bot2N)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.Bot3)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        bool = True
        self.writeBool(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(1) # LowID

        self.writeString(self.player.Bot3N)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.Bot4)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        bool = True
        self.writeBool(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(1) # LowID

        self.writeString(self.player.Bot4N)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.Bot5)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        bool = True
        self.writeBool(bool)
        if bool == True:
            self.writeInt(0) # HighID
            self.writeInt(1) # LowID

        self.writeString(self.player.Bot5N)

        self.writeVint(100) #?
        self.writeVint(28000000) #?
        self.writeVint(43000000) #?
        # Experience Array
        value = 2
        self.writeVint(value)
        for i in range(value):
            self.writeVint(0) # ???
            self.writeVint(0) # Experience Gained

        # Array 2
        self.writeVint(0)

        # Array 3
        self.writeVint(39) # Milestones Csv ID
        self.writeVint(1) # Ranks Milestone
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(5) # Experience Milestone
        self.writeVint(5000)