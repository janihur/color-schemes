import itertools

# green main #4B882B
# green dark #264416
# green 800  #2E7D32
# green 900  #1B5E20

background_colors = [
    '#4B882B',
    '#264416',
    '#2E7D32',
    '#1B5E20',
]

# secondary/light  #EDF7FF
# primary/contrast #FFFFFF

text_colors = [
    '#EDF7FF',
    '#FFFFFF',
]

def get_colors() -> list[tuple[str, str]]:
    return list(itertools.product(background_colors, text_colors))