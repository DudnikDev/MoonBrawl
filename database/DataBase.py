from tinydb import TinyDB, Query
import json
import string
import random
import pymysql
from Utils.Helpers import Helpers
from Packets.Messages.Server.CustomError import LoginFailedMessage

class DataBase:

    def loadAccount(self):
        con = pymysql.connect()
        with con:    
            cur = con.cursor()
            cur.execute(f"SELECT * FROM user WHERE token = '{self.player.Token}'") 
            rows = cur.fetchall()
            
            for row in rows: 
                row_value = 2 #0 - id 1 - token
                self.player.name =  row[row_value]
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.gems =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.gold =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ban =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.tickets =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.brawlerID =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.skinID =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.trophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.profileIcon =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.brawlBoxes =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bigBoxes =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.namecolor =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.gadget =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.starpower =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.DoNotDistrub =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.roomID =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mapID =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue

                self.player.shellySkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.nitaSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.coltSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bullSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jessieSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.brockSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.dynamikeSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.boSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.elprimoSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.barleySkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pocoSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ricoSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.darrylSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pennySkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.piperSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pamSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.frankSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mortisSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.taraSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.spikeSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.crowSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.geneSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.tickSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.leonSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.rosaSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.carlSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bibiSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bitSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sandySkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.beaSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.emzSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mrpSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.maxSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jackySkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.galeSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.naniSkin =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sproutSkin =  int(row[row_value])

                
                self.player.shellyunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.nitaunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.coltunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bullunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jessieunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.brockunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.dynamikeunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bounlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.elprimounlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.barleyunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pocounlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ricounlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.darrylunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pennyunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.piperunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pamunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.frankunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mortisunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.taraunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.spikeunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.crowunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.geneunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.tickunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.leonunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.rosaunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.carlunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bibiunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bitunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sandyunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.beaunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.emzunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mrpunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.maxunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jackyunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.galeunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.naniunlocked =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sproutunlocked =  int(row[row_value])


                self.player.shellytrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.nitatrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.colttrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bulltrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jessietrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.brocktrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.dynamiketrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.botrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.elprimotrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.barleytrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pocotrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ricotrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.darryltrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pennytrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pipertrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pamtrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.franktrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mortistrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.taratrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.spiketrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.crowtrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.genetrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ticktrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.leontrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.rosatrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.carltrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bibitrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bittrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sandytrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.beatrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.emztrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mrptrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.maxtrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jackytrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.galetrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.nanitrophies =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sprouttrophies =  int(row[row_value])

                
                self.player.shellytrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.nitatrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.colttrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bulltrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jessietrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.brocktrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.dynamiketrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.botrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.elprimotrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.barleytrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pocotrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ricotrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.darryltrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pennytrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pipertrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.pamtrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.franktrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mortistrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.taratrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.spiketrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.crowtrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.genetrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.ticktrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.leontrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.rosatrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.carltrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bibitrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.bittrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sandytrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.beatrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.emztrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.mrptrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.maxtrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.jackytrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.galetrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.nanitrophiesrank =  int(row[row_value])
                row_newvalue = row_value + 1
                row_value = row_newvalue
                self.player.sprouttrophiesrank =  int(row[row_value])


        
    def getSpecifiedValue(self, value_name):
        directoryold = "oldusers/" + self.player.Token
        print(directoryold)
        db = TinyDB(directoryold)
        query = Query()
        self.fr_aa = db.search(query.token == str(self.player.Token))[0]['info']['trophies']
        self.fr_ab = db.search(query.token == str(self.player.Token))[0]['info']['gems']
        self.fr_ac = db.search(query.token == str(self.player.Token))[0]['info']['gold']
        self.fr_ad = db.search(query.token == str(self.player.Token))[0]['info']['shellyunlocked']
        self.fr_ae = db.search(query.token == str(self.player.Token))[0]['info']['nitaunlocked']
        self.fr_af = db.search(query.token == str(self.player.Token))[0]['info']['coltunlocked']
        self.fr_ag = db.search(query.token == str(self.player.Token))[0]['info']['bullunlocked']
        self.fr_ah = db.search(query.token == str(self.player.Token))[0]['info']['jessieunlocked']
        self.fr_ai = db.search(query.token == str(self.player.Token))[0]['info']['brockunlocked']
        self.fr_aj = db.search(query.token == str(self.player.Token))[0]['info']['dynamikeunlocked']
        self.fr_ak = db.search(query.token == str(self.player.Token))[0]['info']['bounlocked']
        self.fr_al = db.search(query.token == str(self.player.Token))[0]['info']['elprimounlocked']
        self.fr_am = db.search(query.token == str(self.player.Token))[0]['info']['barleyunlocked']
        self.fr_an = db.search(query.token == str(self.player.Token))[0]['info']['pocounlocked']
        self.fr_ao = db.search(query.token == str(self.player.Token))[0]['info']['ricounlocked']
        self.fr_ap = db.search(query.token == str(self.player.Token))[0]['info']['darrylunlocked']
        self.fr_aq = db.search(query.token == str(self.player.Token))[0]['info']['pennyunlocked']
        self.fr_ar = db.search(query.token == str(self.player.Token))[0]['info']['piperunlocked']
        self.fr_as = db.search(query.token == str(self.player.Token))[0]['info']['pamunlocked']
        self.fr_at = db.search(query.token == str(self.player.Token))[0]['info']['frankunlocked']
        self.fr_au = db.search(query.token == str(self.player.Token))[0]['info']['mortisunlocked']
        self.fr_av = db.search(query.token == str(self.player.Token))[0]['info']['taraunlocked']
        self.fr_aw = db.search(query.token == str(self.player.Token))[0]['info']['spikeunlocked']
        self.fr_ax = db.search(query.token == str(self.player.Token))[0]['info']['crowunlocked']
        self.fr_ay = db.search(query.token == str(self.player.Token))[0]['info']['geneunlocked']
        self.fr_az = db.search(query.token == str(self.player.Token))[0]['info']['tickunlocked']
        self.fr_ba = db.search(query.token == str(self.player.Token))[0]['info']['leonunlocked']
        self.fr_bb = db.search(query.token == str(self.player.Token))[0]['info']['rosaunlocked']
        self.fr_bc = db.search(query.token == str(self.player.Token))[0]['info']['carlunlocked']
        self.fr_bd = db.search(query.token == str(self.player.Token))[0]['info']['bibiunlocked']
        self.fr_be = db.search(query.token == str(self.player.Token))[0]['info']['bitunlocked']
        self.fr_bf = db.search(query.token == str(self.player.Token))[0]['info']['sandyunlocked']
        self.fr_bg = db.search(query.token == str(self.player.Token))[0]['info']['beaunlocked']
        self.fr_bh = db.search(query.token == str(self.player.Token))[0]['info']['emzunlocked']
        self.fr_bi = db.search(query.token == str(self.player.Token))[0]['info']['mrpunlocked']
        self.fr_bj = db.search(query.token == str(self.player.Token))[0]['info']['maxunlocked']
        self.fr_bk = db.search(query.token == str(self.player.Token))[0]['info']['jackyunlocked']
        self.fr_bl = db.search(query.token == str(self.player.Token))[0]['info']['galeunlocked']
        self.fr_bm = db.search(query.token == str(self.player.Token))[0]['info']['naniunlocked']
        self.fr_bn = db.search(query.token == str(self.player.Token))[0]['info']['sproutunlocked']
        self.fr_bo = db.search(query.token == str(self.player.Token))[0]['info']['shellytrophies']
        self.fr_bp = db.search(query.token == str(self.player.Token))[0]['info']['shellytrophiesrank']
        self.fr_bq = db.search(query.token == str(self.player.Token))[0]['info']['nitatrophies']
        self.fr_br = db.search(query.token == str(self.player.Token))[0]['info']['nitatrophiesrank']
        self.fr_bs = db.search(query.token == str(self.player.Token))[0]['info']['colttrophies']
        self.fr_bt = db.search(query.token == str(self.player.Token))[0]['info']['colttrophiesrank']
        self.fr_bu = db.search(query.token == str(self.player.Token))[0]['info']['bulltrophies']
        self.fr_bv = db.search(query.token == str(self.player.Token))[0]['info']['bulltrophiesrank']
        self.fr_bw = db.search(query.token == str(self.player.Token))[0]['info']['jessietrophies']
        self.fr_bx = db.search(query.token == str(self.player.Token))[0]['info']['jessietrophiesrank']
        self.fr_by = db.search(query.token == str(self.player.Token))[0]['info']['brocktrophies']
        self.fr_bz = db.search(query.token == str(self.player.Token))[0]['info']['brocktrophiesrank']
        self.fr_ca = db.search(query.token == str(self.player.Token))[0]['info']['dynamiketrophies']
        self.fr_cb = db.search(query.token == str(self.player.Token))[0]['info']['dynamiketrophiesrank']
        self.fr_cc = db.search(query.token == str(self.player.Token))[0]['info']['botrophies']
        self.fr_cd = db.search(query.token == str(self.player.Token))[0]['info']['botrophiesrank']
        self.fr_ce = db.search(query.token == str(self.player.Token))[0]['info']['elprimotrophies']
        self.fr_cf = db.search(query.token == str(self.player.Token))[0]['info']['elprimotrophiesrank']
        self.fr_cg = db.search(query.token == str(self.player.Token))[0]['info']['barleytrophies']
        self.fr_ch = db.search(query.token == str(self.player.Token))[0]['info']['barleytrophiesrank']
        self.fr_ci = db.search(query.token == str(self.player.Token))[0]['info']['pocotrophies']
        self.fr_cj = db.search(query.token == str(self.player.Token))[0]['info']['pocotrophiesrank']
        self.fr_ck = db.search(query.token == str(self.player.Token))[0]['info']['ricotrophies']
        self.fr_cm = db.search(query.token == str(self.player.Token))[0]['info']['ricotrophiesrank']
        self.fr_cn = db.search(query.token == str(self.player.Token))[0]['info']['darryltrophies']
        self.fr_co = db.search(query.token == str(self.player.Token))[0]['info']['darryltrophiesrank']
        self.fr_cp = db.search(query.token == str(self.player.Token))[0]['info']['pennytrophies']
        self.fr_cq = db.search(query.token == str(self.player.Token))[0]['info']['pennytrophiesrank']
        self.fr_cr = db.search(query.token == str(self.player.Token))[0]['info']['pipertrophies']
        self.fr_cs = db.search(query.token == str(self.player.Token))[0]['info']['pipertrophiesrank']
        self.fr_ct = db.search(query.token == str(self.player.Token))[0]['info']['pamtrophies']
        self.fr_cu = db.search(query.token == str(self.player.Token))[0]['info']['pamtrophiesrank']
        self.fr_cv = db.search(query.token == str(self.player.Token))[0]['info']['franktrophies']
        self.fr_cw = db.search(query.token == str(self.player.Token))[0]['info']['franktrophiesrank']
        self.fr_cx = db.search(query.token == str(self.player.Token))[0]['info']['mortistrophies']
        self.fr_cz = db.search(query.token == str(self.player.Token))[0]['info']['mortistrophiesrank']
        self.fr_da = db.search(query.token == str(self.player.Token))[0]['info']['taratrophies']
        self.fr_db = db.search(query.token == str(self.player.Token))[0]['info']['taratrophiesrank']
        self.fr_dc = db.search(query.token == str(self.player.Token))[0]['info']['spiketrophies']
        self.fr_dd = db.search(query.token == str(self.player.Token))[0]['info']['spiketrophiesrank']
        self.fr_de = db.search(query.token == str(self.player.Token))[0]['info']['crowtrophies']
        self.fr_df = db.search(query.token == str(self.player.Token))[0]['info']['crowtrophiesrank']
        self.fr_dg = db.search(query.token == str(self.player.Token))[0]['info']['genetrophies']
        self.fr_dh = db.search(query.token == str(self.player.Token))[0]['info']['genetrophiesrank']
        self.fr_di = db.search(query.token == str(self.player.Token))[0]['info']['ticktrophies']
        self.fr_dj = db.search(query.token == str(self.player.Token))[0]['info']['ticktrophiesrank']
        self.fr_dk = db.search(query.token == str(self.player.Token))[0]['info']['leontrophies']
        self.fr_dl = db.search(query.token == str(self.player.Token))[0]['info']['leontrophiesrank']
        self.fr_dm = db.search(query.token == str(self.player.Token))[0]['info']['rosatrophies']
        self.fr_dn = db.search(query.token == str(self.player.Token))[0]['info']['rosatrophiesrank']
        self.fr_do = db.search(query.token == str(self.player.Token))[0]['info']['carltrophies']
        self.fr_dp = db.search(query.token == str(self.player.Token))[0]['info']['carltrophiesrank']
        self.fr_dq = db.search(query.token == str(self.player.Token))[0]['info']['bibitrophies']
        self.fr_dr = db.search(query.token == str(self.player.Token))[0]['info']['bibitrophiesrank']
        self.fr_ds = db.search(query.token == str(self.player.Token))[0]['info']['8bittrophies']
        self.fr_dt = db.search(query.token == str(self.player.Token))[0]['info']['8bittrophiesrank']
        self.fr_du = db.search(query.token == str(self.player.Token))[0]['info']['sandytrophies']
        self.fr_dv = db.search(query.token == str(self.player.Token))[0]['info']['sandytrophiesrank']
        self.fr_dw = db.search(query.token == str(self.player.Token))[0]['info']['beatrophies']
        self.fr_dx = db.search(query.token == str(self.player.Token))[0]['info']['beatrophiesrank']
        self.fr_dy = db.search(query.token == str(self.player.Token))[0]['info']['emztrophies']
        self.fr_dz = db.search(query.token == str(self.player.Token))[0]['info']['emztrophiesrank']
        self.fr_ea = db.search(query.token == str(self.player.Token))[0]['info']['mrptrophies']
        self.fr_eb = db.search(query.token == str(self.player.Token))[0]['info']['mrptrophiesrank']
        self.fr_ec = db.search(query.token == str(self.player.Token))[0]['info']['maxtrophies']
        self.fr_ed = db.search(query.token == str(self.player.Token))[0]['info']['maxtrophiesrank']
        self.fr_ee = db.search(query.token == str(self.player.Token))[0]['info']['jackytrophies']
        self.fr_ef = db.search(query.token == str(self.player.Token))[0]['info']['jackytrophiesrank']
        self.fr_eg = db.search(query.token == str(self.player.Token))[0]['info']['galetrophies']
        self.fr_eh = db.search(query.token == str(self.player.Token))[0]['info']['galetrophiesrank']
        self.fr_ei = db.search(query.token == str(self.player.Token))[0]['info']['nanitrophies']
        self.fr_ej = db.search(query.token == str(self.player.Token))[0]['info']['nanitrophiesrank']
        self.fr_ek = db.search(query.token == str(self.player.Token))[0]['info']['sprouttrophies']
        self.fr_el = db.search(query.token == str(self.player.Token))[0]['info']['sprouttrophiesrank']
        self.fr_eq = db.search(query.token == str(self.player.Token))[0]['info']['tickets']
        self.fr_er = db.search(query.token == str(self.player.Token))[0]['info']['ban']
        self.fr_es = db.search(query.token == str(self.player.Token))[0]['info']['name']