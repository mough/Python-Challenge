
start = '../channel/90052.txt'  # edited out real filepath

order = []


def get_next(start):
    with open(start, 'r') as f:
        text = f.read()
        for item in text.split():
            if item.isdigit():
                number = item
                order.append(item)
                start = '../channel/%s.txt' % number
                get_next(start)
            elif not any(ch.isdigit() for ch in text):
                print("STOPPED", text)
                break


def collect_comments():
    import zipfile
    new = []
    zf = zipfile.ZipFile('../channel.zip', 'r')
    for item in order:
        file = '%s.txt' % item
        new.append(zf.getinfo(file).comment.decode("utf-8"))

    print(' '.join(ch for ch in new))




get_next(start)
collect_comments()
