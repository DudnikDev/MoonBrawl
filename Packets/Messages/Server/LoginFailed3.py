from Utils.Writer import Writer


class SError(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20103
        self.player = player

    def encode(self):
        self.writeInt(3)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString("https://t.me/pedikdev")
        self.writeString("Ошибка базы данных, она пошла по пизде! Сообщи pedikDev - https://t.me/pedikdev")
        self.writeHexa('''2E0000012C000000000000000000''')
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeHexa('''00FFFF0000000000''')
        print("[INFO] Message LoginFailed has been sent.")