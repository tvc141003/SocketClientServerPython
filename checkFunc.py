def checkFoodName(foodNames, dataMenu):
    for i in foodNames:
        isTrue = False
        for j in dataMenu:
            if i == j['name']:
                isTrue = True
                break
        if (isTrue == False): return False
    return True

def checkNumberOfBankCard(numberOfBankCard):
    if (len(numberOfBankCard) != 10): return False
    for i in range(len(numberOfBankCard)):
        if (numberOfBankCard[i] < '0' or numberOfBankCard[i] > '9'):
            return False
    return True

def getSec(getSecTime):
    #print(getSecTime)
    listTime = getSecTime.split(' ')
    totalSec = int(listTime[2])*24*3600
    listDays = listTime[3].split(':')
    totalSec = totalSec + int(listDays[0])*3600 + int(listDays[1])*60 + int(listDays[2])
    return totalSec

def checkDiffTimeUnderSecondHours(backTime, curTime):
    backTimeSec = getSec(backTime)
    curTimeSec = getSec(curTime)

    return (curTimeSec - backTimeSec <= 7200)