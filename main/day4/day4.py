class array:
    def __init__(self, array_text):
        self.array_text = array_text
        self.array = []
        for line in array_text:
            line = line.rstrip('\n')
            row = []
            for char in line:
                row.append(char)
            #print("Row:", row)
            self.array.append(row)

    def get_value(self, row, col):
        return self.array[row][col]
    
    def get_array(self):
        return self.array
    
class graph_from_array:
    def __init__(self, array):
        self.array = array
        self.graph = {}
        self.rows = len(array)
        self.cols = len(array[0])
        self.build_graph()
    def build_graph(self):  
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = []
                #all adjacent positions, including diagonals
                if r > 0:
                    neighbors.append((r - 1, c))
                if r < self.rows - 1:
                    neighbors.append((r + 1, c))
                if c > 0:
                    neighbors.append((r, c - 1))
                if c < self.cols - 1:
                    neighbors.append((r, c + 1))
                if r > 0 and c > 0:
                    neighbors.append((r - 1, c - 1))
                if r > 0 and c < self.cols - 1:
                    neighbors.append((r - 1, c + 1))
                if r < self.rows - 1 and c > 0:
                    neighbors.append((r + 1, c - 1))
                if r < self.rows - 1 and c < self.cols - 1:
                    neighbors.append((r + 1, c + 1))
                self.graph[(r, c)] = neighbors

    def get_neighbors(self, position):
        return self.graph.get(position, [])
    
    def get_value(self, position):
        r, c = position
        return self.array[r][c]
    
    def how_many_neighbors_are_paper(self, position):
        neighbors = self.get_neighbors(position)
        count = 0
        for neighbor in neighbors:
            r, c = neighbor
            if self.array[r][c] == '@':
                count += 1
        return count

def remove_paper(graph, position):
    r, c = position
    graph.array[r][c] = '.'

def loop_through_array(graph):
    accessible_papers = 0
    for position in graph.graph:
        if graph.how_many_neighbors_are_paper(position) < 4 and graph.get_value(position) == '@':
            remove_paper(graph, position)
            accessible_papers += 1
    return accessible_papers

with open('main/day4/arrayText.txt', 'r') as f:
    array_text = f.readlines()
    #print("Array Text:", array_text)
    rows = array(array_text)


    graph = graph_from_array(rows.get_array())
    accessible_papers = 1
    total_accessible_papers = 0
    while accessible_papers > 0:
        accessible_papers = loop_through_array(graph)
        total_accessible_papers += accessible_papers

    print(total_accessible_papers)
    


    