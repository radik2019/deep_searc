import os

file_python = os.getcwd() + "/test_raccolta"
if os.path.exists(file_python):
    pass
else:
    os.mkdir(file_python)

def cop(i, file_python):
	with open(i, "rb") as df:
		s = df.read()

	with open(f"{file_python}/{i}", "wb") as gf:
		gf.write(s)

def ser(dir, index="py"):
	for i in os.listdir(dir):
		if os.path.isfile(dir + "/" + i):
			new = i.split(".")
			if len(new) == 2:
				if new[1] == index:
					cop(i, file_python)
		else:
			ser(dir+"/"+i)


print(ser(os.getcwd()))