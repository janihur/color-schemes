import itertools

# red 600          #E53935
# red 700          #D50000
# red 800          #C62828
# error main       #D32F2F
# error dark (900) #B71C1C

background_colors = [
    '#E53935',
    '#D50000',
    '#C62828',
    '#D32F2F',
    '#B71C1C',
]

# secondary/light  #EDF7FF
# primary/contrast #FFFFFF

text_colors = [
    '#EDF7FF',
    '#FFFFFF',
]

def get_colors() -> list[tuple[str, str]]:
    return list(itertools.product(background_colors, text_colors))