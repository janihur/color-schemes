import importlib.util
import sys

from pathlib import Path
from string import Template


def load_module(module_file:Path) -> object:
    '''
    Loads a python module.

    See: https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    '''
    module_name = module_file.stem
    spec = importlib.util.spec_from_file_location(module_name, module_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

if __name__ == '__main__':
    color_config = load_module(Path(sys.argv[1]))
    all_color_combinations = color_config.get_colors()

    content = ''
    for colors in all_color_combinations:
        snippet = f'''
    <div class="color-scheme" style="background-color: {colors[0]}; color: {colors[1]};">
        <h1>Header Level One</h1>
        <p>background: <code>{colors[0]}</code> text: <code>{colors[1]}</code></p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo perferendis maxime rerum magni doloribus quo incidunt ab iusto, modi porro itaque, pariatur laboriosam optio! Odit amet sunt odio eveniet corrupti.</p>
        <h2>Header Level Two</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo perferendis maxime rerum magni doloribus quo incidunt ab iusto, modi porro itaque, pariatur laboriosam optio! Odit amet sunt odio eveniet corrupti.</p>
    </div>
'''
        content += snippet

    template = Path('template.html').read_text()
    template = Template(template).substitute(content = content)

    print(template)

