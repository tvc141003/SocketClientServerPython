import json
import definedObj
import checkFunc
import time
import UI
def welcomeClient(client):
    #print('OPTION')
    msg='\nWelcome to Chu Be Dan foodstore! What do you want to do?'
    msg+='\n1.View menu\t2.Order food\t3.Pay bill\n4.Add food\t5.View port\t6.Count connected people\n7.Quit'
    msg+='\nPlease type your request with correct syntax!'
    client.conn.sendall(bytes(msg,"utf8"))
    #print('1.View Menu')
    
def writeJson(data, jsonFileName):
    with open(jsonFileName, "w") as jsonFile:
        convertJson = json.dumps(data, indent = 4)
        jsonFile.write(convertJson)
    jsonFile.close()

def readJson(jsonFileName):
    with open(jsonFileName) as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
        return data

def viewMenu():
    dataMenu = readJson('menu.json')
    UI.Window(dataMenu)

def orderFood(client):
    
    msg = 'Input name of food: '
    client.conn.sendall(bytes(msg, 'utf-8'))

    dataMenu = readJson('menu.json')
    
    while True:
        data = client.conn.recv(1024)
        foodName = data.decode("utf8")
        foodNames = foodName.split(',')
        for i in range(len(foodNames)):
            foodNames[i] = foodNames[i].strip()
        if (checkFunc.checkFoodName(foodNames, dataMenu)): 
            break
        else:
            msg = 'Not found food\nPlease order again'
            client.conn.sendall(bytes(msg, 'utf-8'))

    amountFoods = []
    for i in foodNames:
        msg = f'Input amount of {i}: '
        client.conn.sendall(bytes(msg, 'utf-8'))
        data = client.conn.recv(1024)
        amountFood = int(data.decode("utf8"))
        amountFoods.append(amountFood)
    
    clientOrderList = []
    for i in range(len(foodNames)):
        createFoodOrder = definedObj.OrderFood(client, foodNames[i], amountFoods[i])
        clientOrderList.append(createFoodOrder.getOrderFood())

    orderData = readJson('orderList.json')
    isClientOrderBefore = False
    for i in orderData:
        if int(i) == int(client.addr[1]):
            isClientOrderBefore = True
            break
    
    if (isClientOrderBefore):
        orderData[str(client.addr[1])] = orderData[str(client.addr[1])] + clientOrderList
    else:
        orderData = orderData | {
            client.addr[1]: clientOrderList
        }

    writeJson(orderData, "orderList.json")
    orderData = readJson('orderList.json')
    totalBill = 0
    for i in orderData[str(client.addr[1])]:
        totalBill += i['totalPrice']
    msg = f'Total price: {totalBill}'
    client.conn.sendall(bytes(msg+'\nAny request?', 'utf-8'))

def payBill(client):
    
    totalBill = 0
    orderData = readJson("orderList.json")
    isClientOrderBefore = False
    for i in orderData:
        if int(i) == int(client.addr[1]):
            isClientOrderBefore = True
            break
    if(isClientOrderBefore == False):
        msg = 'You don\'t have any bill to pay.\nPlease order food first!'
        client.conn.sendall(bytes(msg, 'utf-8'))
        return
    
    for i in orderData[str(client.addr[1])]:
        if (i['status'] == True):
            totalBill += i['totalPrice']

    
    msg = f'Total bill you need pay: {totalBill}\nPlease choose payment method: \n1: By money\n2: By bank card'
    client.conn.sendall(bytes(msg, 'utf-8'))

    while True:
        clientSend = client.conn.recv(1024)
        paymentMethod = clientSend.decode("utf8")
        if (paymentMethod == '1'):
            for i in orderData[str(client.addr[1])]:
                if (i['status'] == True):
                    i['status'] = False
            msg = 'Thank you for visit'
            client.conn.send(bytes(msg+'\nAny request?', 'utf-8'))
            break
        elif (paymentMethod == '2'):
            msg = f'Input your number of bank card: '
            client.conn.sendall(bytes(msg, 'utf-8'))

            while True:
                clientInput = client.conn.recv(1024)
                numberOfBankCard = clientInput.decode("utf8")
                if (checkFunc.checkNumberOfBankCard(numberOfBankCard) == True):
                    for i in orderData[str(client.addr[1])]:
                        if (i['status'] == True):
                            i['status'] = False
                    msg = 'Thank you for visit'
                    client.conn.send(bytes(msg+'\nAny request?', 'utf-8'))
                    break
                else:
                    msg = 'Your number of bank card not found. Please try again:'
                    client.conn.send(bytes(msg, 'utf-8'))
            break
        else:
            msg = 'Not found. Please try again'
            client.conn.send(bytes(msg, 'utf-8'))
    
    writeJson(orderData, 'orderList.json')

def addFood(client):
    orderData = readJson('orderList.json')
    currentTime = time.ctime()
    
    isTrue = False
    isClientOrderBefore = False
    for i in orderData:
        if int(i) == int(client.addr[1]):
            isClientOrderBefore = True
            break
    if(isClientOrderBefore == False):
        msg = 'Please order food first!'
        client.conn.sendall(bytes(msg, 'utf-8'))
        return
    for i in orderData[str(client.addr[1])]:
        if (checkFunc.checkDiffTimeUnderSecondHours(i['time'], currentTime)):
            isTrue = True
            break
    if (isTrue == False ):
        msg = 'You can\'t add more food because the time is out!\nPlease order other food!'
        client.conn.sendall(bytes(msg, 'utf-8'))
        return
    msg = 'Input name of food: '
    client.conn.sendall(bytes(msg, 'utf-8'))
    dataMenu = readJson('menu.json')
    
    while True:
        data = client.conn.recv(1024)
        foodName = data.decode("utf8")
        foodNames = foodName.split(',')
        if (checkFunc.checkFoodName(foodNames, dataMenu)): 
            break
        else:
            msg = 'Not found food\nPlease try again'
            client.conn.sendall(bytes(msg, 'utf-8'))

    amountFoods = []
    for i in foodNames:
        msg = f'Input amount of {i}: '
        client.conn.sendall(bytes(msg, 'utf-8'))
        data = client.conn.recv(1024)
        amountFood = int(data.decode("utf8"))
        amountFoods.append(amountFood)
    
    clientOrderList = []
    for i in range(len(foodNames)):
        createFoodOrder = definedObj.OrderFood(client, foodNames[i], amountFoods[i])
        clientOrderList.append(createFoodOrder.getOrderFood())

    orderData = readJson('orderList.json')
    isClientOrderBefore = False
    for i in orderData:
        if int(i) == int(client.addr[1]):
            isClientOrderBefore = True
            break
    
    if (isClientOrderBefore):
        orderData[str(client.addr[1])] = orderData[str(client.addr[1])] + clientOrderList
    else:
        orderData = orderData | {
            client.addr[1]: clientOrderList
        }

    writeJson(orderData, "orderList.json")
    orderData = readJson('orderList.json')
    totalBill = 0
    for i in orderData[str(client.addr[1])]:
        if (i['status'] == True):
            totalBill += i['totalPrice']
    payBill(client)