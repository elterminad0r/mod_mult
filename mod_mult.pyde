from draw_table import draw_table

PERFRAME = 50

def setup():
    global tab
    size(1000, 1000)
    colorMode(HSB, 255, 255, 255)
    noStroke()
    background(0)
    tab = draw_table(4)

def draw():
    try:
        for _ in xrange(PERFRAME):
            next(tab)
    except StopIteration:
        pass