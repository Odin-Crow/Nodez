
class Node:


    def __init__(self, n="Node", d="0/0/0", det={}):
        self.Name = n
        self.Date=d
        self.Details = det
        self.Connections={}

    def addConnect(self, conn, desc):
        self.Connections[conn] = desc
        #conn.addConnect(self, desc)


    def saveToFile(self, node):

        file = open('nodes.csv','a+')
        nodes = file.readlines()
        print('[DEBUG] NODES : '+str(nodes)+'\n')
        #Check if Node exists in file
        nodeIn = '#'+node.Name in nodes
        #print('[DEBUG] Node '+node.Name+' is in file : '+str(nodeIn))
        #If it is not
        file.write('#'+node.Name+'\n\n')
        if not nodeIn:
            for n in node.Connections:
                file.write('~'+n.Name+' : '+node.Connections[n]+'\n')


        #If it is
            #Run through each connection, check if connection exists
            #If it does not



            #If it does



        file.close()


    def __del__(self):
        self.saveToFile(self)
