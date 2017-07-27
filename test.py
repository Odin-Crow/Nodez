from Node import Node, Connection

def main():
    node1 = Node('Test1','0/0/1',{'This_Var':'ThisValue'})
    node2 = Node('Test2','0/0/2',{'That_Var':'ThatValue'})

    node3 = Node('Test3')
    node4 = Node('Test4')

    connect12 = Connection('conn1_Name','0/0/3',{'This_Conn':'This_Value'})
    connect13 = Connection('conn_1to3')
    connect14 = Connection('conn_1to4')
    connect42 = Connection('conn_4to2')

    connect12.Connect(node1, node2)
    connect13.Connect(node1, node3)
    connect14.Connect(node1, node4)
    connect42.Connect(node4, node2)

    node1.saveToFile(node1)
    node2.saveToFile(node2)
    node3.saveToFile(node3)
    node4.saveToFile(node4)
    print(connect12.Node1.Name+' is the name of Node 1\n'+connect12.Node2.Name+' is the name of Node 2\n')
    for conn in node1.Connections:
        print(conn.Name + ' is connected to '+ conn.Name)

if __name__ == '__main__':
    main()