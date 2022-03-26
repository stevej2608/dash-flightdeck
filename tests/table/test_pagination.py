from paginator import paginate

def test_paginator1():
    p = paginate(1, total_items=100)
    assert ' '.join(p) == 'prev [1] 2 3 4 5 6 7 ... 19 20 NEXT'

def test_paginator2():
    p = paginate(2, total_items=100)
    assert ' '.join(p) == 'PREV 1 [2] 3 4 5 6 7 ... 19 20 NEXT'

def test_paginator4():
    p = paginate(4, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 3 [4] 5 6 7 ... 19 20 NEXT'

def test_paginator5():
    p = paginate(5, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 3 4 [5] 6 7 ... 19 20 NEXT'

def test_paginator7():
    p = paginate(7, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 5 6 [7] 8 9 ... 19 20 NEXT'

    p = paginate(7, adjacents=3, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 4 5 6 [7] 8 9 10 ... 19 20 NEXT'

    p = paginate(7, adjacents=4, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 3 4 5 6 [7] 8 9 10 11 ... 19 20 NEXT'

def test_paginator15():
    p = paginate(15, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 13 14 [15] 16 17 ... 19 20 NEXT'

def test_paginator16():
    p = paginate(16, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 14 15 [16] 17 18 19 20 NEXT'

def test_paginator19():
    p = paginate(19, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 14 15 16 17 18 [19] 20 NEXT'

def test_paginator20():
    p = paginate(20, total_items=100)
    assert ' '.join(p) == 'PREV 1 2 ... 14 15 16 17 18 19 [20] next'

def test_paginator_pages2():
    p = paginate(1, total_items=10)
    assert ' '.join(p) == 'prev [1] 2 NEXT'

    p = paginate(2, total_items=10)
    assert ' '.join(p) == 'PREV 1 [2] next'

def test_paginator_pages1():
    p = paginate(1, total_items=5)
    assert ' '.join(p) == ''
