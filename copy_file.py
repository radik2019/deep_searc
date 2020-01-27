
import os
import hashlib

# frase = hashlib.sha256(bytes(input("password:\t"), encoding="utf-8"))
# print(frase.hexdigest())



def deep_search(index, file_python, path=os.getcwd()):
    if os.path.exists(file_python):
        pass
    else:
        os.mkdir(file_python)
    for i in os.listdir(path):
        dir_p = path + "/" + i
        if os.path.isfile(dir_p):
            if i.split(".")[1] == index:

                with open(i, "rb") as df:
                    s = df.read()

                with open(f"{file_python}/{i}", "wb") as gf:
                    gf.write(s)
        elif os.path.isdir(dir_p):
            if  (i[0] == ".") or (i.count(".") > 1):
                pass
            else:
                print(i)
                deep_search(index, file_python, path=dir_p)
        else:
            pass





deep_search("py", "cartella_coso")