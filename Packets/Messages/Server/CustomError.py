from Utils.Writer import Writer
from Utils.Fingerprint import Fingerprint

class LoginFailedMessage(Writer):

    def __init__(self, client, player, msg):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.msg = msg
        self.fingerprint = Fingerprint.loadFinger_full("GameAssets/fingerprint.json")

       
    def encode(self):
        self.writeInt(self.player.err_code)

        self.writeString(self.fingerprint)

        self.writeString() # Server Host
# https://discord.gg/PcQbt42eVg
        self.writeString("https://t.me/moonbrawl")
        self.writeString("https://t.me/moonbrawl")
        self.writeString(self.msg)

        self.writeInt(5000)
        self.writeBool(False)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(3)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)

        self.writeBool(False)
        self.writeBool(False)



