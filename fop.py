def readf(link):
    with open(link,"r") as f:
        h = int(f.readline())
    return h

def writef(link,k):
    with open(link, "w") as f:
        f.write(str(k))

def addf(link,k):
    with open(link, "a") as f:
        f.write(str(k))
