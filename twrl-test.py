import twrlparse as tp
p = tp.Parser("neotwirl.tar.zst","./tmp")
fp,data = p.load()
print(fp)
print(f"Members: {[x.name for x in data]}")
for x in data:
	if x.name == "neotwirl/pkginfo":
		pkginfo = ""
