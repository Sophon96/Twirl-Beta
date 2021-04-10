import twrlparse as tp
from sys import argv
p = tp.Parser("neotwirl.tar.zst","./tmp")
fp, data = p.load()
print(f"{data.name} | {fp}\n\n")

for member in data:
	print(f"{member.name} | Type: {'File' if member.isfile() else 'Folder'} | Size: {member.size}\n")
print(data)
#stuff = data.extractfile("pkginfo/PKGINFO")
print("PKGINFO:")
pkg = p.pkginfo()
print(pkg)
print(f"\nPackage Name: {pkg['pkgname']}")
print(p.extract_rootfs("./out"))
