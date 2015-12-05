

def safe_pawns(pawns):
    count = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for pawn in pawns:
        l, n = pawn
        next_letter = (alpha.index(str(l))+1)  # gives next letter
        prev_letter = (alpha.index(str(l))-1)  # gives previous letter

        dn = str(int(n) - 1)
        dl = alpha[next_letter]
        new_key = dl + dn

        if new_key in pawns:
            count += 1
        else:
            dl = alpha[prev_letter]  # repetitive code here, should optimize
            new_key = dl + dn
            if new_key in pawns:
                count += 1

    return count


safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1





















# def check_connection(self, network, first, second):
#     self.map = {}
#     for item in network:
#         new_network = item.split('-')
#     for connection in new_network:
#         a, b = connection
#         if b not in self.map.get(a, set()):  # if no b in a, return empty set
#             if a not in self.map:
#                 map[a] = set()
#             self.map[a].add(b)
#             if b not in self.map:
#                 self.map[b] = set()
#             self.map[b].add(a)
#             return True
#         return False
#
#
# check_connection(("dr101-mr99","mr99-out00","dr101-out00","scout1-scout2","scout3-scout1","scout1-scout4","scout4-sscout","sscout-super",),"super","scout2")


#network = ("dr101-mr99","mr99-out00","dr101-out00","scout1-scout2","scout3-scout1","scout1-scout4","scout4-sscout","sscout-super")


# below trying to make a dictionary.....can't figure it out

# network = ' '.join(network).split(' ')
# new_list = []
#
# for item in network:
#     new_item = item.replace('-', ',')
#     new_list.append(new_item)
#
#
# for item in new_list:
#     item = item.split(',')
#     print(item)

#first_network = [item.split() for item in ' '.join(first_network).split('-') if item]

#
# def check_connection(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end:
#             return path
#         if not graph.has_key(start):
#             return None
#         for node in graph[start]:
#             if node not in path:
#                 newpath = find_path(graph, node, end, path)
#                 if newpath: return newpath
#         return None
















