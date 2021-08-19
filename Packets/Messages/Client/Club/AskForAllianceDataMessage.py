from Packets.Messages.Client.Club.AllianceDataMessage import AllianceDataMessage

from Utils.Reader import BSMessageReader


class AskForAllianceDataMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        AllianceDataMessage(self.client, self.player).send()

    def process(self):
        AllianceDataMessage(self.client, self.player).send()