from Packets.Messages.Server.MatchMakingCancelledMessage import CancelMatchMaking


from Utils.Reader import BSMessageReader


class PlayerStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.initial_bytes = initial_bytes
        self.player = player
        self.client = client


    def decode(self):
        self.status = self.read_Vint()

    def process(self):
        if self.status == 4 or self.status == 12:
            CancelMatchMaking(self.client, self.player, self.initial_bytes)