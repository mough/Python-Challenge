
class Friends(object):
    def __init__(self, connections):
        self.map = {}
        for connection in connections:
            self.add(connection)

    def add(self, connection):
        a, b = connection
        if b not in self.map.get(a, set()):  # if no b in a, return empty set
            if a not in self.map:
                map[a] = set()
            self.map[a].add(b)
            if b not in self.map:
                self.map[b] = set()
            self.map[b].add(a)
            return True
        return False


connections = ({'x','y'}, {'y','z'}, {'z','x'})

# more condensed version of add function
def add(self, connection):
        a, b = connection
        if b not in self.map.get(a, set()):  # if no b in a, return empty set
            self.map.setdefault(a,set()).add(b)
            self.map.setdefault(b,set()).add(a)
            return True
        return False

# using defaultdict
from collections import defaultdict

class Friends(object):
    def __init__(self, connections):
        self.map = defaultdict(set)  # make self.maps a dictionary of sets,
        for connection in connections:
            self.add(connection)

    def add(self, connection):
        a, b = connection
        if b not in self.map.get(a, set()):  # if no b in a, return empty set
            self.map[a].add(b)
            self.map[b].add(a)
            return True
        return False

def remove(self, connection):
    a, b = connection
    if b not in self.map.get(a,set()):
        return False
    self.map[a].discard(b)
    if not self.map[a]: # if self.map[a] is empty, will result to False, making that statement True and will delete self.map[a]
        del self.map[a]
    self.map[b].discard(a)
    if not self.map[b]: del self.map[a]  # can keep if statement on one line
    return True

def names(self):
    return set(self.map)