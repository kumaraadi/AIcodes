
    ArrayList<Node> children = []
    char[][] state
    int heuristic
    Node parent
    int depth
    int nodeNu
    int visited
    
    def __init__(self, char[][] state,int heuristic,Node parent,int depth,int Nodenum,int visited){
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.depth= depth
        self.nodeNum = Nodenum
        self.visited = visited
    
    
    def addchild(Node n):
        children.add(n)
    
