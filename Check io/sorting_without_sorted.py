
def bubble_sort(items):
    new = ""
    items = list(items)
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                new += "".join((str(j), str(j+1), ","))
    if new.endswith(','):  #  need to strip off comma at the end
        return new[:-1]
    else:
        return new


print(bubble_sort((1, 2, 3, 1, 5, 3)))

