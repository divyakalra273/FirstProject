"""
names="John,Jennie,Jim,John,Jack,Joe"
splittedNames=names.split(",")

print(splittedNames,type(splittedNames))
for names in splittedNames:
    print(names.strip())


words=quotes.split(" ")
print(words)
for word in words:
    print(word)
"""
quotes= """
    Work Hard, Get Luckier
    Search the candle ,rather than cursing the darkness
"""
def split(quotes):
    for i in range(0,len(quotes)):
        if i==" ":
            j=i-1
            for j in quotes():
                print(quotes[0:j])

wor=split(quotes)
print(wor)
#on basis of space

