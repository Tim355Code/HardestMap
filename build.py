import os



def copy(src,dst):
	print(f"  Copying '{src}' to '{dst}'...")
	os.makedirs(dst[:dst.rindex("/")],exist_ok=True)
	with open(src,"rb") as rf,open(dst,"wb") as wf:
		wf.write(rf.read())



if (os.path.exists("build")):
	dl=[]
	for r,ndl,fl in os.walk("build"):
		r=r.replace("\\","/").strip("/")+"/"
		for d in ndl:
			dl.insert(0,r+d)
		for f in fl:
			os.remove(r+f)
	for k in dl:
		os.rmdir(k)
else:
	os.mkdir("build")
print("Adding HTML...")
copy("src/index.html","build/index.html")
print("Adding CSS...")
for k in os.listdir("src/css"):
	copy(f"src/css/{k}",f"build/css/{k}")
print("Adding JS...")
for k in os.listdir("src/js"):
	copy(f"src/js/{k}",f"build/js/{k}")
print("Adding images...")
for k in os.listdir("rsrc/img"):
	copy(f"rsrc/img/{k}",f"build/img/{k}")
print("Adding fonts...")
for k in os.listdir("rsrc/font"):
	copy(f"rsrc/font/{k}",f"build/font/{k}")
