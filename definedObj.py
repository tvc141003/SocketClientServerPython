import time
import handleFunc

class Food:
    def __init__(self, name, price, description, picture):
        self.name = name
        self.price = price
        self.description = description
        self.picture = picture
    
    def getFood(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "picture": self.picture
        }

class Client:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

class OrderFood:
    def __init__(self, client, name, amount):
        self.id = client.addr[1]
        self.foodName = name
        self.amount = amount
        self.time = time.ctime()
        self.status = True

    
    def getOrderFood(self):
        dataMenu = handleFunc.readJson('menu.json')
        price = 0
        for i in dataMenu:
            if i['name'] == self.foodName:
                price = int(i['price'])
                break
        return {
            'id': self.id,
            'foodName': self.foodName,
            'price': price,
            'amount': self.amount,
            'totalPrice': price * int(self.amount),
            'time': time.ctime(),
            'status': self.status,
        }