import os

names = os.listdir("G:/gui")
names.remove("ff.ico")
print(names)
# os.system("cd G:/gui")
for name in names :
	n = name.split(".")[0]
	command = f"pyuic5 -x -o G:/gui/{n}.py G:/gui/{name}"
	os.system(command)
    