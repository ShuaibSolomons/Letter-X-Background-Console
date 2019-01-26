#################################################
#   Author:     Shu'aib Solomons                #
#################################################


def ProblemA003 (sizeOfX):

    lineList = ["=","=","=","=","=","=","=","=","=","1","=","=","=","=","=","=","=","=","=","2","=","=","=","=","=","=","=","=","=","3","=","=","=","=","=","=","=","=","=","4","=","=","=","=","=","=","=","=","=","5","=","=","=","=","=","=","=","=","=","6","=","=","=","=","=","=","=","=","=","7","=","=","=","=","=","=","=","=","="]
    tempLineList = ["=","=","=","=","=","=","=","=","=","1","=","=","=","=","=","=","=","=","=","2","=","=","=","=","=","=","=","=","=","3","=","=","=","=","=","=","=","=","=","4","=","=","=","=","=","=","=","=","=","5","=","=","=","=","=","=","=","=","=","6","=","=","=","=","=","=","=","=","=","7","=","=","=","=","=","=","=","=","="]
    count = 0
    
    if (sizeOfX > 0 and sizeOfX<=9):
        centerRow = 13
        centerCol = 39

        for i in range (13-sizeOfX-1):
            count += 1
            linePrint(lineList)

        countXAlign = 0
        for i in range (sizeOfX):
            
            tempLineList = lineCreate(tempLineList, lineList)
            
            tempLineList[centerCol -sizeOfX + countXAlign] = "$"
            tempLineList[centerCol +sizeOfX - countXAlign] = "$"
            countXAlign +=1
            linePrint(tempLineList)

        countXAlign -=1

        tempLineList[39]="$"
        tempLineList[38]="="
        tempLineList[40]="="
        linePrint(tempLineList)
        
        #i =1
        for i in range (sizeOfX):
            tempLineList = lineCreate(tempLineList, lineList)
            
            tempLineList[centerCol -sizeOfX + countXAlign] = "$"
            tempLineList[centerCol +sizeOfX - countXAlign] = "$"
            linePrint(tempLineList)
            countXAlign -= 1

        for i in range (13-sizeOfX-1):
            count += 1
            linePrint(lineList)
            
        var = 0
        sizeOfX

    else:
        print("Unfortunately the size of your X is to large please ensure that it is between 1 and 9")



def lineCreate(tempLineList, lineList):
    for i in range(len(tempLineList)-1):
        tempLineList[i] = lineList[i]

    return tempLineList


def linePrint(lineList):
    list = ""
    for i in range(len(lineList)):
        
        list += lineList[i]

    print(list)



ProblemA003(9)
