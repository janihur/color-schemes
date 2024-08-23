import itertools

# primary/main   #1D3B57
# primary/light  #1B4A7C
# secondary/dark #A1DAFF
# secondary/main #E0F3FF

background_colors = [
    '#1D3B57',
    '#1B4A7C',
    '#A1DAFF',
    '#E0F3FF',
]

# secondary/light   #EDF7FF
# primary/contrast  #FFFFFF
# black             #000000
# seconday/contrast #1D3B57
# primary/dark      #162D42
# grey900/10        #1F1F1F / #2E2F33

text_colors = [
    '#EDF7FF',
    '#FFFFFF',
    '#000000',
    '#1D3B57',
    '#162D42',
    '#1F1F1F',
    '#2E2F33',
]

def get_colors() -> list[tuple[str, str]]:
    return list(itertools.product(background_colors, text_colors))