import logging
import socket
import time
import os
from threading import *
from Logic.Device import Device
from Logic.Player import Players
from Packets.Messages.Server.CustomError import LoginFailedMessage
from Packets.Factory import packets
print("Loading...")
logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")
def _(*args):
	print('', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()
class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip
	def start(self):
		if not os.path.exists('./data.db'):
			os.mknod('./data.db') # create database file if does not exist
		try:
		    self.server.bind((self.ip, self.port))
		except OSError:
		    print('Error, port busy?')
		    exit()
		online = 0
		print('OK...')
		while True:
			try:
			    self.server.listen()
			except:
				print("ERR CONN LISTEN")
			client, address = self.server.accept()
			_(f'[CNT] Ip: {address[0]} Online: {online} ')
			online += 1
			ClientThread(client, address).start()


class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("[RXE] IP {self.address[0]}")
				self.client.close()
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)

					if packet_id in packets:
						_(f'[RX] {packet_id} IP {self.address[0]}')
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()
					else:
						_(f'[404] {packet_id} IP {self.address[0]}')
				if time.time() - last_packet > 10:
					print(f"[DISN] IP: {self.address[0]} ")
					#online -= 1
					self.client.close()
					break
		except ConnectionAbortedError:
			print(f"[DISN] IP: {self.address[0]} ")
			#online -= 1
			self.client.close()
		except ConnectionResetError:
			print(f"[DISN] IP: {self.address[0]} ")
			#online -= 1
			self.client.close()
		except TimeoutError:
			print(f"[DISN] IP: {self.address[0]} ")
			#online -= 1
			self.client.close()


if __name__ == '__main__':
	server = Server('0.0.0.0', 9339)
	server.start()
