from Utils.Writer import Writer


class RoomDisconnect(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24125
        self.player = player

    def encode(self):
        self.writeHexa('''00000000''')
        print("[INFO] Message RoomDisconnect has been sent.")
