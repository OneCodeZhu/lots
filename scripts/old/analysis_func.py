#!usr/bin/python


class lottery_parser():
    """use to generate data list and kill numbers"""
    def __init__(self,lotteryfile):
        self.baseurl = lotteryfile
        self.dict_block = {}
        self.indexlist = []

    def gen_data(self,baseurl):
        fh = open(baseurl, 'rb')
        for line in fh:
            self.dict_block[int(line.split()[1])] = [ int(x) for x in line.strip('\n').split()[2:]]
    def get_x_qi(self,baseqi,distance):
        try:
            tmplist = self.indexlist
            indexnum = tmplist.index(baseqi)
            dictnum = self.indexlist[ indexnum + distance ]
            return self.dict_block[dictnum]
        except ValueError:
            print "%s dose not exist!" % dictnum




if __name__ == '__main__':
    f = lottery_parser('../history.data')
    f.gen_data('../history.data')
