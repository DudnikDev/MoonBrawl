from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.LoginFailed import LoginFailed
from Packets.Messages.Server.LoginFailed2 import SError

from Utils.Reader import BSMessageReader

class ClientHello(BSMessageReader):

    def encode(self):
        self.player.errorID = 3 
        self.player.errorText = "The server does not support your version"
        LoginFailed(self.client, self.player).send()

    def decode(self):
        self.player.errorID = 3 
        self.player.errorText = "The server does not support your version"
        LoginFailed(self.client, self.player).send()

    def process(self):
        self.player.errorID = 3 
        self.player.errorText = "The server does not support your version"
        LoginFailed(self.client, self.player).send()