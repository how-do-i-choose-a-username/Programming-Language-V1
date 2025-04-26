import re

def out(data):
    if (isinstance(data, int)):
        print(data)
    elif (isinstance(data, list)):
        string = ""
        for i in range(len(data)):
            string += chr(data[i] % 1114112)
        print(string)

def intin():
    data = input()
    data = "0" + data
    data = re.sub('[^0-9]','', data)
    data = int(data)
    return data

def lstin():
    text = input()
    data = []
    for i in range(len(text)):
        data.append(ord(text[i]))
    return data

def convert(data):
    if (isinstance(data, int)):
        #lst = []
        #text = str(data)
        #for i in range(len(text)):
        #    lst.append(int(text[i]))
        #return lst
        return [data]
    #elif (isinstance(data, list)):
    #    return len(data)
    else:
        return len(data)



class pos:
    x = int()
    y = int()
    
    def __init__(self, _x = 0, _y = 0):
        self.x = _x
        self.y = _y
        
    
    def __add__(self, position):
        sum = pos()
        sum.x = self.x + position.x
        sum.y = self.y + position.y
        return sum
        
    
    def __sub__(self, position):
        sum = pos()
        sum.x = self.x - position.x
        sum.y = self.y - position.y
        return sum
        
    

class lstpos:
    x = []
    y = []
    
    def __init__(self, position = pos()):
        self.x = self.x + convert(position.x)
        self.y = self.y + convert(position.y)
        
    
    def __add__(self, new):
        result = lstpos()
        result.x = self.x + new.x
        result.y = self.y + new.y
        return result
        
    
    def __len__(self, ):
        return convert(self.x)
        
    

worldSize = int()
worldSize = 15
def render( player, bullets):
    row = int()
    row = worldSize
    
    while True:
        output = []
        colom = int()
        while True:
            if (row == player.y  and  colom == player.x):
                output = output + convert(80)
                
            else:
                count = int()
                length = int()
                length = convert(bullets)
                while True:
                    if (row == bullets.y[count]  and  colom == bullets.x[count]):
                        output = output + convert(111)
                        break
                        
                    
                    count = count + 1
                    if (count == length):
                        output = output + convert(46)
                        break
                        
                    
                
            output = output + convert(32)
            colom = colom + 1
            if (colom > worldSize):
                break
                
            
        
        out(output)
        
        row = row - 1
        if (row < 0):
            break
            
        
    

bulletPos = lstpos()
bulletPos = lstpos(pos(5, 5))
bulletSpeed = lstpos()
bulletSpeed = lstpos(pos(1,0))
player = pos()
while True:
    
    render(player, bulletPos)
    
    first = int()
    second = int()
    length = int()
    dataIn = []
    dataIn = lstin()
    length = convert(dataIn)
    if (length > 0):
        first = dataIn[0]
        
    if (length > 1):
        second = dataIn[1]
        
    
    if (first == 32):
        if (second == 119):
            bulletPos.x = bulletPos.x + convert(player.x)
            bulletPos.y = bulletPos.y + convert(player.y)
            bulletSpeed.x = bulletSpeed.x + convert(0)
            bulletSpeed.y = bulletSpeed.y + convert(1)
            
        if (second == 115):
            bulletPos.x = bulletPos.x + convert(player.x)
            bulletPos.y = bulletPos.y + convert(player.y)
            bulletSpeed.x = bulletSpeed.x + convert(0)
            bulletSpeed.y = bulletSpeed.y + convert(-1)
            
        if (second == 97):
            bulletPos.x = bulletPos.x + convert(player.x)
            bulletPos.y = bulletPos.y + convert(player.y)
            bulletSpeed.x = bulletSpeed.x + convert(-1)
            bulletSpeed.y = bulletSpeed.y + convert(0)
            
        if (second == 100):
            bulletPos.x = bulletPos.x + convert(player.x)
            bulletPos.y = bulletPos.y + convert(player.y)
            bulletSpeed.x = bulletSpeed.x + convert(1)
            bulletSpeed.y = bulletSpeed.y + convert(0)
            
        
    if (first == 119):
        player = player + pos(0,1)
        
    if (first == 115):
        player = player + pos(0,-1)
        
    if (first == 97):
        player = player + pos(-1,0)
        
    if (first == 100):
        player = player + pos(1,0)
        
    if (player.x < 0):
        player.x = worldSize
        
    if (player.y < 0):
        player.y = worldSize
        
    if (player.x > worldSize):
        player.x = 0
        
    if (player.y > worldSize):
        player.y = 0
        
    
    
    dead = int()
    count = int()
    bulletLength = int()
    bulletLength = convert(bulletPos)
    while True:
        
        bulletPos.x[count] = bulletPos.x[count] + bulletSpeed.x[count]
        bulletPos.y[count] = bulletPos.y[count] + bulletSpeed.y[count]
        
        if (bulletPos.x[count] < 0):
            bulletPos.x[count] = worldSize
            
        if (bulletPos.y[count] < 0):
            bulletPos.y[count] = worldSize
            
        if (bulletPos.x[count] > worldSize):
            bulletPos.x[count] = 0
            
        if (bulletPos.y[count] > worldSize):
            bulletPos.y[count] = 0
            
        
        if (bulletPos.x[count] == player.x  and  bulletPos.y[count] == player.y):
            dead = 1
            
        
        count = count + 1
        if (count == bulletLength):
            break
            
        
    
    if (dead == 1):
        break
        
    

deadMessage = []
deadMessage = deadMessage + convert(68)
deadMessage = deadMessage + convert(69)
deadMessage = deadMessage + convert(65)
deadMessage = deadMessage + convert(68)
out(deadMessage)
out(convert(bulletPos))
