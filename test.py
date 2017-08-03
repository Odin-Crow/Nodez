from Node import Node, Connection

def main():
    node1 = Node('Test1','0/0/1',{'This_Var':'ThisValue'})
    node2 = Node('Test2','0/0/2',{'That_Var':'ThatValue'})

    node3 = Node('Test3')
    node4 = Node('Test4')
    node5 = Node('Test5')

    connect12 = Connection('conn1_Name','0/0/3',{'This_Conn':'This_Value'})
    connect13 = Connection('conn_1to3')
    connect14 = Connection('conn_1to4')
    connect42 = Connection('conn_4to2')
    connect15 = Connection('conn_1to5')
    connect25 = Connection('conn_2to5')
    connect35 = Connection('conn_3to5')

    connect12.Connect(node1, node2)
    connect13.Connect(node1, node3)
    connect14.Connect(node1, node4)
    connect42.Connect(node4, node2)
    connect15.Connect(node1, node5)
    connect25.Connect(node2, node5)
    connect35.Connect(node3, node5)


if __name__ == '__main__':
    main()