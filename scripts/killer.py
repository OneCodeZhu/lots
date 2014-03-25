#!usr/bin/python
import sys
import math


def gen_data(baseurl):
    dict_block = {}
    fh = open(baseurl, 'rb')
    for line in fh:
        dict_block[int(line.split()[1])] = [ int(x) for x in line.strip('\n').split()[2:9]]
        dict_block[int(line.split()[1])].append(line.split()[0])
    return dict_block
def get_x_qi(phase,differ):
    try:
        tmplist = indexlist
        indexnum = tmplist.index(baseqi)
        dictnum = self.indexlist[ indexnum + distance ]
        return self.dict_block[dictnum]
    except ValueError:
        print "%s dose not exist!" % dictnum

def get_phase(datacol,phase,differ):
    if phase % 1000 < 4:
        print "not suitable for this case!"
    else:
        return datacol[phase + (differ)]

def kill_m1(inphase):
    return inphase[0] + inphase[4]

def kill_m2(inphase):
    return ( inphase[0] + inphase[4] + inphase[5] + inphase[6] ) / 3

def kill_m3(inphase):
    return (inphase[4] - inphase[0]) * (inphase[6] - inphase[5]) / 8.0

def kill_m4(inphase):
    return inphase[4] - inphase[0]

def kill_m5(inphase):
    return inphase[5] + inphase[6]

def kill_m6(inphase):
    return inphase[0] + inphase[5]

def kill_m7(inphase):
    return inphase[0] + inphase[6]

def kill_m8(inphase):
    return inphase[0] + inphase[1]

def kill_m9(inphase):
    return math.ceil((inphase[0] + inphase[1]) / 2.0)

def kill_m10(inphase1,inphase2):
    return inphase1[5] + inphase2[5]

def kill_m11(inphase1,inphase2):
    return inphase1[6] + inphase2[6]

def kill_m12(inphase1, inphase2):
    return inphase1[6] + inphase2[5]

def kill_m13(inphase):
    summ = 0
    for i in range(0,5):
        summ += inphase[i] % 10
    return summ

def kill_m14(inphase):
    return math.ceil(kill_m13(inphase) / 2.0)


def kill_list(data,inphase):
    phase_m4 = get_phase(data,nextphase,-4)
    phase_m3 = get_phase(data,nextphase,-3)
    phase_m2 = get_phase(data,nextphase,-2)
    phase_m1 = get_phase(data,nextphase,-1)
    klist = []
    klist = [kill_m1(phase_m4), kill_m2(phase_m4), kill_m3(phase_m4), \
             kill_m4(phase_m1),kill_m5(phase_m1),kill_m6(phase_m1),   \
             kill_m7(phase_m1),kill_m8(phase_m1),kill_m9(phase_m1),   \
             kill_m10(phase_m2, phase_m1),kill_m11(phase_m2, phase_m1),kill_m12(phase_m2, phase_m1),  \
             kill_m13(phase_m1), kill_m14(phase_m1) ]
    return klist


if __name__ == '__main__':
    nextphase = int(sys.argv[1])
    data = gen_data('../history.data')
    klist = kill_list(data, nextphase)
    print klist

