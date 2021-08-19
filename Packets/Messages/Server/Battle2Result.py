from Utils.Writer import Writer
from database.DataBase import DataBase
import time

class Battle2Result(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):from Utils.Writer import Writer
from database.DataBase import DataBase


class Battle2Result(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(self.player.GameType)
        print(self.player.GameType)
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
        	brawler_trophies = self.player.rozatrophies
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

        ticketscheckduo = DataBase.getVal(self, 'tickets')
        if self.requested_val != 6392:
            if 0 <= brawler_trophies <= 49:
                win_val = 8
                lose_val = 0
                lose_val2 = 0

            else:
                if 50 <= brawler_trophies <= 99:
                    win_val = 8
                    lose_val = -1
                    lose_val2 = -64

                if 100 <= brawler_trophies <= 199:
                    win_val = 8
                    lose_val = -2
                    lose_val2 = -63

                if 200 <= brawler_trophies <= 299:
                    win_val = 8
                    lose_val = -3
                    lose_val2 = -62

                if 300 <= brawler_trophies <= 399:
                    win_val = 8
                    lose_val = -4
                    lose_val2 = -61

                if 400 <= brawler_trophies <= 499:
                    win_val = 8
                    lose_val = -5
                    lose_val2 = -60

                if 500 <= brawler_trophies <= 599:
                    win_val = 8
                    lose_val = -6
                    lose_val2 = -59

                if 600 <= brawler_trophies <= 699:
                    win_val = 7
                    lose_val = -7
                    lose_val2 = -58

                if 700 <= brawler_trophies <= 799:
                    win_val = 7
                    lose_val = -8
                    lose_val2 = -57

                if 800 <= brawler_trophies <= 899:
                    win_val = 7
                    lose_val = -9
                    lose_val2 = -56

                if 900 <= brawler_trophies <= 999:
                    win_val = 6
                    lose_val = -10
                    lose_val2 = -55

                if 1000 <= brawler_trophies <= 1099:
                    win_val = 5
                    lose_val = -11
                    lose_val2 = -54

                if 1100 <= brawler_trophies <= 1199:
                    win_val = 4
                    lose_val = -12
                    lose_val2 = -53

                if brawler_trophies >= 1200:
                    win_val = 3
                    lose_val = -12
                    lose_val2 = -53

        elif self.requested_val == 6392:
            if 0 <= brawler_trophies <= 49:
                win_val = 16
                lose_val = 0
                lose_val2 = 0

            else:
                if 50 <= brawler_trophies <= 99:
                    win_val = 15
                    lose_val = -1
                    lose_val2 = -64

                if 100 <= brawler_trophies <= 199:
                    win_val = 14
                    lose_val = -2
                    lose_val2 = -63

                if 200 <= brawler_trophies <= 299:
                    win_val = 13
                    lose_val = -3
                    lose_val2 = -62

                if 300 <= brawler_trophies <= 399:
                    win_val = 12
                    lose_val = -4
                    lose_val2 = -61

                if 400 <= brawler_trophies <= 499:
                    win_val = 12
                    lose_val = -5
                    lose_val2 = -60

                if 500 <= brawler_trophies <= 599:
                    win_val = 12
                    lose_val = -6
                    lose_val2 = -59

                if 600 <= brawler_trophies <= 699:
                    win_val = 12
                    lose_val = -7
                    lose_val2 = -58

                if 700 <= brawler_trophies <= 799:
                    win_val = 12
                    lose_val = -8
                    lose_val2 = -57

                if 800 <= brawler_trophies <= 899:
                    win_val = 11
                    lose_val = -9
                    lose_val2 = -56

                if 900 <= brawler_trophies <= 999:
                    win_val = 10
                    lose_val = -10
                    lose_val2 = -55

                if 1000 <= brawler_trophies <= 1099:
                    win_val = 9
                    lose_val = -11
                    lose_val2 = -54

                if 1100 <= brawler_trophies <= 1199:
                    win_val = 7
                    lose_val = -12
                    lose_val2 = -53

                if brawler_trophies >= 1200:
                    win_val = 4
                    lose_val = -12
                    lose_val2 = -53
        if self.player.GameType == 0:
            trophiesend = win_val
            xp = (5000)
            result = (17)
            tokens = (32)
            checldoubled = (20)
            eventdoubled = (40)
            totaltokens = (80)
            starplayer = (5)
            new_trophies = self.player.trophies + win_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            #new_startokens = self.player.big_boxes + (1)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + win_val
            goldgetted = (0)
            #new_gold = self.player.gold + goldgetted
            #DataBase.replaceValue(self, 'gold', new_gold)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("errdb")
        if self.player.brawlerID == 0:
        	if self.player.shellytrophiesrank < self.player.shellytrophies:
        	    self.player.shellytrophiesrank = self.player.shellytrophies
        	brawler_trophies_win = self.player.shellytrophies + win_val
        	brawler_trophies_for_rank = self.player.shellytrophies + win_val
        	DataBase.replaceValue(self, 'shellytrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'shellytrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Шелли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 1:
        	if self.player.colttrophiesrank < self.player.colttrophies:
        	    self.player.colttrophiesrank = self.player.colttrophies
        	brawler_trophies_win = self.player.colttrophies + win_val
        	brawler_trophies_for_rank = self.player.colttrophies  + win_val
        	DataBase.replaceValue(self, 'colttrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'colttrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Кольт\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 2:
        	if self.player.bulltrophiesrank < self.player.bulltrophies:
        	    self.player.bulltrophiesrank = self.player.bulltrophies
        	brawler_trophies_win = self.player.bulltrophies + win_val
        	brawler_trophies_for_rank = self.player.bulltrophies + win_val
        	DataBase.replaceValue(self, 'bulltrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'bulltrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Булл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 3:
        	if self.player.brocktrophiesrank < self.player.brocktrophies:
        	    self.player.brocktrophiesrank = self.player.brocktrophies
        	brawler_trophies_win = self.player.brocktrophies + win_val
        	brawler_trophies_for_rank = self.player.brocktrophies + win_val
        	DataBase.replaceValue(self, 'brocktrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'brocktrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Брок\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 4:
        	if self.player.ricotrophiesrank < self.player.ricotrophies:
        	    self.player.ricotrophiesrank = self.player.ricotrophies
        	brawler_trophies_win = self.player.ricotrophies + win_val
        	brawler_trophies_for_rank = self.player.ricotrophies + win_val
        	DataBase.replaceValue(self, 'ricotrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'ricotrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Рико\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 5:
        	if self.player.spiketrophiesrank < self.player.spiketrophies:
        	    self.player.spiketrophiesrank = self.player.spiketrophies
        	brawler_trophies_win = self.player.spiketrophies + win_val
        	brawler_trophies_for_rank = self.player.spiketrophies + win_val
        	DataBase.replaceValue(self, 'spiketrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'spiketrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Спайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 6:
        	if self.player.barleytrophiesrank < self.player.barleytrophies:
        	    self.player.barleytrophiesrank = self.player.barleytrophies
        	brawler_trophies_win = self.player.barleytrophies + win_val
        	brawler_trophies_for_rank = self.player.barleytrophies + win_val
        	DataBase.replaceValue(self, 'barleytrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'barleytrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Барли\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 7:
        	if self.player.jessietrophiesrank < self.player.jessietrophies:
        	    self.player.jessietrophiesrank = self.player.jessietrophies
        	brawler_trophies_win = self.player.jessietrophies + win_val
        	brawler_trophies_for_rank = self.player.jessietrophies + win_val
        	DataBase.replaceValue(self, 'jessietrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'jessietrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джесси\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 8:
        	if self.player.nitatrophiesrank < self.player.nitatrophies:
        	    self.player.nitatrophiesrank = self.player.nitatrophies
        	brawler_trophies_win = self.player.nitatrophies + win_val
        	brawler_trophies_for_rank = self.player.nitatrophies + win_val
        	DataBase.replaceValue(self, 'nitatrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'nitatrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нита\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 9:
        	if self.player.dynamiketrophiesrank < self.player.dynamiketrophies:
        	    self.player.dynamiketrophiesrank = self.player.dynamiketrophies
        	brawler_trophies_win = self.player.dynamiketrophies + win_val
        	brawler_trophies_for_rank = self.player.dynamiketrophies + win_val
        	DataBase.replaceValue(self, 'dynamiketrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'dynamiketrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Диномайк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 10:
        	if self.player.elprimotrophiesrank < self.player.elprimotrophies:
        	    self.player.elprimotrophiesrank = self.player.elprimotrophies
        	brawler_trophies_win = self.player.elprimotrophies + win_val
        	brawler_trophies_for_rank = self.player.elprimotrophies + win_val
        	DataBase.replaceValue(self, 'elprimotrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'elprimotrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эль Примо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 11:
        	if self.player.mortistrophiesrank < self.player.mortistrophies:
        	    self.player.mortistrophiesrank = self.player.mortistrophies
        	brawler_trophies_win = self.player.mortistrophies + win_val
        	brawler_trophies_for_rank = self.player.mortistrophies + win_val
        	DataBase.replaceValue(self, 'mortistrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'mortistrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Мортис\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 12:
        	if self.player.crowtrophiesrank < self.player.crowtrophies:
        	    self.player.crowtrophiesrank = self.player.crowtrophies
        	brawler_trophies_win = self.player.crowtrophies + win_val
        	brawler_trophies_for_rank = self.player.crowtrophies + win_val
        	DataBase.replaceValue(self, 'crowtrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'crowtrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Ворон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 13:
        	if self.player.pocotrophiesrank < self.player.pocotrophies:
        	    self.player.pocotrophiesrank = self.player.pocotrophies
        	brawler_trophies_win = self.player.pocotrophies + win_val
        	brawler_trophies_for_rank = self.player.pocotrophies + win_val
        	DataBase.replaceValue(self, 'pocotrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'pocotrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Поко\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 14:
        	if self.player.botrophiesrank < self.player.botrophies:
        	    self.player.botrophiesrank = self.player.botrophies
        	brawler_trophies_win = self.player.botrophies + win_val
        	brawler_trophies_for_rank = self.player.botrophies + win_val
        	DataBase.replaceValue(self, 'botrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'botrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Бо\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 15:
        	if self.player.pipertrophiesrank < self.player.pipertrophies:
        	    self.player.pipertrophiesrank = self.player.pipertrophies
        	brawler_trophies_win = self.player.pipertrophies + win_val
        	brawler_trophies_for_rank = self.player.pipertrophies + win_val
        	DataBase.replaceValue(self, 'pipertrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'pipertrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пайпер\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 16:
        	if self.player.pamtrophiesrank < self.player.pamtrophies:
        	    self.player.pamtrophiesrank = self.player.pamtrophies
        	brawler_trophies_win = self.player.pamtrophies + win_val
        	brawler_trophies_for_rank = self.player.pamtrophies + win_val
        	DataBase.replaceValue(self, 'pamtrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'pamtrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пэм\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 17:
        	if self.player.taratrophiesrank < self.player.taratrophies:
        	    self.player.taratrophiesrank = self.player.taratrophies
        	brawler_trophies_win = self.player.taratrophies + win_val
        	brawler_trophies_for_rank = self.player.taratrophies + win_val
        	DataBase.replaceValue(self, 'taratrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'taratrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тара\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 18:
        	if self.player.darryltrophiesrank < self.player.darryltrophies:
        	    self.player.darryltrophiesrank = self.player.darryltrophies
        	brawler_trophies_win = self.player.darryltrophies + win_val
        	brawler_trophies_for_rank = self.player.darryltrophies + win_val
        	DataBase.replaceValue(self, 'darryltrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'darryltrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Дэррил\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 19:
        	if self.player.pennytrophiesrank < self.player.pennytrophies:
        	    self.player.pennytrophiesrank = self.player.pennytrophies
        	brawler_trophies_win = self.player.pennytrophies + win_val
        	brawler_trophies_for_rank = self.player.pennytrophies + win_val
        	DataBase.replaceValue(self, 'pennytrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'pennytrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Пенни\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 20:
        	if self.player.franktrophiesrank < self.player.franktrophies:
        	    self.player.franktrophiesrank = self.player.franktrophies
        	brawler_trophies_win = self.player.franktrophies + win_val
        	brawler_trophies_for_rank = self.player.franktrophies + win_val
        	DataBase.replaceValue(self, 'franktrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'franktrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Фрэнк\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 21:
        	if self.player.genetrophiesrank < self.player.genetrophies:
        	    self.player.genetrophiesrank = self.player.genetrophies
        	brawler_trophies_win = self.player.genetrophies + win_val
        	brawler_trophies_for_rank = self.player.genetrophies + win_val
        	DataBase.replaceValue(self, 'genetrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'genetrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джин\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 22:
        	if self.player.ticktrophiesrank < self.player.ticktrophies:
        	    self.player.ticktrophiesrank = self.player.ticktrophies
        	brawler_trophies_win = self.player.ticktrophies + win_val
        	brawler_trophies_for_rank = self.player.ticktrophies + win_val
        	DataBase.replaceValue(self, 'ticktrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'ticktrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Тик\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 23:
        	if self.player.leontrophiesrank < self.player.leontrophies:
        	    self.player.leontrophiesrank = self.player.leontrophies
        	brawler_trophies_win = self.player.leontrophies + win_val
        	brawler_trophies_for_rank = self.player.leontrophies + win_val
        	DataBase.replaceValue(self, 'leontrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'leontrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Леон\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 24:
        	if self.player.rosatrophiesrank < self.player.rosatrophies:
        	    self.player.rosatrophiesrank = self.player.rosatrophies
        	brawler_trophies_win = self.player.rosatrophies + win_val
        	brawler_trophies_for_rank = self.player.rosatrophies + win_val
        	DataBase.replaceValue(self, 'rosatrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'rosatrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Роза\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 25:
        	if self.player.carltrophiesrank < self.player.carltrophies:
        	    self.player.carltrophiesrank = self.player.carltrophies
        	brawler_trophies_win = self.player.carltrophies + win_val
        	brawler_trophies_for_rank = self.player.carltrophies + win_val
        	DataBase.replaceValue(self, 'carltrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'carltrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Карл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 26:
        	if self.player.bibitrophiesrank < self.player.bibitrophies:
        	    self.player.bibitrophiesrank = self.player.bibitrophies
        	brawler_trophies_win = self.player.bibitrophies + win_val
        	brawler_trophies_for_rank = self.player.bibitrophies + win_val
        	DataBase.replaceValue(self, 'bibitrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'bibitrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Биби\n\nПослание от разраба: Кто купит мне туалетную бумагу получит 100$\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 27:
        	if self.player.bittrophiesrank < self.player.bittrophies:
        	    self.player.bittrophiesrank = self.player.bittrophies
        	brawler_trophies_win = self.player.bittrophies + win_val
        	brawler_trophies_for_rank = self.player.bittrophies + win_val
        	DataBase.replaceValue(self, '8bittrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, '8bittrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - 8-Бит\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 28:
        	if self.player.sandytrophiesrank < self.player.sandytrophies:
        	    self.player.sandytrophiesrank = self.player.sandytrophies
        	brawler_trophies_win = self.player.sandytrophies + win_val
        	brawler_trophies_for_rank = self.player.sandytrophies + win_val
        	DataBase.replaceValue(self, 'sandytrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'sandytrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Сэнди\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 29:
        	if self.player.beatrophiesrank < self.player.beatrophies:
        	    self.player.beatrophiesrank = self.player.beatrophies
        	brawler_trophies_win = self.player.beatrophies + win_val
        	brawler_trophies_for_rank = self.player.beatrophies + win_val
        	DataBase.replaceValue(self, 'beatrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'beatrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Беа\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 30:
        	if self.player.emztrophiesrank < self.player.emztrophies:
        	    self.player.emztrophiesrank = self.player.emztrophies
        	brawler_trophies_win = self.player.emztrophies + win_val
        	brawler_trophies_for_rank = self.player.emztrophies + win_val
        	DataBase.replaceValue(self, 'emztrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'emztrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Эмз\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 31:
        	if self.player.mrptrophiesrank < self.player.mrptrophies:
        	    self.player.mrptrophiesrank = self.player.mrptrophies
        	brawler_trophies_win = self.player.mrptrophies + win_val
        	brawler_trophies_for_rank = self.player.mrptrophies + win_val
        	DataBase.replaceValue(self, 'mrptrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'mrptrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Mr.P\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 32:
        	if self.player.maxtrophiesrank < self.player.maxtrophies:
        	    self.player.maxtrophiesrank = self.player.maxtrophies
        	brawler_trophies_win = self.player.maxtrophies + win_val
        	brawler_trophies_for_rank = self.player.maxtrophies + win_val
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
        	brawler_trophies_win = self.player.jackytrophies + win_val
        	brawler_trophies_for_rank = self.player.jackytrophies + win_val
        	DataBase.replaceValue(self, 'jackytrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'jackytrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Джекки\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 35:
        	if self.player.galetrophiesrank < self.player.galetrophies:
        	    self.player.galetrophiesrank = self.player.galetrophies
        	brawler_trophies_win = self.player.galetrophies + win_val
        	brawler_trophies_for_rank = self.player.galetrophies + win_val
        	DataBase.replaceValue(self, 'galetrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'galetrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Гэйл\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 36:
        	if self.player.nanitrophiesrank < self.player.nanitrophies:
        	    self.player.nanitrophiesrank = self.player.nanitrophies
        	brawler_trophies_win = self.player.nanitrophies + win_val
        	brawler_trophies_for_rank = self.player.nanitrophies + win_val
        	DataBase.replaceValue(self, 'nanitrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'nanitrophies', brawler_trophies_win)
        	time.sleep(2)
        	self.player.err_code = 1
        	#LoginFailedMessage(self.client, self.player, '+8 кубков!\n+50 монет!\n+3 гемов!\nВыбранный бравлер - Нани\n\nСпасибо что играете в MoonBrawl!\nВерсия: 1.02').send()
        elif self.player.brawlerID == 37:
        	if self.player.sprouttrophiesrank < self.player.dynamiketrophies:
        	    self.player.sprouttrophiesrank = self.player.dynamiketrophies
        	brawler_trophies_win = self.player.sprouttrophies + win_val
        	brawler_trophies_for_rank = self.player.sprouttrophies + win_val
        	DataBase.replaceValue(self, 'sprouttrophiesrank', brawler_trophies_for_rank)
        	DataBase.replaceValue(self, 'sprouttrophies', brawler_trophies_win)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
            #DataBase.replaceValue(self, 'bigBoxes', new_startokens)
            
        if self.player.GameType == 1:
            trophiesend = lose_val2
            new_trophies = self.player.trophies + lose_val
            if self.player.brawlerID == 0:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'shellytrophies', newtrop) #shellytrophies
            elif self.player.brawlerID == 1:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'colttrophies', newtrop) #colttrophies
            elif self.player.brawlerID == 2:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'bulltrophies', newtrop) #bulltrophies
            elif self.player.brawlerID == 3:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'brocktrophies', newtrop) #brocktrophies
            elif self.player.brawlerID == 4:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'ricotrophies', newtrop) #ricotrophies
            elif self.player.brawlerID == 5:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'spiketrophies', newtrop) #spiketrophies
            elif self.player.brawlerID == 6:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'barleytrophies', newtrop) #barleytrophies
            elif self.player.brawlerID == 7:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'jessietrophies', newtrop) #jessietrophies
            elif self.player.brawlerID == 8:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'nitatrophies', newtrop) #nitatrophies
            elif self.player.brawlerID == 9:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'dynamiketrophies', newtrop) #dynamiketrophies
            elif self.player.brawlerID == 10:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'elprimotrophies', newtrop) #elprimotrophies
            elif self.player.brawlerID == 11:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'mortistrophies', newtrop) #mortistrophies
            elif self.player.brawlerID == 12:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'crowtrophies', newtrop) #crowtrophies
            elif self.player.brawlerID == 13:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'pocotrophies', newtrop) #pocotrophies
            elif self.player.brawlerID == 14:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'botrophies', newtrop) #botrophies
            elif self.player.brawlerID == 15:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'pipertrophies', newtrop) #pipertrophies
            elif self.player.brawlerID == 16:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'pamtrophies', newtrop) #pamtrophies
            elif self.player.brawlerID == 17:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'taratrophies', newtrop) #taratrophies
            elif self.player.brawlerID == 18:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'darryltrophies', newtrop) #darryltrophies
            elif self.player.brawlerID == 19:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'pennytrophies', newtrop) #pennytrophies
            elif self.player.brawlerID == 20:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'franktrophies', newtrop) #franktrophies
            elif self.player.brawlerID == 21:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'genetrophies', newtrop) #genetrophies
            elif self.player.brawlerID == 22:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'ticktrophies', newtrop) #ticktrophies
            elif self.player.brawlerID == 23:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'leontrophies', newtrop) #leontrophies
            elif self.player.brawlerID == 24:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'rosatrophies', newtrop) #rozatrophies
            elif self.player.brawlerID == 25:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'carltrophies', newtrop) #carltrophies
            elif self.player.brawlerID == 26:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'bibitrophies', newtrop) #bibitrophies
            elif self.player.brawlerID == 27:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'bittrophies', newtrop) #bittrophies
            elif self.player.brawlerID == 28:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'sandytrophies', newtrop) #sandytrophies
            elif self.player.brawlerID == 29:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'beatrophies', newtrop) #beatrophies
            elif self.player.brawlerID == 30:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'emztrophies', newtrop) #emztrophies
            elif self.player.brawlerID == 31:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'mrptrophies', newtrop) #mrptrophies
            elif self.player.brawlerID == 32:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'maxtrophies', newtrop) #maxtrophies
            elif self.player.brawlerID == 34:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'jackytrophies', newtrop) #jackytrophies
            elif self.player.brawlerID == 35:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'galetrophies', newtrop) #galetrophies
            elif self.player.brawlerID == 36:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'nanitrophies', newtrop) #nanitrophies
            elif self.player.brawlerID == 37:
            	newtrop = brawler_trophies + lose_val
            	DataBase.replaceValue(self, 'sprouttrophies', newtrop) #sprouttrophies
            xp = (5000)
            result = (16)
            tokens = (15)
            checldoubled = (10)
            eventdoubled = (20)
            totaltokens = (40)
            starplayer = (1)
            new_trophies = self.player.trophies + lose_val
            #new_tokens = self.player.brawl_boxes + totaltokens
            goldgetted = (0)
            #new_gold = self.player.gold + goldgetted
            #DataBase.replaceValue(self, 'gold', new_gold)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + lose_val
           # DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            DataBase.replaceValue(self, 'trophies', new_trophies)
            try:
                DataBase.replaceValueLD(self, 'trophies', new_trophies)
            except:
            	print("err.db")
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)

        if self.player.GameType == 2:
            #new_trophies = self.player.trophies + (0)
            trophiesend = (0)
            xp = (5000)
            result = (16)
            tokens = (16)
            checldoubled = (15)
            eventdoubled = (30)
            totaltokens = (60)
            starplayer = (0)
            #new_tokens = self.player.brawl_boxes + totaltokens
            goldgetted = (0)
            #new_gold = self.player.gold + goldgetted
            #DataBase.replaceValue(self, 'gold', new_gold)
            #self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + (0)
            #DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            #DataBase.replaceValue(self, 'trophies', new_trophies)
            #DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
   
        self.writeVint(35) #Battle Tokens 
        self.writeVint(trophiesend) #Trophies Value
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
        self.writeVint(trophiesend) #Trophies
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
        self.writeVint(1)
        self.writeVint(self.player.GameType)

       # brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        exp_reward = [8, 6, 4]
        token_list = [20,15,10]
        namecolor = (43000000) + self.player.namecolor