f = open("val2014.txt", "r", encoding = "utf8")
if f.mode == 'r':
    contents = f.read()
    contents = contents.split()

def cleanContents(contents):
    imageList = []
    for image in contents:
        imageList.append(image)
    with open("newVal2014.txt", 'w') as filehandle:
        for item in imageList:
            filehandle.write('%s\n'% item)

cleanContents(contents)
