from Utils.Writer import Writer

class PlayerProfile(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVint(0)  # High Id
        self.writeVint(1)  # Low Id
        self.writeVint(0)
        self.writeVint(37)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(3)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(4)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(5)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(6)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(7)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(8)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(9)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(10)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(11)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(12)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(13)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(14)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(15)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(17)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(18)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(19)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(20)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(21)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(22)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(23)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(24)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(25)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(26)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(27)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(28)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(29)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(30)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(31)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(32)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(34)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(35)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(36)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(16)
        self.writeVint(37)
        self.writeVint(0)
        self.writeVint(500)
        self.writeVint(500)
        self.writeVint(10)
        self.writeVint(14)
        self.writeVint(1)
        self.writeVint(499)  # 3v3 victories
        self.writeVint(2)
        self.writeVint(1262469)
        self.writeVint(3)
        self.writeVint(500)
        self.writeVint(4)
        self.writeVint(14501)  # highest trophies
        self.writeVint(5)
        self.writeVint(37)
        self.writeVint(7)
        self.writeVint(28000000 + self.player.profileIcon)
        self.writeVint(8)
        self.writeVint(500)  # solo victories
        self.writeVint(9)
        self.writeVint(21)
        self.writeVint(10)
        self.writeVint(500)
        self.writeVint(11)
        self.writeVint(499)  # duo victories
        self.writeVint(12)
        self.writeVint(21)
        self.writeVint(13)
        self.writeVint(500)
        self.writeVint(14)
        self.writeVint(1)
        self.writeVint(15)
        self.writeVint(499)  # most challenge wins
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000 + self.player.profileIcon)
        self.writeVint(43000000 + self.player.namecolor)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-1040385)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        print("(I) PlayerData send success")