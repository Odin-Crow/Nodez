from Node import Node

def main():
    node1 = Node('Test1','0/0/1',{'This_Var':'ThisValue'})
    node2 = Node('Test2','0/0/2',{'That_Var':'ThatValue'})
    node3 = Node('Test3')
    node4 = Node('Test4')
    node5 = Node('Test5')

    node1.addConnect(node2, 'node1to2')
    node1.addConnect(node3, 'node1to3')
    node1.addConnect(node4, 'node1to4')
    node3.addConnect(node5, 'node3to5')

    for node, desc in node1.Connections.items():
        print(node.Name+' : '+desc)



if __name__ == '__main__':
    main()