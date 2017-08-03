
class Node:


    def __init__(self, n="Node", d="0/0/0", det={}):
        self.Name = n
        self.Date=d
        self.Details = det
        self.Connections=[]

    def addConnect(self, conn):
        self.Connections.append(conn)


    def saveToFile(self, node):

        file = open('nodes.csv','r')
        found = False
        #Find line
        lines = file.readlines()
        linesArr = []
        markLine = 0

        for line in lines:
            linesArr.append(line)
            spl = line.split(',')

            if spl[0] == node.Name:
                markLine = len(linesArr)
                found = True

        file.close()
        #If found, append
        if found==True:
            #print('[DEBUG] TRUE MARKLINE '+str(markLine))
            spl = linesArr[markLine-1].split(',')
            for n in node.Connections:
                found = False
                for ele in spl:
                    if ele == n.Name:
                        found = True
            if found == False:
                file = open('nodes.csv','w+')
                linesArr[markLine-1]+=
                for line in linesArr:
                    file.write(line)
                file.close()


        #If not found, new line
        if found == False:
            file = open('nodes.csv','a+')
            print('[DEBUG] NOT FOUND')
            connections = []
            connections.append(node)
            for n in node.Connections:
                connections.append(n)

            for n in connections:
                file.write(n.Name+',')

            file.write('\n')

        #Close
        file.close()

class Connection:

    def __init__(self, n="Connection", d="0/0/0", det={}):
        self.Name=n
        self.Date=d
        self.Details=det

    def Connect(self, Node1, Node2):
        self.Node1 = Node1
        self.Node2 = Node2

        Node1.addConnect(self.Node2)
        Node2.addConnect(self.Node1)