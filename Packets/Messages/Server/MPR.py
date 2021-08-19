from Utils.Writer import Writer


class MaintenancePred(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20161
        self.player = player

    def encode(self):
        self.writeInt(0)