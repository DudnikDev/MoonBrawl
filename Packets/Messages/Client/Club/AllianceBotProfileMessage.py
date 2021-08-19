from Utils.Writer import Writer
from Packets.Messages.Server.CustomError import LoginFailedMessage

class BotProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.player.err_code = 1
        LoginFailedMessage(self.client, self.player, "Незя").send()
