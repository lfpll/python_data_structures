from queue.queue import Queue
import logging

class Node:
    def __init__(self,data) -> None:
        self.vertex = data
        self.next = None

class GraphAdjacentList:

    def __init__(self,vertices: int) -> None:
        self.vertices = vertices
        self.graph = [None] * self.vertices
        
    def add(self,first: int,sec: int):
        node = Node(sec)
        node.next = self.graph[first]
        self.graph[first] = node
        
        node = Node(first)
        node.next = self.graph[sec]
        self.graph[sec] = node

    def dfs_traversal(self):        
        stack = []        
        path  = []
        visited = [None] * self.vertices
        
        stack.append([0,self.graph[0]])

        while stack:
            vertex,node = stack.pop()

            if not visited[vertex]:
                visited[vertex] = True
                path.append(vertex)

            while node:
                if not visited[node.vertex]:
                    stack.append([node.vertex,self.graph[node.vertex]])
                node = node.next
            
        return path

    def bfs_traversal(self):
        path = []
        visited = [False] * self.vertices
        que = Queue(size=20)
        que.enqueue((0,self.graph[0]))

        while not que.is_empty(): 
            vertex,node = que.dequeue()

            if not visited[vertex]:
                path.append(vertex)
                visited[vertex] = True
            
            while node:
                if not visited[node.vertex]:
                    que.enqueue((node.vertex,
                                 self.graph[node.vertex]))
                
                node = node.next
                    
        return path

    def find_path(self,value: int,paths: list,
                  path: list = [0],visited: list = None,
                  node: Node = None) -> list:

        # Creating visited array if does not exists
        if not visited:
            visited = [False] * self.vertices
            visited[0] = True

        # Start by the root
        if not node:
            node = self.graph[0]

        # Value found
        if node.vertex == value:
            this_path = path + [node.vertex]
            paths.append(this_path)
        else:
            if node.next:
                # Creating new reference of visited
                this_visited = list(visited)
                self.find_path(paths=paths,value=value,
                            path=path,visited=this_visited,
                            node=node.next)    
            
            # Continue iteration if value was not visited
            if not visited[node.vertex]:
                visited[node.vertex] = True
                this_path = path + [node.vertex]

                self.find_path(paths=paths,value=value,
                            path=this_path,visited=visited,
                            node=self.graph[node.vertex])            
            
        return paths



        

