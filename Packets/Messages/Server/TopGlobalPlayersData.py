from Utils.Writer import Writer
import pymysql

class TopGlobalPlayersData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeBool(True)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()
        self.ccplayers = 0

        con = pymysql.connect()
         
        playernum = 0
        with con:    
            cur = con.cursor()
            cur.execute(f"SELECT * FROM `user` ORDER BY `user`.`trophies` DESC LIMIT 100") 
            rows = cur.fetchall()
                   
            for row in rows:  
                name = row[1]
                trophies = int(row[9])
                profile_icon = int(row[10])
                name_color = int(row[13])
                new_player = playernum + 1
                playernum = new_player
            
        #self.writeVint(len(self.players)) # Players Count
        self.writeVint(playernum)

        con = pymysql.connect()
         
        with con:    
            cur = con.cursor()
            cur.execute(f"SELECT * FROM `user` ORDER BY `user`.`trophies` DESC LIMIT 100") 
            rows = cur.fetchall()
            
            for row in rows:    
                name = row[2]
                trophies = int(row[9])
                profile_icon = int(row[10])
                name_color = int(row[13])
                
                self.writeVint(0) # High ID
                self.writeVint(1) # Low ID

                self.writeVint(1)
                self.writeVint(trophies) # Player Trophies

                self.writeVint(1)

                self.writeString() # Club Name
                self.writeString(name) # Player Name

                self.writeVint(1) # Player Level
                self.writeVint(28000000 + profile_icon)
                self.writeVint(43000000 + name_color)
                self.writeVint(0)


        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString("UA")
        print("[LEADERBOARD] FETCH")