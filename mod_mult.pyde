from draw_table import draw_table

PERFRAME = 1000

def setup():
    global tab
    size(1009, 1009)
    colorMode(HSB, 255, 255, 255)
    noStroke()
    background(0)
    tab = draw_table(1)

def draw():
    try:
        for _ in xrange(PERFRAME):
            next(tab)
    except StopIteration:
        pass