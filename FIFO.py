dimBuffer = 4

top = " ___"*dimBuffer +" " 
mid = "|   "*dimBuffer+"|" 
bot = "|___" *dimBuffer+"|" 
central = [" "] *dimBuffer
pointIn = 0
pointOut = 0
count = 0
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
sequence = [1, " ", 2, " ", 3, " ", 4, " ", 5,  " ", " ", " ", " "] 


def printStats():
    string = [" "]*4*dimBuffer
    string1=string.copy()
    string[(pointIn+1)*4-2] ="i"
    string1[(pointOut+1)*4-2] ="o"
    print(''.join(string))
    print(''.join(string1))


def insertElem(elem):
    global central, pointIn, pointOut
    central = [str(elem)] + central
    if not (str(elem) == " "):
        pointIn+=1
    if pointIn >= dimBuffer:
        pointIn =0
    if not (central[-1] == " "):
        pointOut +=1
        if pointOut >= dimBuffer:
            pointOut =0
    central.pop(-1)
    drawBuffer() 

def drawBuffer():
    global count, central
    maincontent = "|" 
    for element in central :
        maincontent += " " + str(element) + " |" 
    print(top+"\n" +mid+"\n" +maincontent+"\n" +bot+"\n") 
    printStats() 
    if count < len(sequence):
        count +=1
        insertElem(sequence[count-1]) 

drawBuffer()