import logging
import inspect
import uuid
import dash
from dash import html, callback, ALL, MATCH
from dash.development.base_component import Component
from dash.dependencies import DashDependency

def _resolver(self, arg):
    key = inspect.stack()[0][3]
    logging.info('key=[%s]=%s', key, arg)


def match(m):

    class _Factory:

        def __init__(self, id, dash_factory):
            self.id = id
            self.dash_factory = dash_factory

        def __getattr__(self, attr):
            return self.dash_factory(self.id, attr)

    class _Match:
        def __init__(self, match):
            self.match = match
            for key, value in match.items():
                if value in [ALL, MATCH]:
                    self.__dict__[key] = lambda value : self.resolver(key, value)
                    # setattr(_Match, key, _resolver)

        # def io(self, id):
        #     return f'{self.prefix}_{id}'

        def resolver(self, key, arg):
            logging.info('key=[%s]=%s', key, arg)
            id = self.match.copy()
            id[key] = arg
            return id

        def callbackIO(self, attr, io_type):
            cb = io_type(self.match, attr)
            return cb

        @property
        def input(self):
            return _Factory(self.match, dash.dependencies.Input)


    return _Match(m)


def prefix(pfx):
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
