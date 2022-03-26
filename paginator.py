import math

def getData(start, limit):
    return [f"I a row {row}" for row in range(start, limit)]


def paginate(page = 1, adjacents = 2, page_size = 5, total_items=None):
    """Ellipses pagination logic

    Args:
        page (int, optional): The active page. Defaults to 1.
        adjacents (int, optional): How many adjacent pages should be shown on each side. Defaults to 2.
        page_size (int, optional): How many items to show per page. Defaults to 5.
        total_items (int): Total number of items to be grouped into pages

    Example:

    Returns a string representing the the UI for pagination. The active page
    is in square brackets. For example:

```
        for page in range(1, 21):
            paginate(page, total_items=100)

        « previous [1] 2 3 4 5 6 7 ... 19 20 NEXT »
        « PREVIOUS 1 [2] 3 4 5 6 7 ... 19 20 NEXT »
        « PREVIOUS 1 2 [3] 4 5 6 7 ... 19 20 NEXT »
        « PREVIOUS 1 2 3 [4] 5 6 7 ... 19 20 NEXT »
        « PREVIOUS 1 2 ... 3 4 [5] 6 7 ... 19 20 NEXT »

        « PREVIOUS 1 2 ... 13 14 [15] 16 17 ... 19 20 NEXT »
        « PREVIOUS 1 2 ... 14 15 [16] 17 18 19 20 NEXT »

        « PREVIOUS 1 2 ... 14 15 16 17 18 [19] 20 NEXT »
        « PREVIOUS 1 2 ... 14 15 16 17 18 19 [20] next »

```
    """

    def emit(page, active=False, disabled=False):
        markup = f"{page}".lower() if disabled else f"{page}".upper()
        if active:
            return [f"[{markup}]"]
        else:
            return [f"{markup}"]

    # first item to display on this page

    start = (page - 1) * page_size

    # Get data.

    data = getData(start, page_size)

    lastpage = math.ceil(total_items / page_size)

    first_pages = emit(1) + emit(2)
    ellipsis = emit('...')
    last_pages = emit(lastpage - 1) + emit(lastpage)

    pagination = []

    # Previous button

    pagination += emit('prev', disabled = page == 1)

    # Determin Pages

    # Test to see if we have enough pages to bother breaking it up

    if lastpage < 7 + (adjacents * 2):
        for i in range(1, lastpage+1):
            pagination += emit(i, i == page)
    elif lastpage > 5 + (adjacents * 2):

        # Test to see if we're close to beginning. If so only hide later pages

        if page < 1 + (adjacents * 2):

            # PREVIOUS 1 [2] 3 4 5 6 7 ... 19 20 NEXT

            for i in range(1, 4 + (adjacents * 2)):
                pagination += emit(i, i == page)

            pagination += ellipsis
            pagination += last_pages

        elif lastpage - (adjacents * 2) > page and page > (adjacents * 2):

            # We're in the middle hide some front and some back
            # PREVIOUS 1 2 ... 5 6 [7] 8 9 ... 19 20 NEXT

            pagination += first_pages
            pagination += ellipsis

            for i in range(page - adjacents, page + adjacents + 1):
                pagination += emit(i, i == page)

            pagination += ellipsis
            pagination += last_pages
        else:

            # Must be close to end only hide early pages
            # PREVIOUS 1 2 ... 14 15 16 17 [18] 19 20 NEXT

            pagination += first_pages
            pagination += ellipsis

            for i in range(lastpage - (2 + (adjacents * 2)), lastpage + 1):
                pagination += emit(i, i == page)


    # Append the Next button

    pagination += emit("next", disabled=(page == lastpage))

    if lastpage <= 1 :
        pagination = []

    return pagination


if __name__ == "__main__":
    for page in range(1, 21):
        p = paginate(page, total_items=100)
        print(' '.join(p))
