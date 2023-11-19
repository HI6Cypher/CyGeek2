import os, json
import hashlib
import datetime
import config
import re

class Database :
	def __init__(self, server) :
		self.path = server.path
		config.config(self.path, "names")
		config.config(self.path, "rooms")        

	def __names(self, name) -> list :
		f = name[0].lower()
		name_list = list()
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				loader = json.load(file)
			for i in loader :
				name_list.append(i["name"]) 
			return name_list
		else :
			return False

	def __rooms(self, name) -> list :
		f = name[0].lower()
		room_list = list()
		if os.path.exists(f"{self.path}/rooms/{f}.json") :
			path = f"{self.path}/rooms/{f}.json"
			with open(path, "r") as file :
				loader = json.load(file)
			for i in loader :
				room_list.append(i["roomname"]) 
			return room_list
		else :
			return False

	def addname(self, name, password) -> None :
		f = name[0].lower()
		time = datetime.datetime.today()
		time = int(time.strftime("%Y%m%d%H%M%S"))
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				names = json.load(file)
			new_name = {
				"name" : name,
				"password" : hashlib.sha256(password.encode()).hexdigest(),
				"rooms" : [],
				"admin" : [],
				"block" : [],
				"time" : time
			}
			names.append(new_name)
			json.dump(names, open(path, "w"), indent = 4)
		return

	def addroom(self, name, admin) -> None:
		f = name[0].lower()
		time = datetime.datetime.today()
		time = int(time.strftime("%Y%m%d%H%M%S"))
		if os.path.exists(f"{self.path}/rooms/{f}.json") :
			path = f"{self.path}/rooms/{f}.json"
			with open(path, "r") as file :
				rooms = json.load(file)
			new_name = {
				"roomname" : name,
				"admin" : admin,
				"members" : 1,
				"time" : time,
				"content" : []
			}
			rooms.append(new_name)
			json.dump(rooms, open(path, "w"), indent = 4)
		return

	def addnameinfo(self, name, info, key) -> None :
		f = name[0].lower()
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				names = json.load(file)
			if key == "addadmin" :
				for i in names :
					if name == i["name"] :
						i["admin"].append(info)
						i["rooms"].append(info)
						break
			elif key == "deladmin" :
				for i in names :
					if name == i["name"] :
						i["admin"].remove(info)
						i["rooms"].remove(info)
						break
			elif key == "addroom" :
				for i in names :
					if name == i["name"] :
						i["rooms"].append(info)
						break
			elif key == "delroom" :
				for i in names :
					if name == i["name"] :
						i["rooms"].remove(info)
						break
			elif key == "block" :
				for i in names :
					if name == i["name"] :
						time = datetime.datetime.today()
						time = int(time.strftime("%Y%m%d%H%M%S"))
						i["block"].append({"room" : info, "time" : time, "until" : time + 1000000})
						break
			json.dump(names, open(path, "w"), indent = 4)
		return

	def addroominfo(self, name, key, msg = str()) -> None :
		f = name[0].lower()
		if os.path.exists(f"{self.path}/rooms/{f}.json") :
			path = f"{self.path}/rooms/{f}.json"
			with open(path, "r") as file :
				rooms = json.load(file)
			if key == "delchat" :
				for i in rooms :
					if name == i["roomname"] :
						rooms.remove(i)
			elif key == "add" :
				for i in rooms :
					if name == i["roomname"] :
						i["members"] += 1
						break
			elif key == "del" :
				for i in rooms :
					if name == i["roomname"] :
						i["members"] -= 1
						break
			elif key == "append" :
				for i in rooms :
					if name == i["roomname"] :
						i["content"].append(msg)
						break
			json.dump(rooms, open(path, "w"), indent = 4)
		return

	def isvalidname(self, name, password) -> bool :
		f = name[0].lower()
		def compare(password1, password2) :
			password2 = hashlib.sha256(password2.encode()).hexdigest()
			return True if password1 == password2 else False
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				names = json.load(file)
			for i in names :
				if name == i["name"] :
					return compare(i["password"], password)

	def isvalidadmin(self, name, admin) -> bool :
		f = name[0].lower()
		if os.path.exists(f"{self.path}/rooms/{f}.json") :
			path = f"{self.path}/rooms/{f}.json"
			with open(path, "r") as file :
				rooms = json.load(file)
			for i in rooms :
				if name == i["roomname"] :
					return True if admin == i["admin"] else False

	def isvalidchar(self, name) -> bool :
		f = name[0].lower()
		return True if re.search(r"\w", f) and len(name) <= 10 else False

	def userinfo(self, name) -> dict :
		f = name[0].lower()
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				names = json.load(file)
			for i in names :
				if name == i["name"] :
					return i

	def isblock(self, name, member) -> bool :
		f = member[0].lower()
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				names = json.load(file)
			for i in names :
				if member == i["name"] :
					for j in i["block"] :
						time = datetime.datetime.today()
						time = int(time.strftime("%Y%m%d%H%M%S"))
						if name == j["room"] :
							if time >= j["until"] :
								print(i["block"])
								i["block"].remove(j)
								print(i["block"])
								json.dump(names, open(path, "w"), indent = 4)
								return False
							else :
								return True
					

	def ismember(self, name, member) -> bool :
		f = member[0].lower()
		if os.path.exists(f"{self.path}/names/{f}.json") :
			path = f"{self.path}/names/{f}.json"
			with open(path, "r") as file :
				names = json.load(file)
			for i in names :
				if member == i["name"] :
					return True if name in i["rooms"] else False

	def isname(self, name) -> bool :
		names = self.__names(name)
		return True if names and name in names else False

	def isroom(self, name) -> bool :
		rooms = self.__rooms(name)
		return True if rooms and name in rooms else False

	def current(self, name) -> list :
		f = name[0].lower()
		if os.path.exists(f"{self.path}/rooms/{f}.json") :
			path = f"{self.path}/rooms/{f}.json"
			with open(path, "r") as file :
				rooms = json.load(file)
			for i in rooms :
				if name == i["roomname"] :
					return i["content"]


# s = Database()
# # s.addroom("ell", "arsgh")
# # s.addroominfo("arsgh", "del")
# # s.addroominfo("ell", "append", "socket programming")
# s.addname("arsgh", "helloworld")
# # s.addnameinfo("arsgh", "ell", "delroom")
# # print(s.isvalidname("arsgh", "helloworld"))
# # print(s.isvalidadmin("ell", "arsgh"))
# # print(s.isroom("ell"))

