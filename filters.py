# How To apply filters

namelist=("Thomas","Sylonjia","Viera","Stuart","James","Susane","John","schillers","Lisa")

slist=filter(lambda x: x.startswith("s") or x.startswith("S"),namelist)#list can also be applied here
otherlist=filter(lambda x: not x.startswith("s") and not x.startswith("S"),namelist)
print("Names Starting with s")
print(list(slist))
print("Names Not Starting with s")
print(list(otherlist))
