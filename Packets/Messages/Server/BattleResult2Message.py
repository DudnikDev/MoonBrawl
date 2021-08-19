from Utils.Writer import Writer
from Database.DataBase import DataBase

class BattleResult2Message(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player



    def encode(self):
        self.writeVint(1)
        self.writeVint(self.player.battle_result)

        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]


        if 0 <= brawler_trophies <= 49:
            win_val = 8
            lose_val = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8
                lose_val = -1

            if 100 <= brawler_trophies <= 199:
                win_val = 8
                lose_val = -2

            if 200 <= brawler_trophies <= 299:
                win_val = 8
                lose_val = -3

            if 300 <= brawler_trophies <= 399:
                win_val = 8
                lose_val = -4

            if 400 <= brawler_trophies <= 499:
                win_val = 8
                lose_val = -5

            if 500 <= brawler_trophies <= 599:
                win_val = 8
                lose_val = -6

            if 600 <= brawler_trophies <= 699:
                win_val = 8
                lose_val = -7

            if 700 <= brawler_trophies <= 799:
                win_val = 8
                lose_val = -8

            if 800 <= brawler_trophies <= 899:
                win_val = 7
                lose_val = -9

            if 900 <= brawler_trophies <= 999:
                win_val = 6
                lose_val = -10

            if 1000 <= brawler_trophies <= 1099:
                win_val = 5
                lose_val = -11

            if 1100 <= brawler_trophies <= 1199:
                win_val = 4
                lose_val = -12

            if brawler_trophies >= 1200:
                win_val = 3
                lose_val = -12

        if self.player.battle_result == 0:
            new_trophies = self.player.trophies + win_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + win_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
        else:
            new_trophies = self.player.trophies + lose_val
            self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + lose_val
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)


        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(23)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(6)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(self.player.brawler_id)
        self.writeVint(29)
        self.writeVint(self.player.skin_id)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.name)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot1)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.bot1_n)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
        self.writeVint(16)
        self.writeVint(self.player.bot2)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.bot2_n)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot3)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.bot3_n)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot4)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.bot4_n)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(2)
        self.writeVint(16)
        self.writeVint(self.player.bot5)
        self.writeVint(0)
        self.writeVint(99999)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeString(self.player.bot5_n)

        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(28)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-1040385)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
