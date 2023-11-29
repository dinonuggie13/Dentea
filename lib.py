import time

def sstlist(string, splitby):
    listtoss = string.split(splitby)
    for i in range(len(listtoss)):
        listtoss[i] = listtoss[i].strip()
    return listtoss

def removeword(word, string):
    meow = string.replace(word, '')
    meow = meow.strip()
    return meow

def dadjoke(lowered):
    if lowered.startswith(("im", "i'm", "i am")):
        if lowered.startswith("im"): 
            wordtoremove = "im"
        elif lowered.startswith("i'm"):
            wordtoremove = "i'm"
        elif lowered.startswith("i am"):
            wordtoremove = "i am"
        withoutim = removeword(wordtoremove, lowered)
        return withoutim


timerdict ={ 
    "timers" : {
      
    }
}


def addtimer(duration, timername):
    timerdict["timers"][timername] = {"time" : time.time(), "duration" : duration} 

def deltimer(timername):
    try:
        del timerdict["timers"][timername]
    except: print("invalid timer name")

def checkfortimer(timername):
    if timername in timerdict["timers"]:
        return True
    else: 
        return False

