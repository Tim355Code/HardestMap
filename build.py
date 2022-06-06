import os
import shutil


DOMAIN_ROOT=os.getenv("DOMAIN_ROOT",".").encode("utf-8")



def copy(src,dst):
	print(f"  Copying '{src}' to '{dst}'...")
	os.makedirs(dst[:dst.rindex("/")],exist_ok=True)
	with open(src,"rb") as rf,open(dst,"wb") as wf:
		data=rf.read()
		if (dst.endswith(".html")):
			data=data.replace(b"{{HEAD}}",head).replace(b"{{HHEADER}}",homeheader).replace(b"{{MHEADER}}",mainheader).replace(b"{{FOOTER}}",footer).replace(b"{{ROOT}}",DOMAIN_ROOT)
		wf.write(data)



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
print("Loading HTML head...")
with open("src/indents/_head.html","rb") as rf:
	head=rf.read()	
print("Loading HTML header...")
with open("src/indents/_homeheader.html","rb") as rf:
	homeheader=rf.read()
with open("src/indents/_mainheader.html","rb") as rf:
	mainheader=rf.read()
print("Loading HTML footer...")
with open("src/indents/_footer.html","rb") as rf:
	footer=rf.read()
print("Adding HTML...")
copy("src/html/index.html","build/index.html")
for k in os.listdir("src/html"):
	copy(f"src/html/{k}",f"build/{k}")
print("Adding CSS...")
for k in os.listdir("src/css"):
	copy(f"src/css/{k}",f"build/css/{k}")
print("Adding JS...")
for k in os.listdir("src/js"):
	copy(f"src/js/{k}",f"build/js/{k}")
print("Adding images...")
for k in os.listdir("rsrc/img"):
	shutil.copytree(f"rsrc/img/{k}",f"build/img/{k}")
print("Adding fonts...")
for k in os.listdir("rsrc/font"):
	copy(f"rsrc/font/{k}",f"build/font/{k}")