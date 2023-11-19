import socket
import concurrent.futures
import json, re
import datetime
import database
import CCP

class Server :
	def __init__(self, host, port, path, backlog) :
		self.host = host
		self.port = port if isinstance(port, int) else int(port)
		self.path = path
		self.backlog = backlog if isinstance(backlog, int) else int(backlog)
		self.database = database.Database(self)
		self.codes = CCP.CCP().codes
		self.payloads = {
			"bad_request" : "[CODE:%s:CODE]" % (self.codes["bad_request"]),
			"ac_register" : "[CODE:%s:CODE]" % (self.codes["ac_register"]),
			"ac_login" : "[CODE:%s:CODE]" % (self.codes["ac_login"]),
			"ac_mk_chatroom" : "[CODE:%s:CODE]" % (self.codes["ac_mk_chatroom"]),
			"ac_refresh" : "[CODE:%s:CODE]" % (self.codes["ac_refresh"]),
			"ac_del_chatroom" : "[CODE:%s:CODE]" % (self.codes["ac_del_chatroom"]),
			"ac_membership" : "[CODE:%s:CODE]" % (self.codes["ac_membership"]),
			"ac_left" : "[CODE:%s:CODE]" % (self.codes["ac_left"]),
			"ac_info" : "[CODE:%s:CODE]" % (self.codes["ac_info"]),
			"ac_kick" : "[CODE:%s:CODE]" % (self.codes["ac_kick"]),
			"ac_msg" : "[CODE:%s:CODE]" % (self.codes["ac_msg"]),
			"rej_register" : "[CODE:%s:CODE]" % (self.codes["rej_register"]),
			"rej_login" : "[CODE:%s:CODE]" % (self.codes["rej_login"]),
			"rej_mk_chatroom" : "[CODE:%s:CODE]" % (self.codes["rej_mk_chatroom"]),
			"rej_refresh" : "[CODE:%s:CODE]" % (self.codes["rej_refresh"]),
			"rej_del_chatroom" : "[CODE:%s:CODE]" % (self.codes["rej_del_chatroom"]),
			"rej_membership" : "[CODE:%s:CODE]" % (self.codes["rej_membership"]),
			"rej_left" : "[CODE:%s:CODE]" % (self.codes["rej_left"]),
			"rej_info" : "[CODE:%s:CODE]" % (self.codes["rej_info"]),
			"rej_kick" : "[CODE:%s:CODE]" % (self.codes["rej_kick"]),
			"rej_msg" : "[CODE:%s:CODE]" % (self.codes["rej_msg"])
		}

	def mission(self, payloads) :
		def analyse() :
			try :
				sock = payloads[0]
				data = payloads[0].recv(4096) 
				data = data.decode() if isinstance(data, bytes) else data
				address = payloads[1]
				code = re.search(r"(?<=CODE:)...(?=:CODE)", data)
				code = int(code.group()) if code else None
				data = re.search(r"(?<=DATA:).+(?=:DATA)", data)
				data = json.loads(data.group()) if data else None
			except :
				payload = (self.payloads["bad_request"], address)
				self.post(sock, payload)
			else :
				return sock, address, code, data

		def task() :
			if code == self.codes["mk_chatroom"]  :
				if not self.database.isroom(name = data["roomname"]) :
					self.database.addroom(name = data["roomname"], admin = data["name"])
					message = "[SERVER] **H3ll0 W0r1d**"
					self.database.addroominfo(name = data["roomname"], key = "append", msg = message)
					self.database.addnameinfo(name = data["name"], info = data["roomname"], key = "addadmin")
					payload = (self.payloads["ac_mk_chatroom"], address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_mk_chatroom"], address)
					self.post(sock, payload)

			elif code == self.codes["refresh"]  :
				member = self.database.ismember(name = data["roomname"], member = data["name"])
				current = self.database.current(name = data["roomname"]) if self.database.isroom(name = data["roomname"]) else None
				if current and member :
					payload = ("%s[DATA:%s:DATA]" % (self.payloads["ac_refresh"], json.dumps(current)), address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_refresh"], address)
					self.post(sock, payload)

			elif code == self.codes["del_chatroom"]  :
				if self.database.isvalidadmin(name = data["roomname"], admin = data["name"]) :
					self.database.addroominfo(name = data["roomname"], key = "delchat")
					self.database.addnameinfo(name = data["name"], info = data["roomname"], key = "deladmin")
					payload = (self.payloads["ac_del_chatroom"], address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_del_chatroom"], address)
					self.post(sock, payload)

			elif code == self.codes["membership"]  :
				if self.database.isroom(name = data["roomname"]) \
					and not self.database.ismember(name = data["roomname"], member = data["name"]) \
					and not self.database.isblock(name = data["roomname"], member = data["name"]) :
					self.database.addroominfo(name = data["roomname"], key = "add")
					self.database.addnameinfo(name = data["name"], info = data["roomname"], key = "addroom")
					payload = (self.payloads["ac_membership"], address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_membership"], address)
					self.post(sock, payload)

			elif code == self.codes["left"]  :
				if self.database.isroom(name = data["roomname"]) \
					and self.database.ismember(name = data["roomname"], member = data["name"]) :
					self.database.addroominfo(name = data["roomname"], key = "del")
					self.database.addnameinfo(name = data["name"], info = data["roomname"], key = "delroom")
					payload = (self.payloads["ac_left"], address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_left"], address)
					self.post(sock, payload)

			elif code == self.codes["info"]  :
				info = json.dumps(self.database.userinfo(name = data["name"]))
				payload = ("%s[DATA:%s:DATA]" % (self.payloads["ac_info"], info), address)
				self.post(sock, payload)

			elif code == self.codes["kick"]  :
				if self.database.isroom(name = data["roomname"]) \
					and self.database.isvalidadmin(name = data["roomname"], admin = data["name"]) :
					self.database.addroominfo(name = data["roomname"], key = "del")
					self.database.addnameinfo(name = data["target"], info = data["roomname"], key = "delroom")
					self.database.addnameinfo(name = data["target"], info = data["roomname"], key = "block")
					payload = (self.payloads["ac_kick"], address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_kick"], address)
					self.post(sock, payload)

			elif code == self.codes["msg"]  :
				if self.database.isroom(name = data["roomname"]) \
					and self.database.ismember(name = data["roomname"], member = data["name"]) :
					time = datetime.datetime.today()
					time = time.strftime("%Y/%m/%d %H:%M:%S")
					message = "[%s][%s] %s" % (time, data["name"], data["message"])
					self.database.addroominfo(name = data["roomname"], key = "append", msg = message)
					payload = (self.payloads["ac_msg"], address)
					self.post(sock, payload)
				else :
					payload = (self.payloads["rej_msg"], address)
					self.post(sock, payload)
			return

		def check() :
			try :
				if code == self.codes["register"] :
					if self.register(name = data["name"]) :
						self.database.addname(name = data["name"], password = data["password"])
						payload = (self.payloads["ac_register"], address)
						self.post(sock, payload)
					else :
						payload = (self.payloads["rej_register"], address)
						self.post(sock, payload)

				elif code == self.codes["login"]  :
					if self.login(name = data["name"], password = data["password"]) :
						payload = (self.payloads["ac_login"], address)
						self.post(sock, payload)
					else :
						payload = (self.payloads["rej_login"], address)
						self.post(sock, payload)

				else :
					if self.login(name = data["name"], password = data["password"]) :
						task()
					else :
						payload = (self.payloads["rej_login"], address)
						self.post(sock, payload)
			except :
				payload = (self.payloads["bad_request"], address)
				self.post(sock, payload)

		sock, address, code, data = analyse()

		if data and isinstance(data, dict) and code :
			check()
		else :
			payload = (self.payloads["bad_request"], address)
			self.post(sock, payload)
		return

	def register(self, name) :
		if not self.database.isname(name = name) \
			and self.database.isvalidchar(name = name) :
			return True
		else :
			return False

	def login(self, name, password) :
		if self.database.isname(name = name) \
			and self.database.isvalidname(name = name, password = password) :
			return True
		else :
			return False

	def listen(self) :
		try :
			with concurrent.futures.ThreadPoolExecutor() as task :
				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen :
					listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
					listen.bind((self.host, self.port))
					listen.listen(self.backlog)
					while True :
						conn, address = listen.accept()
						time = datetime.datetime.today()
						time = int(time.strftime("%Y%m%d%H%M%S"))
						print(f"[{time}] Connection from {address}", end = "\r", flush = True)
						payload = (conn, address)
						task.submit(self.mission, payload)
		except OSError as error :
			error = " ".join(str(error).split()[2:])
			print(f"[!] Error(listen) - {error or None}")
			self.listen()
		except Exception as error :
			print(f"[!] Error(listen) - {error or None}")
			self.listen()
		return

	def post(self, socket, payload) :
		try :
			time = datetime.datetime.today()
			time = int(time.strftime("%Y%m%d%H%M%S"))
			socket.sendall(payload[0].encode())
			print(f"[{time}] Connection from {payload[1]}  success", end = "\n")
		except OSError :
			print(f"[{time}] Connection from {payload[1]}  failure", end = "\n")
			return False
		except Exception as error :
			print(f"[!] Error(post) - {error or None}")
			return False
		else :
			socket.close()
			return True


if __name__ == "__main__" :
	host = socket.gethostbyname(socket.gethostname())
	print(host)
	path = "e:/Dev/python/CyGeek2/cygeek_server"
	print(f"server running...")
	server = Server("127.0.0.1", 8549, path, 1)
	server.listen()