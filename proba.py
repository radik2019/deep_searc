import os
path = os.getcwd()
os.chdir(r"C:\\users")
file_python = path + "/test_raccolta"
if os.path.exists(file_python):
    pass
else:
    os.mkdir(file_python)



def ser(dir, index="py"):
	for i in os.listdir(dir):
		if os.path.isfile(dir + "/" + i):
			new = i.split(".")
			if len(new) == 2:
				if new[1] == index:
					with open(i, "rb") as df:
						s = df.read()

					with open(f"{file_python}/{i}", "wb") as gf:
						gf.write(s)
		else:
			ser(dir+"/"+i)

for dir_, path, file in os.walk(os.getcwd()):
	for i in file:
		df = i.split(".")
		if df[-1] == 'png':
			print(i)
			









# print(ser(os.getcwd()))