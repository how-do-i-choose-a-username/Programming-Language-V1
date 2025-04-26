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

