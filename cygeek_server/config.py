import json, os
def config(path, folder) :
	f = "0123456789abcdefghijklmnopqrstuvwxyz"
	for i in list(f) :
		try :
			json.dump([], open(f"{path}/{folder}/{i}.json", "x"), indent = 4)
		except FileNotFoundError :
			raise FileNotFoundError(f"{path}/{folder}/{i}.json")
		except Exception :
			pass