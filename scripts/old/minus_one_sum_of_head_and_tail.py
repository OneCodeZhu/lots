#!/usr/bin/python


def sum_of_blue_remainder:
    for key in store.keys():
        sum_blurem = []
        for i in range(0,5):





fh = open('../history.data')
store = {}
for line in fh:
    redone = int(line.split(' ')[2])
    redtwo = int(line.split(' ')[3])
    redthree = int(line.split(' ')[4])
    redfour = int(line.split(' ')[5])
    redfive = int(line.split(' ')[6])
    blumin = int(line.split(' ')[7])
    blumax = int(line.strip('\n').split(' ')[8])
    redminus = redfive - redone
    bluminus = blumax - blumin
    yushusum = redone % 10 + redtwo % 10 + redthree % 10 + redfour % 10 + redfive % 10
    rightsum = blumin + blumax
    if line.split(' ')[1] == '12154':
        nextlink = '13001'
    elif line.split(' ')[1] == '13153':
        nextlink = '14001'
    else:
        nextlink = int(line.split(' ')[1]) + 1
    store[line.split(' ')[1]]={'red':[redone, redtwo, redthree, redfour, redfive],'blue':[blumin, blumax],'redminus': redminus, 'bluminus' : bluminus, 'nextlink': nextlink, 'yushusum':yushusum, 'rightsum': rightsum}

#print store
counts = 0
for key in store.keys():
    if key != '14027' and store[key]['rightsum'] in store[str(store[key]['nextlink'])]['red']:
        print "%s in %s ," %(store[key]['rightsum'], store[str(store[key]['nextlink'])]['red'])
        counts += 1
print "the percentage of right sum in next lottery is %d" %(counts)

counts = 0
for key in store.keys():
    if key != '14027' and store[key]['yushusum'] in store[str(store[key]['nextlink'])]['red']:
        print key
        counts += 1
print "yu shu in next lottery %d" %(counts)
