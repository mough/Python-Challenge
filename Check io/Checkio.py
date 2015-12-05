
def checkio(n):
    possibles = []
    factors = [[i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0]

    print("factors", factors)

    for item in factors:
        possibles.append(''.join([str(i) for i in item]))

    smallest = int(possibles[0])
    for item in possibles:
        if int(item) < smallest:
            smallest = int(item)

    print(possibles)
    if str(n) in str(smallest):
        print(0)
    else:
        print(smallest)


checkio(125)

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(20) == 45, "1st example"
#     assert checkio(21) == 37, "2nd example"
#     assert checkio(17) == 0, "3rd example"
#     assert checkio(33) == 0, "4th example"
#     assert checkio(3125) == 55555, "5th example"
#     assert checkio(9973) == 0, "6th example"























# def find_path(graph, start, end, path=[]):
#         possibles = dict()
#         for i in graph.split(','):
#             possibles.setdefault(i[0], []).append(i[1])
#             possibles.setdefault(i[1], []).append(i[0])
#         print(possibles)
#
#         path = path + [start]
#         if start == end:
#             return path
#         if start not in possibles:
#             return None
#         for vertex in possibles[start]:
#             if vertex not in path:
#                 extended_path = find_path(vertex, end, path)
#                 if extended_path:
#                     return extended_path
#         return None
#
#
# print(find_path("12,23,34,45,56,67,78,81", 1, 7))

#This part is using only for self-testing
# if __name__ == "__main__":
#     def check_solution(func, teleports_str):
#         route = func(teleports_str)
#         teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
#         if route[0] != '1' or route[-1] != '1':
#             print("The path must start and end at 1")
#             return False
#         ch_route = route[0]
#         for i in range(len(route) - 1):
#             teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
#             if not teleport in teleports_map:
#                 print("No way from {0} to {1}".format(route[i], route[i + 1]))
#                 return False
#             teleports_map.remove(teleport)
#             ch_route += route[i + 1]
#         for s in range(1, 9):
#             if not str(s) in ch_route:
#                 print("You forgot about {0}".format(s))
#                 return False
#         return True
#
#     assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
#     assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
#     assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
#     assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"




