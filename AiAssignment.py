def BFS(current_state, heur_function):
    visited = []
    while(current_state != "123456789ABCDEF "):
        if heur_function == "1":
            print("method called")

def AStar(current_state, heur_function):
    print("hey")


str = input()
newstr = []
newstr = str.split()

if len(newstr) == 3:
        init_state = newstr[0]
        search_method = newstr[1]
        heur_function = newstr[2]
  
        if search_method == "bfs":
            print("bfs in")
            BFS(init_state, heur_function)
        elif search_method == "astar":
            AStar(init_state, heur_function)
        else:
            print("Invalid search method!")
            exit(0)
else:
    print("Invalid arguments!")