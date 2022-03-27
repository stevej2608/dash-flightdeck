from components.table import TableAIOPaginator

class TestPaginator(TableAIOPaginator):

    PREVIOUS = 'Prev'
    NEXT = 'Next'

    def selectable(self, page:int, adjacents=2):
        return self.select(page, adjacents)

    def emit(self, page, active=False, disabled=False):
        markup = f"{page}".lower() if disabled else f"{page}".upper()
        if active:
            return f"[{markup}]"
        else:
            return f"{markup}"

def test_paginator1():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(1)
    assert ' '.join(p) == 'prev [1] 2 3 4 5 6 7 8 ... 19 20 NEXT'

def test_paginator2():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(2)
    assert ' '.join(p) == 'PREV 1 [2] 3 4 5 6 7 8 ... 19 20 NEXT'

def test_paginator4():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(4)
    assert ' '.join(p) == 'PREV 1 2 3 [4] 5 6 7 8 ... 19 20 NEXT'

def test_paginator5():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(5)
    assert ' '.join(p) == 'PREV 1 2 3 4 [5] 6 7 8 ... 19 20 NEXT'

def test_paginator6():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(6)
    assert ' '.join(p) == 'PREV 1 2 ... 4 5 [6] 7 8 ... 19 20 NEXT'

def test_paginator7():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(7)
    assert ' '.join(p) == 'PREV 1 2 ... 5 6 [7] 8 9 ... 19 20 NEXT'

    p = paginator.select(7, adjacents=3)
    assert ' '.join(p) == 'PREV 1 2 3 4 5 6 [7] 8 9 10 ... 19 20 NEXT'

def test_paginator14():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(14)
    assert ' '.join(p) == 'PREV 1 2 ... 12 13 [14] 15 16 ... 19 20 NEXT'

def test_paginator15():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(15)
    assert ' '.join(p) == 'PREV 1 2 ... 13 14 [15] 16 17 18 19 20 NEXT'

def test_paginator19():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(19)
    assert ' '.join(p) == 'PREV 1 2 ... 13 14 15 16 17 18 [19] 20 NEXT'

def test_paginator20():
    paginator = TestPaginator(total_items=100)
    p = paginator.select(20)
    assert ' '.join(p) == 'PREV 1 2 ... 13 14 15 16 17 18 19 [20] next'

def test_paginator_pages2():
    paginator = TestPaginator(total_items=10)
    p = paginator.select(1)
    assert ' '.join(p) == 'prev [1] 2 NEXT'

    p = paginator.select(2)
    assert ' '.join(p) == 'PREV 1 [2] next'

def test_paginator_pages1():
    paginator = TestPaginator(total_items=5)
    p = paginator.select(1)
    assert ' '.join(p) == ''
