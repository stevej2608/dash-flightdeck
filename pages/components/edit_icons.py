import io
import os
import re

def read(filename):
    """Read file"""
    filename = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return fd.read()

icons = read('hero_icons.py')

result = re.findall(r"[A-Z_0-9]+_ICON.*?svg'", icons, re.MULTILINE | re.DOTALL)

icon_dict = {}
icon_compare = {}

for icon in result:
    name, svg = icon.split(' = ')
    if svg in icon_compare:
        print(f'Duplicate {name} - {icon_compare[svg]}')
        continue
    icon_dict[name] = svg
    icon_compare[svg] = name

# for k, v in sorted(icon_dict.items()):
#     print(f"{k} = {v})\n")

