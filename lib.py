import time



## UTILITY FUNCTIONS
# Turn string into list, then strip whitespace
def sstlist(string, splitby):
    listtoss = string.split(splitby)
    for i in range(len(listtoss)):
        listtoss[i] = listtoss[i].strip()
    return listtoss


# Remove word from string, then return word
def removeword(word, string):
    meow = string.replace(word, '')
    meow = meow.strip()
    return meow


# removes variations of "i'm" from a string
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



## MAIN LIBRARY FUNCTIONS
timerdict = { 
    "timers" : {
      
    }
}


def addtimer(duration, timername):
    timerdict["timers"][timername] = {"time" : time.time(), "duration" : duration} 


def deltimer(timername):
    try:
        del timerdict["timers"][timername]
    except: print("invalid timer name")


# Check existence of timer with given name
def checkfortimer(timername):
    if timername in timerdict["timers"]:
        return True
    else: 
        return False

