

class TableBase():

    def __init__(self):
        print('TableBase')

class TableUtils():

    def __init__(self):
        print('TableUtils')

class BigTable(TableBase, TableUtils):

    def __init__(self):
        TableBase.__init__(self)
        TableUtils.__init__(self)
        print('BigTable')

if __name__ == '__main__':
    table = BigTable()
