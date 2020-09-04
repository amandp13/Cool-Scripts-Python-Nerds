def statistics(f1):

    ''' Find number of lines , words and Characters in passed file '''
    try:
        file = open(f1)
    except:
        print('File not found ..')
        exit(0)
    d = {}
    d2 = file.readlines()
    # print(d2)  # debug
    d['lines'] = len(d2)
    d['words'] = 0
    d['characters'] = 0
    for r in d2:
        z = r.split()
        # print(z) # debug
        d['words'] += len(z)
        for x in str(z):
            if x.isalpha():
                # print(x) # debug
                d['characters'] += 1
    file.close()
    return d

z = input('Enter path / file name [ With exttention ] : ')
info = statistics(z)
print(f"\n Your file contains {info['lines']} Lines {info['words']} Words and {info['characters']} Characters.")
