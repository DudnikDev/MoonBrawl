from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from database.DataBase import DataBase
from Packets.Messages.Server.CustomError import LoginFailedMessage
from Packets.Messages.Server.OutOfSync import OutOfSync

from Utils.Reader import BSMessageReader


class SetContentCreator(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        

    def decode(self):
        print("[ANALYTICS]", self.player.Token, "kicked contentCreator")
        self.iscommand = False
        self.string = self.read_string()
        self.player.err_code = 1
        LoginFailedMessage(self.client, self.player, "Зачем? >.<").send()

    def process(self):
        if self.iscommand:
            OutOfSync(self.client, self.player).send()