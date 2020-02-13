f= open("train2014.txt","r",encoding="utf8")
if f.mode == 'r':
    contents = f.read()
    print(type(contents))
    print(contents)

def cleanContents(contents):
    images = contents.split()
