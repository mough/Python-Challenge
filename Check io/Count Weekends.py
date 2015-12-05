from datetime import date, timedelta

def checkio(from_date, to_date):
    count = 0
    for day in generation(from_date, to_date):
        if day.isoweekday() == 6: count += 1
        elif day.isoweekday() == 7: count += 1

    return count


def generation(from_date, to_date):

    for d in range(int((to_date - from_date).days)+1):
        yield(from_date + timedelta(days=d))



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"



# Top Answer
# def checkio(d1, d2):
#     w1, w2 = d1.weekday(), d2.weekday()
#     count = (d2 - d1).days // 7 * 2
#     while True:
#         count += w2 > 4
#         if w1 == w2: return count
#         w2 = (w2 - 1) % 7