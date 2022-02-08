import pytest
from dash import html, ALL
from dash_spa import prefix, match

def test_prefix_id():
    pfx = prefix('dash')
    assert pfx('btn') == 'dash_btn'

def test_prefix_name():
    pfx = prefix(__name__)
    assert pfx('btn') == 'tests_test_component_id_btn'

def test_prefix_default():
    pfx = prefix()
    assert pfx('btn').startswith('i')

def test_id_simple():
    pfx = prefix('dash')
    btn = html.Button(id=pfx("button"))
    assert btn.id == "dash_button"
    assert btn.css_id == "#dash_button"


def test_id_match():
    pfx = prefix('dash')

    btn = match({'type': pfx('btn'), 'idx': ALL})
    btn1 = html.Button(id=btn.idx(1))

    assert btn1.id == {'type': 'dash_btn', 'idx': 1}
    assert btn1.css_id == '#\\{\\"idx\\"\\:1\\,\\"type\\"\\:\\"dash_btn\\"\\}'

    with pytest.raises(AttributeError):
        html.Button(id=btn.idxx(1))
