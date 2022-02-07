from typing import Callable
import json
import uuid
import dash
from dash import html, callback, callback_context, ALL, MATCH, ALLSMALLER
from dash.development.base_component import Component
from dash.dependencies import DashDependency, Input, Output, State

def css_id(element: Component) -> str:
    """Convert the ID of given Dash component into a css selector

    Args:
        element (Dash element): [description]

    Returns:
        [type]: [description]
    """
    id = json.dumps(element.id, sort_keys=True, separators=(",", ":"))
    for c in r'{}",:':
        id = id.replace(c, f"\\{c}")
    id = '#' + id
    return id


def isTriggered(component: DashDependency) -> bool:
    """Return true if the given dash component was the reasion for the enclosing callback being triggered

    Args:
        component (DashDependency): The calback component being tested

    Returns:
        bool: Return true if the given component is the trigger
    """
    ctx = callback_context
    if not ctx.triggered: return False
    prop_id = f'{json.dumps(component.id, sort_keys=True, separators=(",", ":"))}.{component.component_property}'
    return ctx.triggered[0]['prop_id'] == prop_id


def match(m: dict):
    """

    Args:
        m (dict): [description]

    Returns:
        [type]: [description]
    """

    class _Factory:

        def __init__(self, id: dict, dash_factory: DashDependency):
            self._id = id
            self.dash_factory = dash_factory

        def __getattr__(self, attr: str):
            cb = self.dash_factory(self._id, attr)
            return cb

    class Matcher:
        def __init__(self, match: dict):
            self.match = match

            # For each of the pattern matching dict entries we
            # create a lambda that can be called which in turn
            # calls our resolver method

            def _resolver(key):
                return lambda value : self.resolver(key, value)

            for key, value in match.items():

                if key in ['input', 'output', 'state']:
                    raise AttributeError(f'Invalid match key "{key}". Key values "input", "output" and "state" are not allowed')

                if value in [ALL, MATCH, ALLSMALLER]:
                    self.__dict__[key] = _resolver(key)

        def resolver(self, key: str, arg:str) -> dict:
            id = self.match.copy()
            id[key] = arg
            return id

        @property
        def input(self) -> _Factory:
            return _Factory(self.match, Input)

        @property
        def output(self) -> _Factory:
            return _Factory(self.match, Output)

        @property
        def state(self) -> _Factory:
            return _Factory(self.match, State)

    return Matcher(m)


def prefix(pfx:str) -> Callable[[str], str]:
    """Return a lambda that will prefix all component IDs with the given prefix

    Args:
        pfx (str): The Component prefix to be assigned

    Returns:
         ((str) -> str)
    """
    pfx = pfx.replace('.', '_')
    return lambda id :f'{pfx}_{id}'


class AIOPrefix:

    def __init__(self, component_id):
        self.component_id=component_id
        self.aio_id = str(uuid.uuid4())

    def id(self, subcomponent_id):
        return {
            'component': self.component_id,
            'subcomponent': subcomponent_id,
            'aio_id': self.aio_id
        }


class AIOBase(html.Div):

    def __init__(self, children):
        super().__init__(children)

    def callback(self, output, inputs=[], state=[]):
        return callback(output, inputs, state)


# Simple helper to get the Dash components identifier
#
#   my_checkbox.component_id
#
#   can now be just:
#
#   my_checkbox.id

DashDependency.id = property(lambda self: self.component_id)

class DashIOFactory:
    """Dash Dependency Factory

Inject DashIOFactory instances into the Dash component. The
factories will be accessable as follows:

    div = html.Div(id='xxx')
    children_attr = div.output.children

Will return the same Dash Dependency Output instance as:

    div = html.Div(id='xxx')
    children_attr = DashDependency.Output('xxx', 'children')

    Raises:
        TypeError: raised id the requested attribute not available on the component
        AttributeError: raised if the associated component has no id

    Returns:
        [obj] -- Dash dependency object Output|Input|State
    """

    def __init__(self, component, iofactory):

        # Add component id prefix if its not allready been done

        if not hasattr(component, '_spa_prefixed_id'):

            assert hasattr(component, 'id'), "The dash component must have an 'id' attribute"

            component._spa_prefixed_id = component.id

        self.component = component
        self.iofactory = iofactory


    def __getattr__(self, name):
        if not name in self.component.available_properties:
            raise AttributeError(f"'{self.component._type}' component '{self.component.id}' has no attribute '{name}'")

        dio = self.iofactory(self.component.id, name)
        self.__setattr__(name, dio)
        return dio

# The following three methods have been injected in to dash's
# Component class as properties 'input', 'output' and 'state'
# In each case, when the property is accessed in a dash callback
# the associated DashIOFactory instance will be invoked

def input(self):
    if not hasattr(self, '_spa_input'):
        self._spa_input = DashIOFactory(self, dash.dependencies.Input)
    return self._spa_input

def output(self):
    if not hasattr(self, '_spa_output'):
        self._spa_output = DashIOFactory(self, dash.dependencies.Output)
    return self._spa_output

def state(self):
    if not hasattr(self, '_spa_state'):
        self._spa_state = DashIOFactory(self, dash.dependencies.State)
    return self._spa_state

# Inject DashIOFactory instances into the Dash component

Component.input = property(input)
Component.output = property(output)
Component.state = property(state)
