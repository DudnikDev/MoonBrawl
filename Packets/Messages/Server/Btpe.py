from Utils.Writer import Writer


class BTPe(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20405
        self.player = player

    def encode(self):
        self.writeInt(1) # timer
        self.writeInt(5)  # Current player
        self.writeInt(6) # Max player

        self.writeInt(1)  # Unknown
        self.writeString("Player")
        self.writeVint(10)

        if False:
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(0)

            self.writeVint(1)

            self.writeInt(0)
            self.writeInt(1)

            self.writeString("Bot")

            self.writeVint(1)
            self.writeVint(1)

            self.writeVint(30)

            self.writeHexa('''84 80 10 01''')

            self.writeVint(0)

            self.writeVint(0)

            self.writeVint(0)

            self.writeHexa('''E9 6D F5 02''')

            self.writeVint(1)
            self.writeVint(1)

            self.writeVint(0)
            self.writeVint(15)
            self.writeVint(10)
