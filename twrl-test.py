import twrlparse as tp
p = tp.Parser("neotwirl.tar.zst","./tmp")
fp, data = p.load()
print(f"{data.name} | {fp}\n\n")

for member in data:
	print(f"{member.name} | Type: {'File' if member.isfile() else 'Folder'} | Size: {member.size}\n")

stuff = data.extractfile("neotwirl/pkginfo/PKGINFO")
print("PKGINFO:")
pkg = p.pkginfo(stuff)
print(pkg)
print(f"\nPackage Name: {pkg['info']['Package']}")
