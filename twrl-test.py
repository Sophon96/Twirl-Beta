import twrlparse as tp
import json
p = tp.Parser("neotwirl.tar.zst","./tmp")
fp,data = p.load()
print(f"{data.name} | {fp}]\n\n")

for member in data:
	print(f"{member.name} | Type: {'File' if member.isfile() else 'Folder'} | Size: {member.size}\n")

stuff = data.extractfile("neotwirl/pkginfo/PKGINFO")
print("PKGINFO:")
stuff = stuff.read().strip().replace(b"\n",b"")
pkginfo_data = json.loads(stuff)
print(pkginfo_data)
