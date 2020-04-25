class Edge:

    def __init__(self, eName, startNode , endNode, alpha, beta):
        self.edgeName = eName
        self.startNode = startNode
        self.endNode   = endNode
        self.startNodeDirToEndNode = alpha
        self.endNodeDirToStartNode = beta

    def get_edgeName(self):
        return self.edgeName

    def get_startNode(self):
        return self.startNode

    def get_endNode(self):
        return self.endNode


    def get_startNode_name(self):
        return self.startNode.name

    def get_endNode_name(self):
        return self.endNode.name

    def get_startNodeDirToEndNode(self):
        return self.startNodeDirToEndNode

    def get_endNodeDirToStartNode(self):
        return self.endNodeDirToStartNode