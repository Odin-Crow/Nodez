
class Node:



    def __init__(self, n="Node", d="0/0/0", det={}):
        self.Name = n
        self.Date=d
        self.Details = det
        self.Connections=[]

    def addConnect(self, conn):
        self.Connections.append(conn)

class Connection:

    def __init__(self, n="Connection", d="0/0/0", det={}):
        self.Name=n
        self.Date=d
        self.Details=det

    def Connect(self, Node1, Node2):
        self.Node1 = Node1
        self.Node2 = Node2

        Node1.addConnect(self)
        Node2.addConnect(self)