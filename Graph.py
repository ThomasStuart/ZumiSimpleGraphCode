from Node import Node
from Edge import Edge

class Graph:
    def __init__(self):
        self.nodes_dict = None
        self.edges_dict = None

    def create_simple(self):
        node_names = ['x', 'a', 's', 'b']
        node_pos = [(0, 10), (-10, 0), (0, 0), (10, 0)]
        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}
        e1 = Edge( "e1", nodes_dict['s'], nodes_dict['x'], 90, 270)
        e2 = Edge( "e2", nodes_dict['a'], nodes_dict['s'], 0, 180)
        e3 = Edge( "e3", nodes_dict['b'], nodes_dict['s'], 180, 0)

        edges_dict['sx'] = e1
        edges_dict['as'] = e2
        edges_dict['bs'] = e3

        # add e1 to both vertices
        nodes_dict['s'].edges.append(e1)
        nodes_dict['x'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['a'].edges.append(e2)
        nodes_dict['s'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['b'].edges.append(e3)
        nodes_dict['s'].edges.append(e3)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict

    def search(self, startChar, destinationChar):
        startNode = self.nodes_dict[startChar]
        destinationNode = self.nodes_dict[destinationChar]
        queue = []
        queue.append((startNode, []))

        while (len(queue) > 0):

            currNode, currRoute = queue.pop(0)
            currNode.visited = True

            if currNode == destinationNode:
                print("FOUND")
                return currRoute

            for edge in currNode.edges:
                # print("Examining edge from ->", edge.get_startNode_name(), "<- to ->", edge.get_endNode_name(), "<-" )
                if edge.startNode != currNode and edge.startNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append((edge, edge.get_endNodeDirToStartNode()))
                    # new_route.append(  edge.startNode )
                    queue.append((edge.startNode, new_route))
                elif edge.endNode != currNode and edge.endNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append((edge, edge.get_startNodeDirToEndNode()))
                    # new_route.append(edge.endNode)
                    queue.append((edge.endNode, new_route))

        return "FAILED"

'''
    def create_complex(self):
        node_names = ['x', 'y', 'z', 'a', 's', 'b']
        node_pos = [(-10, 10), (0, 10), (10, 10), (-10, 0), (0, 0), (10, 0)]
        # nodeS = ( 's' , (0, 0) , [], False )
        # nodeX = ( 'x' , (-10, 10) , [], False )
        # nodeY = ( 'y' , (0, 10) , [], False )
        # nodeZ = ( 'z' , (10, 10) , [], False )
        # nodeA = ( 'a' , (-10, 0) , [], False )
        # nodeB = ( 'b' , (10, 0) , [], False )

        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}
        e1 = Edge(nodes_dict['x'], nodes_dict['y'])
        e2 = Edge(nodes_dict['y'], nodes_dict['z'])
        e3 = Edge(nodes_dict['s'], nodes_dict['y']) # has s
        e4 = Edge(nodes_dict['s'], nodes_dict['z']) # has s
        e5 = Edge(nodes_dict['b'], nodes_dict['z'])
        e6 = Edge(nodes_dict['a'], nodes_dict['s'])
        e7 = Edge(nodes_dict['s'], nodes_dict['b']) # has s

        edges_dict['xy'] = e1
        edges_dict['yz'] = e2
        edges_dict['sy'] = e3
        edges_dict['sz'] = e4
        edges_dict['bz'] = e5
        edges_dict['as'] = e6
        edges_dict['sb'] = e7

        # add e1 to both vertices
        nodes_dict['x'].edges.append(e1)
        nodes_dict['y'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['y'].edges.append(e2)
        nodes_dict['z'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['s'].edges.append(e3)
        nodes_dict['y'].edges.append(e3)

        # add e4 to both vertices
        nodes_dict['s'].edges.append(e4)
        nodes_dict['z'].edges.append(e4)

        # add e5 to both vertices
        nodes_dict['b'].edges.append(e5)
        nodes_dict['z'].edges.append(e5)

        # add e6 to both vertices
        nodes_dict['a'].edges.append(e6)
        nodes_dict['s'].edges.append(e6)

        # add e7 to both vertices
        nodes_dict['s'].edges.append(e7)
        nodes_dict['b'].edges.append(e7)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict




    def create_d_graph(self):
        nodes_dict = {}
        edges_dict = {}

        node0 = Node( '0', (0,0))
        node1 = Node('1', (20, 0))
        node2 = Node('2', (20, -20))
        node3 = Node('3', (10, -10))
        node4 = Node('4', (30, -10))

        nodes_dict['0'] = node0
        nodes_dict['1'] = node1
        nodes_dict['2'] = node2
        nodes_dict['3'] = node3
        nodes_dict['4'] = node4

        e1 = Edge(nodes_dict['0'], nodes_dict['1'])
        e2 = Edge(nodes_dict['1'], nodes_dict['3'])
        e3 = Edge(nodes_dict['1'], nodes_dict['4'])
        e4 = Edge(nodes_dict['3'], nodes_dict['2'])
        e5 = Edge(nodes_dict['4'], nodes_dict['2'])


        edges_dict['01'] = e1
        edges_dict['13'] = e2
        edges_dict['14'] = e3
        edges_dict['23'] = e4
        edges_dict['24'] = e5

        # add e1 to both vertices
        nodes_dict['0'].edges.append(e1)
        nodes_dict['1'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['1'].edges.append(e2)
        nodes_dict['3'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['1'].edges.append(e3)
        nodes_dict['4'].edges.append(e3)

        # add e4 to both vertices
        nodes_dict['3'].edges.append(e4)
        nodes_dict['2'].edges.append(e4)

        # add e5 to both vertices
        nodes_dict['2'].edges.append(e5)
        nodes_dict['4'].edges.append(e5)

        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict
        
'''