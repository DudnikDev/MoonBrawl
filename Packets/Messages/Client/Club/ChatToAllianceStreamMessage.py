from Packets.Messages.Client.Club.AllianceStreamMessage import AllianceStreamMessage
from Packets.Messages.Client.Club.AllianceBotStreamMessage import AllianceBotStreamMessage
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Packets.Messages.Server.CustomError import LoginFailedMessage
from database.DataBase import DataBase
import time
from Packets.Messages.Server.CustomError import LoginFailedMessage

from Utils.Reader import BSMessageReader


class ChatToAllianceStreamMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False

    def decode(self):
        self.player.err_code = 1
        self.sleepnan = 0
        self.msg = self.read_string()

        if self.msg.lower() == '/stats':
            self.bot_msg = f'Статус сервера:OK\nОтпечаток SHA: {self.player.patch_sha}'

        elif self.msg.lower() == '/token':
            self.bot_msg = f'Сохраните на случай утери аккаунта\n\nНИКОМУ НЕ ПЕРЕДАВАЙТЕ ТОКЕН!\nНик: {self.player.name}\nТокен: {self.player.Token}'
        elif self.msg.lower() == '/double':
            ticketscheck = DataBase.getVal(self, 'tickets')
            if self.requested_val == 6391:
                self.sleepnan = 1
                DataBase.replaceValue(self, 'tickets', 6392)
                self.bot_msg2 = f'Удвоение кубков включено!'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                pass
            elif self.requested_val == 6392:
                self.sleepnan = 1
                DataBase.replaceValue(self, 'tickets', 6391)
                self.bot_msg2 = f'Удвоение кубков выключено!'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                pass
            else:
        	    self.bot_msg = f'Ошибка! У вас нету VIP! Купите его у @pedikdev в Telegram\n\nотладка: {self.requested_val} {self.player.tickets}'
        elif self.msg.lower() == '/full':
        	if self.player.tickets != 6391:
        	    self.bot_msg = f'Ошибка! У вас нету VIP! Купите его у @pedikdev в Telegram'
        	if self.player.tickets == 6392:
        	    self.bot_msg = f'Ошибка! У вас включён множитель кубков! Отключите его прежде чем юзать команды!'
        	if self.player.tickets == 6391:
        	    try:
                	self.sleepnan = 1
                	DataBase.replaceValue(self, 'coltunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'1/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'bullunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'2/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'brockunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'3/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'ricounlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'4/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'spikeunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'5/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'barleyunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'6/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'jessieunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'7/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'nitaunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'8/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'dynamikeunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'9/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'elprimounlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'10/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'mortisunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'11/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'crowunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'12/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'pocounlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'13/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'bounlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'14/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'piperunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'15/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'pamunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'16/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'taraunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'17/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'darrylunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'18/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'pennyunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'19/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'frankunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'20/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'geneunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'21/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'tickunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'22/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'leonunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'23/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'rosaunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'24/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'carlunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'25/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'bibiunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'26/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'bitunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'27/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'sandyunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'28/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'beaunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'29/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'emzunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'30/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'mrpunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'31/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'maxunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'32/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'jackyunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'33/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'galeunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'34/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'naniunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'35/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	DataBase.replaceValue(self, 'sproutunlocked', 1)
                	time.sleep(0.12)
                	self.bot_msg2 = f'36/36'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	time.sleep(0.5)
                	self.bot_msg2 = f'Сохранение...'
                	AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                	self.player.message_tick += 1
                	time.sleep(2.0)
                	self.send_ofs = True
        	    except:
                	LoginFailedMessage(self.client, self.player, "Server error 501").send()	
        elif self.msg.lower() == '/reset':
            self.send_ofs = True
            DataBase.replaceValue(self, 'gold', 0)
            DataBase.replaceValue(self, 'gems', 0)
            DataBase.replaceValue(self, 'tickets', 0)

        elif self.msg.lower().startswith('/gems'):
            try:
            	if self.player.tickets != 6391:
        	        self.bot_msg = f'Ошибка! У вас нету VIP! Купите его у @pedikdev в Telegram'
            	if self.player.tickets == 6392:
            		self.bot_msg = f'Ошибка! У вас включён множитель кубков! Отключите его прежде чем юзать команды!'
            	elif self.player.tickets == 6391:
                    newGems = self.msg.split(" ", 4)[1:]
                    if int(newGems[0]) > 10001:
                	    self.bot_msg = f'Слишком большое число!(\nЧтобы снять лимит купите VIP!'
                    elif int(newGems[0]) < 1:
                	    self.bot_msg = f'Слишком маленькое число число!('
                    elif int(newGems[0]) < 10001:
                       DataBase.replaceValue(self, 'gems', int(newGems[0]))
                       self.send_ofs = True
            except:
                pass
        elif self.msg.lower().startswith('/vip'):
        	if self.player.tickets != 6391:
        	    self.bot_msg = f'У вас нету VIP\nКупите его у @pedikdev в Telegram'
        	if self.player.tickets == 6392:
        	    self.bot_msg = f'Ошибка! У вас включён множитель кубков! Отключите его прежде чем юзать команды!'
        	elif self.player.tickets == 6391:
        	    self.bot_msg = f'У вас есть VIP\nСрок: PERMANENT'
        elif self.msg.lower().startswith('/gold'):
            try:
                newGold = self.msg.split(" ", 4)[1:]
                if int(newGold[0]) > 10001:
                	self.bot_msg = f'Слишком большое число!(\nЧтобы снять лимит купите VIP!'
                elif int(newGold[0]) < 1:
                	self.bot_msg = f'Слишком маленькое число!('
                elif int(newGold[0]) < 10001:
                    DataBase.replaceValue(self, 'gold', int(newGold[0]))
                    self.send_ofs = True
            except:
                self.bot_msg = f'Произошла ошибка ('
        if self.msg.lower() == '/about':
            self.bot_msg = f'Это сервер 27-ой версии базара тары!\nРазработчики: pedikDev и hpdev\nНаш дискорд сервер -> https://discord.gg/qdMw3Qvm2b'

        elif self.msg.lower().startswith('/starpoints'):
            try:
                newStarpoints = self.msg.split(" ", 10)[1:]
                if int(newStarpoints[0]) > 10001:
                	self.bot_msg = f'Слишком большое число!(\nЧтобы снять лимит купите VIP!'
                elif int(newStarpoints[0]) < 1:
                	self.bot_msg = f'Слишком маленькое число!('
                elif int(newStarpoints[0]) < 10001:
                    DataBase.replaceValue(self, 'starpoints', int(newStarpoints[0]))
                    self.send_ofs = True
            except:
                pass
        elif self.msg.lower().startswith('/restore'):
            try:
                self.sleepnan = 1
                DataBase.getSpecifiedValue(self, 'trophies')
                self.bot_msg2 = f'Найден аккаунт с ником {self.fr_es}\n\nТрофеи - {self.fr_aa}\nГемы - {self.fr_ab}\nМонеты - {self.fr_ac}'
                AllianceStreamMessage(self.client, self.player, self.msg).send()
                self.player.message_tick += 1
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(2)
                self.bot_msg2 = f'Восстановление аккаунта через 5...'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(1)
                self.bot_msg2 = f'Восстановление аккаунта через 4...'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(1)
                self.bot_msg2 = f'Восстановление аккаунта через 3...'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(1)
                self.bot_msg2 = f'Восстановление аккаунта через 2...'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(1)
                self.bot_msg2 = f'Восстановление аккаунта через 1...'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(1)
                self.bot_msg2 = f'Восстановление аккаунта через 0...'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                time.sleep(3)
                self.bot_msg2 = f'Восстановление...\nПосле восстановления аккаунт будет удалён с старого облака через 3 дня\nЧтобы хранить ваш аккаунт в облаке вечно - купите VIP!'
                AllianceBotStreamMessage(self.client, self.player, self.bot_msg2).send()
                self.player.message_tick += 1
                DataBase.replaceValue(self, 'trophies', self.fr_aa)
                DataBase.replaceValue(self, 'gems', self.fr_ab)
                DataBase.replaceValue(self, 'gold', self.fr_ac)
                DataBase.replaceValue(self, 'shellyunlocked', self.fr_ad)
                DataBase.replaceValue(self, 'nitaunlocked', self.fr_ae)
                DataBase.replaceValue(self, 'coltunlocked', self.fr_af)
                DataBase.replaceValue(self, 'bullunlocked', self.fr_ag)
                DataBase.replaceValue(self, 'jessieunlocked', self.fr_ah)
                DataBase.replaceValue(self, 'brockunlocked', self.fr_ai)
                DataBase.replaceValue(self, 'dynamikeunlocked', self.fr_aj)
                DataBase.replaceValue(self, 'bounlocked', self.fr_ak)
                DataBase.replaceValue(self, 'elprimounlocked', self.fr_al)
                DataBase.replaceValue(self, 'barleyunlocked', self.fr_am)
                DataBase.replaceValue(self, 'pocounlocked', self.fr_an)
                DataBase.replaceValue(self, 'ricounlocked', self.fr_ao)
                DataBase.replaceValue(self, 'darrylunlocked', self.fr_ap)
                DataBase.replaceValue(self, 'pennyunlocked', self.fr_aq)
                DataBase.replaceValue(self, 'piperunlocked', self.fr_ar)
                DataBase.replaceValue(self, 'pamunlocked', self.fr_as)
                DataBase.replaceValue(self, 'frankunlocked', self.fr_at)
                DataBase.replaceValue(self, 'mortisunlocked', self.fr_au)
                DataBase.replaceValue(self, 'taraunlocked', self.fr_av)
                DataBase.replaceValue(self, 'spikeunlocked', self.fr_aw)
                DataBase.replaceValue(self, 'crowunlocked', self.fr_ax)
                DataBase.replaceValue(self, 'geneunlocked', self.fr_ay)
                DataBase.replaceValue(self, 'tickunlocked', self.fr_az)
                DataBase.replaceValue(self, 'leonunlocked', self.fr_ba)
                DataBase.replaceValue(self, 'rosaunlocked', self.fr_bb)
                DataBase.replaceValue(self, 'carlunlocked', self.fr_bc)
                DataBase.replaceValue(self, 'bibiunlocked', self.fr_bd)
                DataBase.replaceValue(self, 'bitunlocked', self.fr_be)
                DataBase.replaceValue(self, 'sandyunlocked', self.fr_bf)
                DataBase.replaceValue(self, 'beaunlocked', self.fr_bg)
                DataBase.replaceValue(self, 'emzunlocked', self.fr_bh)
                DataBase.replaceValue(self, 'mrpunlocked', self.fr_bi)
                DataBase.replaceValue(self, 'maxunlocked', self.fr_bj)
                DataBase.replaceValue(self, 'jackyunlocked', self.fr_bk)
                DataBase.replaceValue(self, 'galeunlocked', self.fr_bl)
                DataBase.replaceValue(self, 'naniunlocked', self.fr_bm)
                DataBase.replaceValue(self, 'sproutunlocked', self.fr_bn)
                DataBase.replaceValue(self, 'shellytrophies', self.fr_bo)
                DataBase.replaceValue(self, 'shellytrophiesrank', self.fr_bp)
                DataBase.replaceValue(self, 'nitatrophies', self.fr_bq)
                DataBase.replaceValue(self, 'nitatrophiesrank', self.fr_br)
                DataBase.replaceValue(self, 'colttrophies', self.fr_bs)
                DataBase.replaceValue(self, 'colttrophiesrank', self.fr_bt)
                DataBase.replaceValue(self, 'bulltrophies', self.fr_bu)
                DataBase.replaceValue(self, 'bulltrophiesrank', self.fr_bv)
                DataBase.replaceValue(self, 'jessietrophies', self.fr_bw)
                DataBase.replaceValue(self, 'jessietrophiesrank', self.fr_bx)
                DataBase.replaceValue(self, 'brocktrophies', self.fr_by)
                DataBase.replaceValue(self, 'brocktrophiesrank', self.fr_bz)
                DataBase.replaceValue(self, 'dynamiketrophies', self.fr_ca)
                DataBase.replaceValue(self, 'dynamiketrophiesrank', self.fr_cb)
                DataBase.replaceValue(self, 'botrophies', self.fr_cc)
                DataBase.replaceValue(self, 'botrophiesrank', self.fr_cd)
                DataBase.replaceValue(self, 'elprimotrophies', self.fr_ce)
                DataBase.replaceValue(self, 'elprimotrophiesrank', self.fr_cf)
                DataBase.replaceValue(self, 'barleytrophies', self.fr_cg)
                DataBase.replaceValue(self, 'barleytrophiesrank', self.fr_ch)
                DataBase.replaceValue(self, 'pocotrophies', self.fr_ci)
                DataBase.replaceValue(self, 'pocotrophiesrank', self.fr_cj)
                DataBase.replaceValue(self, 'ricotrophies', self.fr_ck)
                DataBase.replaceValue(self, 'ricotrophiesrank', self.fr_cm)
                DataBase.replaceValue(self, 'darryltrophies', self.fr_cn)
                DataBase.replaceValue(self, 'darryltrophiesrank', self.fr_co)
                DataBase.replaceValue(self, 'pennytrophies', self.fr_cp)
                DataBase.replaceValue(self, 'pennytrophiesrank', self.fr_cq)
                DataBase.replaceValue(self, 'pipertrophies', self.fr_cr)
                DataBase.replaceValue(self, 'pipertrophiesrank', self.fr_cs)
                DataBase.replaceValue(self, 'pamtrophies', self.fr_ct)
                DataBase.replaceValue(self, 'pamtrophiesrank', self.fr_cu)
                DataBase.replaceValue(self, 'franktrophies', self.fr_cv)
                DataBase.replaceValue(self, 'franktrophiesrank', self.fr_cw)
                DataBase.replaceValue(self, 'mortistrophies', self.fr_cx)
                DataBase.replaceValue(self, 'mortistrophiesrank', self.fr_cz)
                DataBase.replaceValue(self, 'taratrophies', self.fr_da)
                DataBase.replaceValue(self, 'taratrophiesrank', self.fr_db)
                DataBase.replaceValue(self, 'spiketrophies', self.fr_dc)
                DataBase.replaceValue(self, 'spiketrophiesrank', self.fr_dd)
                DataBase.replaceValue(self, 'crowtrophies', self.fr_de)
                DataBase.replaceValue(self, 'crowtrophiesrank', self.fr_df)
                DataBase.replaceValue(self, 'genetrophies', self.fr_dg)
                DataBase.replaceValue(self, 'genetrophiesrank', self.fr_dh)
                DataBase.replaceValue(self, 'ticktrophies', self.fr_di)
                DataBase.replaceValue(self, 'ticktrophiesrank', self.fr_dj)
                DataBase.replaceValue(self, 'leontrophies', self.fr_dk)
                DataBase.replaceValue(self, 'leontrophiesrank', self.fr_dl)
                DataBase.replaceValue(self, 'rosatrophies', self.fr_dm)
                DataBase.replaceValue(self, 'rosatrophiesrank', self.fr_dn)
                DataBase.replaceValue(self, 'carltrophies', self.fr_do)
                DataBase.replaceValue(self, 'carltrophiesrank', self.fr_dp)
                DataBase.replaceValue(self, 'bibitrophies', self.fr_dq)
                DataBase.replaceValue(self, 'bibitrophiesrank', self.fr_dr)
                DataBase.replaceValue(self, 'bittrophies', self.fr_ds)
                DataBase.replaceValue(self, 'bittrophiesrank', self.fr_dt)
                DataBase.replaceValue(self, 'sandytrophies', self.fr_du)
                DataBase.replaceValue(self, 'sandytrophiesrank', self.fr_dv)
                DataBase.replaceValue(self, 'beatrophies', self.fr_dw)
                DataBase.replaceValue(self, 'beatrophiesrank', self.fr_dx)
                DataBase.replaceValue(self, 'emztrophies', self.fr_dy)
                DataBase.replaceValue(self, 'emztrophiesrank', self.fr_dz)
                DataBase.replaceValue(self, 'mrptrophies', self.fr_ea)
                DataBase.replaceValue(self, 'mrptrophiesrank', self.fr_eb)
                DataBase.replaceValue(self, 'maxtrophies', self.fr_ec)
                DataBase.replaceValue(self, 'maxtrophiesrank', self.fr_ed)
                DataBase.replaceValue(self, 'jackytrophies', self.fr_ee)
                DataBase.replaceValue(self, 'jackytrophiesrank', self.fr_ef)
                DataBase.replaceValue(self, 'galetrophies', self.fr_eg)
                DataBase.replaceValue(self, 'galetrophiesrank', self.fr_eh)
                DataBase.replaceValue(self, 'nanitrophies', self.fr_ei)
                DataBase.replaceValue(self, 'nanitrophiesrank', self.fr_ej)
                DataBase.replaceValue(self, 'sprouttrophies', self.fr_ek)
                DataBase.replaceValue(self, 'sprouttrophiesrank', self.fr_el)
                DataBase.replaceValue(self, 'tickets', self.fr_aq)
                DataBase.replaceValue(self, 'ban', self.fr_er)
                DataBase.replaceValue(self, 'name', self.fr_es)
                time.sleep(13)
                self.send_ofs = True
            except:
                print("error")

        elif self.msg.lower() == '/help':
            self.bot_msg = 'Команды\n/about - про этот сервер а также ссылка на нашу дискорд группу!\n/stats - статус сервера\n\nВажное:\n/token - Ваш токен, СОХРАНИТЕ НА СЛУЧАЙ УТЕРИ АККАУНТА!\n/gems (число до 9999) - установить себе гемов\n/gold (число до 999999) - установить себе монет\n/starpoints (число до 999999) - установить себе старпоинтов\n/reset - сбросить аккаунт\n/full - выбить всех бравлеров\n/vip - проверить есть ли у вас VIP\n\n/restore - восстановить ваш аккаунт после вайпа'

    def process(self):
        if self.sleepnan != 1:
            AllianceStreamMessage(self.client, self.player, self.msg).send()
            self.player.message_tick += 1
            self.sleepnan = 0

        if self.bot_msg != '':
            AllianceBotStreamMessage(self.client, self.player, self.bot_msg).send()
            self.player.message_tick += 1

        if self.send_ofs:
            #OutOfSyncMessage(self.client, self.player, 'Я сохранил всё! Перезайди!').send()
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Перезайдите для показа изменений!").send()
