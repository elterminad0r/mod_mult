def generate_coords(w, h):
    if w < h:
        for x, y in generate_coords(h, w):
            yield y, x

    for wi in xrange(w + 1):
        for x in xrange(min(wi, h) + 1):
            yield wi - x, x
    
    for hi in xrange(wi + 1, wi + h + 1):
        for x in xrange(hi - h, w + 1):
            yield x, hi - x

def draw_table(thick):
    w = width // thick
    h = height // thick
    for x, y in generate_coords(w, h):
        fill(x * y % min(w, h), 255, 255)
        rect(x * thick, y * thick, thick, thick)
        yield