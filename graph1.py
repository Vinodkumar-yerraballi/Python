from collections import deque 
class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graph",self.graph_dict)
    
    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    def get_shorets_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shorets_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path=sp
        return shortest_path
    def find_shorest_path(self,start,end): 
        dist={start:[start]}
        a=deque(start)
        while len(a):
            at=a.popleft()
            for next in [at]:  
                if next not in dist:
                    dist[next]=[dist[at],next]
                    a.append(next)
        return dist.get(end)

             


if __name__=="__main__":

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes1 = [
        ("Mumbai", "Paris","Vs Bangaluru"),
        ("Mumbai", "Dubai","vs Chennia"),
        ("Paris", "Dubai","Vs Surat"),
        ("Paris", "New York","Pune"),
        ("Dubai", "New York","Varanasi"),
        ("New York", "Toronto","Hyderabad"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_path(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shorets_path(start,end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_path(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shorets_path(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.find_shorest_path(start,end))