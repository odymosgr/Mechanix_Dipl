class Graph:
  def __init__ (self, V, E):
    self.E = set(frozenset((u,v)) for u,v in E)
    self._nbrs = {}
    for v in V: 
      self.addvertex(v)
    for u,v in self.E:
      self.addedge(u,v)

  def adj_dict(self):
    return self._nbrs

  def nbrs(self, v): 
    return iter(self._nbrs[v])

  def addvertex(self, v):
    if v not in self._nbrs:
      self._nbrs[v] = set()

  def addedge(self, u, v):
    self.addvertex(u)
    self.addvertex(v)
    self.E.add(frozenset((u,v)))
    self._nbrs[u].add(v)
    self._nbrs[v].add(u)

  def removeedge(self, u, v):
    e = frozenset((u,v))
    if e in self.E:
      self.E.remove(e)
      self._nbrs[v].remove(v)
      self._nbrs[u].remove(u)
  
  def removevertex(self, u):
    todelete = list(self.nbrs(u))
    for v in todelete:
      self.removeedge(u,v)
    del self._nbrs[u]

  def is_bipartite(self):
    set1 = set()
    set2 = set()

    for v in self._nbrs:
      if v not in set2:
        set1.add(v)
        for nbr in self._nbrs[v]:
          if nbr in set1: return False
          set2.add(nbr)
      else:
        for nbr in self._nbrs[v]:
          if nbr in set2: return False
          set1.add(nbr)
    return True



if __name__ == "__main__":
  g = Graph({1,2,3,4}, {(1,2), (2,3), (1,3), (2,4), (3,4)})
  for i in g.nbrs(2): print(i)