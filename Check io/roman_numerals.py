def checkio(data):
    result = ""

    while data > 0:
        if data >= 1000:
            result += 'M' * (data // 1000)
            data %= 1000
        if data >= 500:
            result += 'D' * (data // 500)
            data %= 500
        if data >= 100:
            result += 'C' * (data // 100)
            data %= 100
        if data >= 50:
            result += 'L' * (data // 50)
            data %= 50
        if data >= 10:
            result += 'X' * (data // 10)
            data %= 10
        if data >= 5:
            result += 'V' * (data // 5)
            data %= 5
        if data >= 1:
            result += 'I' * (data)
            break

    if 'DCCCC' in result:
        result = result.replace('DCCCC', 'CM')
    if 'CCCC' in result:
        result = result.replace('CCCC', 'CD')
    if 'LXXXX' in result:
        result = result.replace('LXXXX', 'XC')
    if 'XXXX' in result:
        result = result.replace('XXXX', 'XL')
    if 'VIIII' in result:
        result = result.replace('VIIII', 'IX')
    if 'IIII' in result:
        result = result.replace('IIII', 'IV')

    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CD XC IX', '499'
    assert checkio(3888) == 'MMM DCCC LXXX VIII', '3888'