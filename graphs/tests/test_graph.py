from graphs.graph_adjacent_list import GraphAdjacentList

class TestGraphFunctions:
    
    def test_add(self):
        graph = GraphAdjacentList(vertices=10)
        graph.add(first=0,sec=3)
        graph.add(first=0,sec=2)
        graph.add(first=2,sec=3)
        assert graph.graph[0].vertex == 2
        assert graph.graph[0].next.vertex == 3
        assert graph.graph[2].vertex == 3
        
    def test_bfs_traversal(self):
        graph = GraphAdjacentList(vertices=10)        
        graph.add(first=0,sec=5)
        graph.add(first=0,sec=2)
        graph.add(first=1,sec=2)
        graph.add(first=2,sec=3)
        graph.add(first=3,sec=4)
        graph.add(first=3,sec=5)
        assert graph.bfs_traversal() == [0,2,5,3,1,4]

    def test_dfs_traversal(self):
        graph = GraphAdjacentList(vertices=10)        
        graph.add(first=0,sec=5)
        graph.add(first=6,sec=5)
        graph.add(first=7,sec=6)
        graph.add(first=0,sec=2)
        graph.add(first=1,sec=2)
        graph.add(first=2,sec=3)
        graph.add(first=3,sec=4)
        assert graph.dfs_traversal() == [0,5,6,7,2,1,3,4]

    def test_find_path(self):
        graph = GraphAdjacentList(vertices=10)
        graph.add(first=0,sec=5)
        graph.add(first=0,sec=2)
        graph.add(first=1,sec=2)
        graph.add(first=2,sec=3)
        graph.add(first=5,sec=3)
        assert graph.find_path(value=3,paths=[]) == [[0,5,3],[0,2,3]]
        graph.add(first=1,sec=7)
        assert graph.find_path(value=1,paths=[]) == [[0,5,3,2,1],[0,2,1]]
        assert graph.find_path(value=7,paths=[]) == [[0,5,3,2,1,7],[0,2,1,7]]
        