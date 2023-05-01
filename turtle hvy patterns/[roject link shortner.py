import pyshorteners
link=input("enter the link:")
shortener=pyshorteners.shortener()

x = shortener.tinyurl.short(link)
print(x)