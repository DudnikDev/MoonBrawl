from Utils.Writer import Writer
from database.DataBase import DataBase
import time


class BattleResult(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(self.player.GameType)

        if self.player.brawlerID == 0:
        	brawler_trophies = self.player.shellytrophies
        elif self.player.brawlerID == 1:
        	brawler_trophies = self.player.colttrophies
        elif self.player.brawlerID == 2:
        	brawler_trophies = self.player.bulltrophies
        elif self.player.brawlerID == 3:
        	brawler_trophies = self.player.brocktrophies
        elif self.player.brawlerID == 4:
        	brawler_trophies = self.player.ricotrophies
        elif self.player.brawlerID == 5:
        	brawler_trophies = self.player.spiketrophies
        elif self.player.brawlerID == 6:
        	brawler_trophies = self.player.barleytrophies
        elif self.player.brawlerID == 7:
        	brawler_trophies = self.player.jessietrophies
        elif self.player.brawlerID == 8:
        	brawler_trophies = self.player.nitatrophies
        elif self.player.brawlerID == 9:
        	brawler_trophies = self.player.dynamiketrophies
        elif self.player.brawlerID == 10:
        	brawler_trophies = self.player.elprimotrophies
        elif self.player.brawlerID == 11:
        	brawler_trophies = self.player.mortistrophies
        elif self.player.brawlerID == 12:
        	brawler_trophies = self.player.crowtrophies
        elif self.player.brawlerID == 13:
        	brawler_trophies = self.player.pocotrophies
        elif self.player.brawlerID == 14:
        	brawler_trophies = self.player.botrophies
        elif self.player.brawlerID == 15:
        	brawler_trophies = self.player.pipertrophies
        elif self.player.brawlerID == 16:
        	brawler_trophies = self.player.pamtrophies
        elif self.player.brawlerID == 17:
        	brawler_trophies = self.player.taratrophies
        elif self.player.brawlerID == 18:
        	brawler_trophies = self.player.darryltrophies
        elif self.player.brawlerID == 19:
        	brawler_trophies = self.player.pennytrophies
        elif self.player.brawlerID == 20:
        	brawler_trophies = self.player.franktrophies
        elif self.player.brawlerID == 21:
        	brawler_trophies = self.player.genetrophies
        elif self.player.brawlerID == 22:
        	brawler_trophies = self.player.ticktrophies
        elif self.player.brawlerID == 23:
        	brawler_trophies = self.player.leontrophies
        elif self.player.brawlerID == 24:
        	brawler_trophies = self.player.rosatrophies
        elif self.player.brawlerID == 25:
        	brawler_trophies = self.player.carltrophies
        elif self.player.brawlerID == 26:
        	brawler_trophies = self.player.bibitrophies
        elif self.player.brawlerID == 27:
        	brawler_trophies = self.player.bittrophies
        elif self.player.brawlerID == 28:
        	brawler_trophies = self.player.sandytrophies
        elif self.player.brawlerID == 29:
        	brawler_trophies = self.player.beatrophies
        elif self.player.brawlerID == 30:
        	brawler_trophies = self.player.emztrophies
        elif self.player.brawlerID == 31:
        	brawler_trophies = self.player.mrptrophies
        elif self.player.brawlerID == 32:
        	brawler_trophies = self.player.maxtrophies
        elif self.player.brawlerID == 34:
        	brawler_trophies = self.player.jackytrophies
        elif self.player.brawlerID == 35:
        	brawler_trophies = self.player.galetrophies
        elif self.player.brawlerID == 36:
        	brawler_trophies = self.player.nanitrophies
        elif self.player.brawlerID == 37:
        	brawler_trophies = self.player.sprouttrophies
        
        exp_reward = [8, 6, 4]
        token_list = [20,15,10]
        namecolor = (43000000) + self.player.namecolor

        self.requested_val = DataBase.getVal(self, 'tickets')
        if self.requested_val != 6392:
            if 0 <= brawler_trophies <= 49:
                win = 8
                rank_1_val = 10
                rank_2_val = 8
                rank_3_val = 7
                rank_4_val = 6
                rank_5_val = 4
                rank_6_val = 2
                rank_7_val = 2
                rank_8_val = 1
                rank_9_val = 0
                rank_10_val = 0

                rank_1_val2 = 10
                rank_2_val2 = 8
                rank_3_val2 = 7
                rank_4_val2 = 6
                rank_5_val2 = 4
                rank_6_val2 = 2
                rank_7_val2 = 2
                rank_8_val2 = 1
                rank_9_val2 = 0
                rank_10_val2 = 0

            else:
                if 50 <= brawler_trophies <= 99:
                    win = 7
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 7
                    rank_4_val = 6
                    rank_5_val = 3
                    rank_6_val = 2
                    rank_7_val = 2
                    rank_8_val = 0
                    rank_9_val = -1
                    rank_10_val = -2

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 7
                    rank_4_val2 = 6
                    rank_5_val2 = 3
                    rank_6_val2 = 2
                    rank_7_val2 = 2
                    rank_8_val2 = 0
                    rank_9_val2 = -64
                    rank_10_val2 = -63

                if 100 <= brawler_trophies <= 199:
                    win = 6
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 7
                    rank_4_val = 6
                    rank_5_val = 3
                    rank_6_val = 1
                    rank_7_val = 0
                    rank_8_val = -1
                    rank_9_val = -2
                    rank_10_val = -2

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 7
                    rank_4_val2 = 6
                    rank_5_val2 = 3
                    rank_6_val2 = 1
                    rank_7_val2 = 0
                    rank_8_val2 = -64
                    rank_9_val2 = -63
                    rank_10_val2 = -63

                if 200 <= brawler_trophies <= 299:
                    win = 6
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 6
                    rank_4_val = 5
                    rank_5_val = 3
                    rank_6_val = 1
                    rank_7_val = 0
                    rank_8_val = -2
                    rank_9_val = -3
                    rank_10_val = -3

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 6
                    rank_4_val2 = 5
                    rank_5_val2 = 3
                    rank_6_val2 = 1
                    rank_7_val2 = 0
                    rank_8_val2 = -63
                    rank_9_val2 = -62
                    rank_10_val2 = -62

                if 300 <= brawler_trophies <= 399:
                    win = 5
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 6
                    rank_4_val = 5
                    rank_5_val = 2
                    rank_6_val = 0
                    rank_7_val = 0
                    rank_8_val = -3
                    rank_9_val = -4
                    rank_10_val = -4

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 6
                    rank_4_val2 = 5
                    rank_5_val2 = 2
                    rank_6_val2 = 0
                    rank_7_val2 = 0
                    rank_8_val2 = -62
                    rank_9_val2 = -61
                    rank_10_val2 = -61

                if 400 <= brawler_trophies <= 499:
                    win = 5
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 6
                    rank_4_val = 5
                    rank_5_val = 2
                    rank_6_val = -1
                    rank_7_val = -2
                    rank_8_val = -3
                    rank_9_val = -5
                    rank_10_val = -5

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 6
                    rank_4_val2 = 5
                    rank_5_val2 = 2
                    rank_6_val2 = -64
                    rank_7_val2 = -63
                    rank_8_val2 = -62
                    rank_9_val2 = -60
                    rank_10_val2 = -60

                if 500 <= brawler_trophies <= 599:
                    win = 5
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 6
                    rank_4_val = 4
                    rank_5_val = 2
                    rank_6_val = -1
                    rank_7_val = -2
                    rank_8_val = -5
                    rank_9_val = -6
                    rank_10_val = -6

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 6
                    rank_4_val2 = 4
                    rank_5_val2 = 2
                    rank_6_val2 = -64
                    rank_7_val2 = -63
                    rank_8_val2 = -60
                    rank_9_val2 = -59
                    rank_10_val2 = -59

                if 600 <= brawler_trophies <= 699:
                    win = 5
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 6
                    rank_4_val = 4
                    rank_5_val = 1
                    rank_6_val = -2
                    rank_7_val = -2
                    rank_8_val = -5
                    rank_9_val = -7
                    rank_10_val = -8

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 6
                    rank_4_val2 = 4
                    rank_5_val2 = 1
                    rank_6_val2 = -63
                    rank_7_val2 = -63
                    rank_8_val2 = -60
                    rank_9_val2 = -58
                    rank_10_val2 = -57

                if 700 <= brawler_trophies <= 799:
                    win = 5
                    rank_1_val = 10
                    rank_2_val = 8
                    rank_3_val = 6
                    rank_4_val = 4
                    rank_5_val = 1
                    rank_6_val = -3
                    rank_7_val = -4
                    rank_8_val = -5
                    rank_9_val = -8
                    rank_10_val = -9

                    rank_1_val2 = 10
                    rank_2_val2 = 8
                    rank_3_val2 = 6
                    rank_4_val2 = 4
                    rank_5_val2 = 1
                    rank_6_val2 = -62
                    rank_7_val2 = -61
                    rank_8_val2 = -60
                    rank_9_val2 = -57
                    rank_10_val2 = -56

                if 800 <= brawler_trophies <= 899:
                    win = 4
                    rank_1_val = 9
                    rank_2_val = 7
                    rank_3_val = 5
                    rank_4_val = 2
                    rank_5_val = 0
                    rank_6_val = -3
                    rank_7_val = -4
                    rank_8_val = -7
                    rank_9_val = -9
                    rank_10_val = -10

                    rank_1_val2 = 9
                    rank_2_val2 = 7
                    rank_3_val2 = 5
                    rank_4_val2 = 2
                    rank_5_val2 = 0
                    rank_6_val2 = -62
                    rank_7_val2 = -61
                    rank_8_val2 = -58
                    rank_9_val2 = -56
                    rank_10_val2 = -55

                if 900 <= brawler_trophies <= 999:
                    win = 4
                    rank_1_val = 8
                    rank_2_val = 6
                    rank_3_val = 4
                    rank_4_val = 1
                    rank_5_val = -1
                    rank_6_val = -3
                    rank_7_val = -6
                    rank_8_val = -8
                    rank_9_val = -10
                    rank_10_val = -11

                    rank_1_val2 = 8
                    rank_2_val2 = 6
                    rank_3_val2 = 4
                    rank_4_val2 = 1
                    rank_5_val2 = -64
                    rank_6_val2 = -62
                    rank_7_val2 = -59
                    rank_8_val2 = -57
                    rank_9_val2 = -55
                    rank_10_val2 = -54

                if 1000 <= brawler_trophies <= 1099:
                    win = 4
                    rank_1_val = 6
                    rank_2_val = 5
                    rank_3_val = 3
                    rank_4_val = 1
                    rank_5_val = -2
                    rank_6_val = -5
                    rank_7_val = -6
                    rank_8_val = -9
                    rank_9_val = -11
                    rank_10_val = -12

                    rank_1_val2 = 6
                    rank_2_val2 = 5
                    rank_3_val2 = 3
                    rank_4_val2 = 1
                    rank_5_val2 = -63
                    rank_6_val2 = -60
                    rank_7_val2 = -59
                    rank_8_val2 = -56
                    rank_9_val2 = -54
                    rank_10_val2 = -53

                if 1100 <= brawler_trophies <= 1199:
                    win = 3
                    rank_1_val = 5
                    rank_2_val = 4
                    rank_3_val = 1
                    rank_4_val = 0
                    rank_5_val = -2
                    rank_6_val = -6
                    rank_7_val = -7
                    rank_8_val = -10
                    rank_9_val = -12
                    rank_10_val = -13

                    rank_1_val2 = 5
                    rank_2_val2 = 4
                    rank_3_val2 = 1
                    rank_4_val2 = 0
                    rank_5_val2 = -63
                    rank_6_val2 = -59
                    rank_7_val2 = -58
                    rank_8_val2 = -55
                    rank_9_val2 = -53
                    rank_10_val2 = -52

                if brawler_trophies >= 1200:
                    win = 2
                    rank_1_val = 5
                    rank_2_val = 3
                    rank_3_val = 0
                    rank_4_val = -1
                    rank_5_val = -2
                    rank_6_val = -6
                    rank_7_val = -8
                    rank_8_val = -11
                    rank_9_val = -12
                    rank_10_val = -13

                    rank_1_val2 = 5
                    rank_2_val2 = 3
                    rank_3_val2 = 0
                    rank_4_val2 = -64
                    rank_5_val2 = -63
                    rank_6_val2 = -59
                    rank_7_val2 = -57
                    rank_8_val2 = -54
                    rank_9_val2 = -53
                    rank_10_val2 = -52

        else:
            if 0 <= brawler_trophies <= 49:
                win = 8
                rank_1_val = 18
                rank_2_val = 14
                rank_3_val = 12
                rank_4_val = 10
                rank_5_val = 6
                rank_6_val = 4
                rank_7_val = 3
                rank_8_val = 2
                rank_9_val = 1
                rank_10_val = 0

                rank_1_val2 = 18
                rank_2_val2 = 14
                rank_3_val2 = 12
                rank_4_val2 = 10
                rank_5_val2 = 6
                rank_6_val2 = 4
                rank_7_val2 = 3
                rank_8_val2 = 2
                rank_9_val2 = 1
                rank_10_val2 = 0

            else:
                if 50 <= brawler_trophies <= 99:
                    win = 7
                    rank_1_val = 17
                    rank_2_val = 13
                    rank_3_val = 12
                    rank_4_val = 11
                    rank_5_val = 5
                    rank_6_val = 3
                    rank_7_val = 2
                    rank_8_val = 1
                    rank_9_val = -1
                    rank_10_val = -2

                    rank_1_val2 = 16
                    rank_2_val2 = 12
                    rank_3_val2 = 11
                    rank_4_val2 = 10
                    rank_5_val2 = 5
                    rank_6_val2 = 4
                    rank_7_val2 = 3
                    rank_8_val2 = 2
                    rank_9_val2 = -64
                    rank_10_val2 = -63

                if 100 <= brawler_trophies <= 199:
                    win = 6
                    rank_1_val = 15
                    rank_2_val = 11
                    rank_3_val = 10
                    rank_4_val = 9
                    rank_5_val = 5
                    rank_6_val = 2
                    rank_7_val = 1
                    rank_8_val = -1
                    rank_9_val = -2
                    rank_10_val = -2

                    rank_1_val2 = 15
                    rank_2_val2 = 11
                    rank_3_val2 = 10
                    rank_4_val2 = 9
                    rank_5_val2 = 5
                    rank_6_val2 = 2
                    rank_7_val2 = 1
                    rank_8_val2 = -64
                    rank_9_val2 = -63
                    rank_10_val2 = -63

                if 200 <= brawler_trophies <= 299:
                    win = 6
                    rank_1_val = 15
                    rank_2_val = 10
                    rank_3_val = 10
                    rank_4_val = 8
                    rank_5_val = 5
                    rank_6_val = 2
                    rank_7_val = 1
                    rank_8_val = -2
                    rank_9_val = -3
                    rank_10_val = -3

                    rank_1_val2 = 15
                    rank_2_val2 = 10
                    rank_3_val2 = 10
                    rank_4_val2 = 8
                    rank_5_val2 = 5
                    rank_6_val2 = 2
                    rank_7_val2 = 1
                    rank_8_val2 = -63
                    rank_9_val2 = -62
                    rank_10_val2 = -62

                if 300 <= brawler_trophies <= 399:
                    win = 5
                    rank_1_val = 15
                    rank_2_val = 10
                    rank_3_val = 10
                    rank_4_val = 8
                    rank_5_val = 5
                    rank_6_val = 2
                    rank_7_val = 1
                    rank_8_val = -3
                    rank_9_val = -4
                    rank_10_val = -4

                    rank_1_val2 = 15
                    rank_2_val2 = 10
                    rank_3_val2 = 10
                    rank_4_val2 = 8
                    rank_5_val2 = 5
                    rank_6_val2 = 2
                    rank_7_val2 = 1
                    rank_8_val2 = -62
                    rank_9_val2 = -61
                    rank_10_val2 = -61

                if 400 <= brawler_trophies <= 499:
                    win = 5
                    rank_1_val = 15
                    rank_2_val = 10
                    rank_3_val = 10
                    rank_4_val = 8
                    rank_5_val = 4
                    rank_6_val = -1
                    rank_7_val = -2
                    rank_8_val = -3
                    rank_9_val = -5
                    rank_10_val = -5

                    rank_1_val2 = 15
                    rank_2_val2 = 10
                    rank_3_val2 = 10
                    rank_4_val2 = 8
                    rank_5_val2 = 4
                    rank_6_val2 = -64
                    rank_7_val2 = -63
                    rank_8_val2 = -62
                    rank_9_val2 = -60
                    rank_10_val2 = -60

                if 500 <= brawler_trophies <= 599:
                    win = 5
                    rank_1_val = 15
                    rank_2_val = 10
                    rank_3_val = 10
                    rank_4_val = 8
                    rank_5_val = 4
                    rank_6_val = -1
                    rank_7_val = -2
                    rank_8_val = -5
                    rank_9_val = -6
                    rank_10_val = -6

                    rank_1_val2 = 15
                    rank_2_val2 = 10
                    rank_3_val2 = 10
                    rank_4_val2 = 7
                    rank_5_val2 = 3
                    rank_6_val2 = -64
                    rank_7_val2 = -63
                    rank_8_val2 = -60
                    rank_9_val2 = -59
                    rank_10_val2 = -59

                if 600 <= brawler_trophies <= 699:
                    win = 5
                    rank_1_val = 15
                    rank_2_val = 10
                    rank_3_val = 10
                    rank_4_val = 6
                    rank_5_val = 3
                    rank_6_val = -2
                    rank_7_val = -2
                    rank_8_val = -5
                    rank_9_val = -7
                    rank_10_val = -8

                    rank_1_val2 = 15
                    rank_2_val2 = 10
                    rank_3_val2 = 10
                    rank_4_val2 = 6
                    rank_5_val2 = 3
                    rank_6_val2 = -63
                    rank_7_val2 = -63
                    rank_8_val2 = -60
                    rank_9_val2 = -58
                    rank_10_val2 = -57

                if 700 <= brawler_trophies <= 799:
                    win = 5
                    rank_1_val = 15
                    rank_2_val = 10
                    rank_3_val = 10
                    rank_4_val = 6
                    rank_5_val = 3
                    rank_6_val = -3
                    rank_7_val = -4
                    rank_8_val = -5
                    rank_9_val = -8
                    rank_10_val = -9

                    rank_1_val2 = 15
                    rank_2_val2 = 10
                    rank_3_val2 = 10
                    rank_4_val2 = 6
                    rank_5_val2 = 3
                    rank_6_val2 = -62
                    rank_7_val2 = -61
                    rank_8_val2 = -60
                    rank_9_val2 = -57
                    rank_10_val2 = -56

                if 800 <= brawler_trophies <= 899:
                    win = 4
                    rank_1_val = 13
                    rank_2_val = 9
                    rank_3_val = 8
                    rank_4_val = 4
                    rank_5_val = 1
                    rank_6_val = -3
                    rank_7_val = -4
                    rank_8_val = -7
                    rank_9_val = -9
                    rank_10_val = -10

                    rank_1_val2 = 13
                    rank_2_val2 = 9
                    rank_3_val2 = 8
                    rank_4_val2 = 4
                    rank_5_val2 = 1
                    rank_6_val2 = -62
                    rank_7_val2 = -61
                    rank_8_val2 = -58
                    rank_9_val2 = -56
                    rank_10_val2 = -55

                if 900 <= brawler_trophies <= 999:
                    win = 4
                    rank_1_val = 13
                    rank_2_val = 9
                    rank_3_val = 7
                    rank_4_val = 3
                    rank_5_val = -1
                    rank_6_val = -3
                    rank_7_val = -6
                    rank_8_val = -8
                    rank_9_val = -10
                    rank_10_val = -11

                    rank_1_val2 = 13
                    rank_2_val2 = 9
                    rank_3_val2 = 7
                    rank_4_val2 = 3
                    rank_5_val2 = -64
                    rank_6_val2 = -62
                    rank_7_val2 = -59
                    rank_8_val2 = -57
                    rank_9_val2 = -55
                    rank_10_val2 = -54

                if 1000 <= brawler_trophies <= 1099:
                    win = 4
                    rank_1_val = 11
                    rank_2_val = 8
                    rank_3_val = 5
                    rank_4_val = 3
                    rank_5_val = -2
                    rank_6_val = -5
                    rank_7_val = -6
                    rank_8_val = -9
                    rank_9_val = -11
                    rank_10_val = -12

                    rank_1_val2 = 10
                    rank_2_val2 = 7
                    rank_3_val2 = 4
                    rank_4_val2 = 2
                    rank_5_val2 = -63
                    rank_6_val2 = -60
                    rank_7_val2 = -59
                    rank_8_val2 = -56
                    rank_9_val2 = -54
                    rank_10_val2 = -53

                if 1100 <= brawler_trophies <= 1199:
                    win = 3
                    rank_1_val = 9
                    rank_2_val = 7
                    rank_3_val = 4
                    rank_4_val = 2
                    rank_5_val = -2
                    rank_6_val = -6
                    rank_7_val = -7
                    rank_8_val = -10
                    rank_9_val = -12
                    rank_10_val = -13

                    rank_1_val2 = 9
                    rank_2_val2 = 7
                    rank_3_val2 = 3
                    rank_4_val2 = 1
                    rank_5_val2 = -63
                    rank_6_val2 = -59
                    rank_7_val2 = -58
                    rank_8_val2 = -55
                    rank_9_val2 = -53
                    rank_10_val2 = -52

                if brawler_trophies >= 1200:
                    win = 2
                    rank_1_val = 8
                    rank_2_val = 6
                    rank_3_val = 3
                    rank_4_val = -1
                    rank_5_val = -2
                    rank_6_val = -6
                    rank_7_val = -8
                    rank_8_val = -11
                    rank_9_val = -12
                    rank_10_val = -13

                    rank_1_val2 = 7
                    rank_2_val2 = 5
                    rank_3_val2 = 2
                    rank_4_val2 = -64
                    rank_5_val2 = -63
                    rank_6_val2 = -59
                    rank_7_val2 = -57
                    rank_8_val2 = -54
                    rank_9_val2 = -53
                    rank_10_val2 = -52
        if self.player.GameType == 1:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_1_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_1_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_1_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_1_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_1_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_1_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_1_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_1_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_1_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_1_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_1_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_1_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_1_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_1_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_1_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_1_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_1_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_1_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_1_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_1_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_1_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_1_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_1_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_1_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_1_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_1_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_1_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_1_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_1_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_1_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_1_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_1_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_1_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_1_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_1_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_1_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_1_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_1_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_1_val2
            xp = (5000)
            result = (17)
            tokens = (32)
            checldoubled = (20)
            eventdoubled = (40)
            totaltokens = (80)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_1_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            ##self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_1_val
            goldgetted = (30)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 2:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_2_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_2_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_2_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_2_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_2_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_2_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_2_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_2_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_2_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_2_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_2_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_2_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_2_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_2_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_2_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_2_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_2_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_2_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_2_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_2_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_2_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_2_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_2_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_2_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_2_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_2_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_2_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_2_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_2_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_2_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_2_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_2_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_2_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_2_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_2_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_2_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_2_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_2_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_2_val2
            xp = (5000)
            result = (17)
            tokens = (25)
            checldoubled = (20)
            eventdoubled = (40)
            totaltokens = (80)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_2_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_2_val
            goldgetted = (30)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 3:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_3_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_3_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_3_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_3_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_3_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_3_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_3_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_3_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_3_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_3_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_3_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_3_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_3_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_3_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_3_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_3_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_3_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_3_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_3_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_3_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_3_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_3_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_3_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_3_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_3_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_3_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_3_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_3_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_3_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_3_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_3_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_3_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_3_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_3_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_3_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_3_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_3_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_3_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_3_val2
            xp = (5000)
            result = (17)
            tokens = (25)
            checldoubled = (20)
            eventdoubled = (40)
            totaltokens = (80)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_3_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_3_val
            goldgetted = (30)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 4:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_4_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_4_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_4_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_4_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_4_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_4_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_4_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_4_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_4_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_4_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_4_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_4_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_4_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_4_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_4_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_4_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_4_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_4_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_4_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_4_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_4_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_4_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_4_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_4_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_4_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_4_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_4_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_4_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_4_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_4_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_4_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_4_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_4_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_4_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_4_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_4_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_4_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_4_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_4_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_4_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_4_val
            goldgetted = (20)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 5:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_5_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_5_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_5_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_5_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_5_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_5_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_5_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_5_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_5_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_5_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_5_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_5_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_5_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_5_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_5_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_5_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_5_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_5_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_5_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_5_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_5_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_5_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_5_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_5_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_5_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_5_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_5_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_5_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_5_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_5_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_5_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_5_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_5_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_5_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_5_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_5_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_5_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_5_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_5_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_5_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_5_val
            goldgetted = (10)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 6:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_6_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_6_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_6_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_6_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_6_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_6_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_6_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_6_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_6_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_6_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_6_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_6_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_6_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_6_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_6_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_6_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_6_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_6_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_6_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_6_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_6_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_6_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_6_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_6_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_6_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_6_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_6_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_6_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_6_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_6_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_6_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_6_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_6_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_6_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_6_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_6_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_6_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_6_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_6_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_6_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_6_val
            goldgetted = (10)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)


        elif self.player.GameType == 7:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_7_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_7_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_7_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_7_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_7_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_7_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_7_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_7_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_7_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_7_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_7_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_7_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_7_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_7_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_7_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_7_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_7_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_7_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_7_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_7_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_7_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_7_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_7_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_7_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_7_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_7_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_7_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_7_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_7_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_7_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_7_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_7_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_7_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_7_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_7_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_7_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_7_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_7_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_7_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_7_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_7_val
            goldgetted = (10)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 8:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_8_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_8_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_8_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_8_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_8_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_8_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_8_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_8_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_8_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_8_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_8_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_8_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_8_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_8_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_8_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_8_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_8_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_8_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_8_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_8_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_8_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_8_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_8_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_8_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_8_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_8_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_8_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_8_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_8_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_8_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_8_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_8_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_8_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_8_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_8_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_8_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_8_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_8_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_8_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_8_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_8_val
            goldgetted = (10)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 9:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_9_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_9_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_9_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_9_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_9_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_9_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_9_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_9_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_9_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_9_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_9_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_9_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_9_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_9_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_9_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_9_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_9_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_9_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_9_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_9_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_9_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_9_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_9_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_9_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_9_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_9_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_9_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_9_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_9_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_9_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_9_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_9_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_9_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_9_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_9_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_9_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_9_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_9_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_9_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_9_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_9_val
            goldgetted = (10)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)

        elif self.player.GameType == 10:
            if self.player.brawlerID == 0:
            	if self.player.shellytrophiesrank < self.player.shellytrophies:
            	    self.player.shellytrophiesrank = self.player.shellytrophies
            	brawler_trophies_win = self.player.shellytrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.shellytrophies + rank_10_val
            	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 1:
            	if self.player.colttrophiesrank < self.player.colttrophies:
            	    self.player.colttrophiesrank = self.player.colttrophies
            	brawler_trophies_win = self.player.colttrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.colttrophies  + rank_10_val
            	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 2:
            	if self.player.bulltrophiesrank < self.player.bulltrophies:
            	    self.player.bulltrophiesrank = self.player.bulltrophies
            	brawler_trophies_win = self.player.bulltrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.bulltrophies + rank_10_val
            	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 3:
            	if self.player.brocktrophiesrank < self.player.brocktrophies:
            	    self.player.brocktrophiesrank = self.player.brocktrophies
            	brawler_trophies_win = self.player.brocktrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.brocktrophies + rank_10_val
            	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 4:
            	if self.player.ricotrophiesrank < self.player.ricotrophies:
            	    self.player.ricotrophiesrank = self.player.ricotrophies
            	brawler_trophies_win = self.player.ricotrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.ricotrophies + rank_10_val
            	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 5:
            	if self.player.spiketrophiesrank < self.player.spiketrophies:
            	    self.player.spiketrophiesrank = self.player.spiketrophies
            	brawler_trophies_win = self.player.spiketrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.spiketrophies + rank_10_val
            	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 6:
            	if self.player.barleytrophiesrank < self.player.barleytrophies:
            	    self.player.barleytrophiesrank = self.player.barleytrophies
            	brawler_trophies_win = self.player.barleytrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.barleytrophies + rank_10_val
            	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 7:
            	if self.player.jessietrophiesrank < self.player.jessietrophies:
            	    self.player.jessietrophiesrank = self.player.jessietrophies
            	brawler_trophies_win = self.player.jessietrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.jessietrophies + rank_10_val
            	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 8:
            	if self.player.nitatrophiesrank < self.player.nitatrophies:
            	    self.player.nitatrophiesrank = self.player.nitatrophies
            	brawler_trophies_win = self.player.nitatrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.nitatrophies + rank_10_val
            	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 9:
            	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
            	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.dynamiketrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.dynamiketrophies + rank_10_val
            	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 10:
            	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
            	    self.player.elprimotrophiesrank = self.player.elprimotrophies
            	brawler_trophies_win = self.player.elprimotrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.elprimotrophies + rank_10_val
            	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 11:
            	if self.player.mortistrophiesrank < self.player.mortistrophies:
            	    self.player.mortistrophiesrank = self.player.mortistrophies
            	brawler_trophies_win = self.player.mortistrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.mortistrophies + rank_10_val
            	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 12:
            	if self.player.crowtrophiesrank < self.player.crowtrophies:
            	    self.player.crowtrophiesrank = self.player.crowtrophies
            	brawler_trophies_win = self.player.crowtrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.crowtrophies + rank_10_val
            	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 13:
            	if self.player.pocotrophiesrank < self.player.pocotrophies:
            	    self.player.pocotrophiesrank = self.player.pocotrophies
            	brawler_trophies_win = self.player.pocotrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.pocotrophies + rank_10_val
            	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 14:
            	if self.player.botrophiesrank < self.player.botrophies:
            	    self.player.botrophiesrank = self.player.botrophies
            	brawler_trophies_win = self.player.botrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.botrophies + rank_10_val
            	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 15:
            	if self.player.pipertrophiesrank < self.player.pipertrophies:
            	    self.player.pipertrophiesrank = self.player.pipertrophies
            	brawler_trophies_win = self.player.pipertrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.pipertrophies + rank_10_val
            	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 16:
            	if self.player.pamtrophiesrank < self.player.pamtrophies:
            	    self.player.pamtrophiesrank = self.player.pamtrophies
            	brawler_trophies_win = self.player.pamtrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.pamtrophies + rank_10_val
            	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 17:
            	if self.player.taratrophiesrank < self.player.taratrophies:
            	    self.player.taratrophiesrank = self.player.taratrophies
            	brawler_trophies_win = self.player.taratrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.taratrophies + rank_10_val
            	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 18:
            	if self.player.darryltrophiesrank < self.player.darryltrophies:
            	    self.player.darryltrophiesrank = self.player.darryltrophies
            	brawler_trophies_win = self.player.darryltrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.darryltrophies + rank_10_val
            	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 19:
            	if self.player.pennytrophiesrank < self.player.pennytrophies:
            	    self.player.pennytrophiesrank = self.player.pennytrophies
            	brawler_trophies_win = self.player.pennytrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.pennytrophies + rank_10_val
            	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 20:
            	if self.player.franktrophiesrank < self.player.franktrophies:
            	    self.player.franktrophiesrank = self.player.franktrophies
            	brawler_trophies_win = self.player.franktrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.franktrophies + rank_10_val
            	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 21:
            	if self.player.genetrophiesrank < self.player.genetrophies:
            	    self.player.genetrophiesrank = self.player.genetrophies
            	brawler_trophies_win = self.player.genetrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.genetrophies + rank_10_val
            	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 22:
            	if self.player.ticktrophiesrank < self.player.ticktrophies:
            	    self.player.ticktrophiesrank = self.player.ticktrophies
            	brawler_trophies_win = self.player.ticktrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.ticktrophies + rank_10_val
            	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 23:
            	if self.player.leontrophiesrank < self.player.leontrophies:
            	    self.player.leontrophiesrank = self.player.leontrophies
            	brawler_trophies_win = self.player.leontrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.leontrophies + rank_10_val
            	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 24:
            	if self.player.rosatrophiesrank < self.player.rosatrophies:
            	    self.player.rosatrophiesrank = self.player.rosatrophies
            	brawler_trophies_win = self.player.rosatrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.rosatrophies + rank_10_val
            	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 25:
            	if self.player.carltrophiesrank < self.player.carltrophies:
            	    self.player.carltrophiesrank = self.player.carltrophies
            	brawler_trophies_win = self.player.carltrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.carltrophies + rank_10_val
            	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 26:
            	if self.player.bibitrophiesrank < self.player.bibitrophies:
            	    self.player.bibitrophiesrank = self.player.bibitrophies
            	brawler_trophies_win = self.player.bibitrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.bibitrophies + rank_10_val
            	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 27:
            	if self.player.bittrophiesrank < self.player.bittrophies:
            	    self.player.bittrophiesrank = self.player.bittrophies
            	brawler_trophies_win = self.player.bittrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.bittrophies + rank_10_val
            	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 28:
            	if self.player.sandytrophiesrank < self.player.sandytrophies:
            	    self.player.sandytrophiesrank = self.player.sandytrophies
            	brawler_trophies_win = self.player.sandytrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.sandytrophies + rank_10_val
            	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 29:
            	if self.player.beatrophiesrank < self.player.beatrophies:
            	    self.player.beatrophiesrank = self.player.beatrophies
            	brawler_trophies_win = self.player.beatrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.beatrophies + rank_10_val
            	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 30:
            	if self.player.emztrophiesrank < self.player.emztrophies:
            	    self.player.emztrophiesrank = self.player.emztrophies
            	brawler_trophies_win = self.player.emztrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.emztrophies + rank_10_val
            	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 31:
            	if self.player.mrptrophiesrank < self.player.mrptrophies:
            	    self.player.mrptrophiesrank = self.player.mrptrophies
            	brawler_trophies_win = self.player.mrptrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.mrptrophies + rank_10_val
            	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 32:
            	if self.player.maxtrophiesrank < self.player.maxtrophies:
            	    self.player.maxtrophiesrank = self.player.maxtrophies
            	brawler_trophies_win = self.player.maxtrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.maxtrophies + rank_10_val
            	DataBase.replaceValue(self, 'maxtrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'maxtrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Макс\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 33:
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, 'Серверная ошибка: 404').send()
            elif self.player.brawlerID == 34:
            	if self.player.jackytrophiesrank < self.player.jackytrophies:
            	    self.player.jackytrophiesrank = self.player.jackytrophies
            	brawler_trophies_win = self.player.jackytrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.jackytrophies + rank_10_val
            	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 35:
            	if self.player.galetrophiesrank < self.player.galetrophies:
            	    self.player.galetrophiesrank = self.player.galetrophies
            	brawler_trophies_win = self.player.galetrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.galetrophies + rank_10_val
            	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 36:
            	if self.player.nanitrophiesrank < self.player.nanitrophies:
            	    self.player.nanitrophiesrank = self.player.nanitrophies
            	brawler_trophies_win = self.player.nanitrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.nanitrophies + rank_10_val
            	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
            	time.sleep(2)
            	self.player.err_code = 1
            	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
            elif self.player.brawlerID == 37:
            	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
            	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
            	brawler_trophies_win = self.player.sprouttrophies + rank_10_val
            	brawler_trophies_for_rank = self.player.sprouttrophies + rank_10_val
            	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
            	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            trophies = rank_10_val2
            xp = (5000)
            result = (17)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (5)
            new_trophies = self.player.trophies + rank_10_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + rank_10_val
            goldgetted = (10)
            new_gold = self.player.gold + goldgetted
            DataBase.replaceValue(self, 'gold', new_gold)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)
        
        else:
            trophies = (1)
            xp = (5000)
            result = (17)
            tokens = (0)
            checldoubled = (0)
            eventdoubled = (0)
            totaltokens = (0)
            starplayer = (5)
            new_trophies = self.player.trophies + (1)
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)

        self.writeVint(tokens) #Battle Tokens 
        self.writeVint(trophies) #Trophies Value
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
        self.writeVint(goldgetted) #Coin Shower Event
        self.writeVint(0) #Underdog (This thing breaks everything)
        self.writeVint(17) #End Screen Type
        self.writeVint(1) # Championship Type
        self.writeVint(2) #Play Again
        
        self.writeVint(6) #Battle End Screen Players
        
        self.writeVint(starplayer)
        self.writeVint(16) # Brawler CsvID
        self.writeVint(self.player.brawlerID)
        self.writeVint(29)
        self.writeVint(self.player.skinID)
        self.writeVint(brawler_trophies) #Trophies
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
        self.writeVint(namecolor) #Name Color
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
        self.writeVint(brawler_trophies)
        self.writeVint(brawler_trophies)
        self.writeVint(5) # Experience Milestone
        self.writeVint(5000)