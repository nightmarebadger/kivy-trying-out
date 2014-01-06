from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (StringProperty)
from kivy.uix.widget import Widget
from random import randint
import kivent_cython # import needed for kv to work!


class DebugPanel(Widget):
    """docstring for DebugPanel"""
    fps = StringProperty(None)

    def __init__(self, *args, **kwargs):
        super(DebugPanel, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.update_fps, .1)

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))


class TestGame(Widget):
    def __init__(self, *args, **kwargs):
        super(TestGame, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.init_game)

    def init_game(self, dt):
        self.setup_states()
        self.set_state()
        self.setup_map()
        self.load_star()
        Clock.schedule_interval(self.update, 1./60.)

    def update(self, dt):
        self.gameworld.update(dt)

    def setup_states(self):
        self.gameworld.add_state(
            state_name='main',
            systems_added=['quadtree_renderer'],
            systems_removed=[],
            systems_paused=[],
            systems_unpaused=['quadtree_renderer'],
            screenmanager_screen='main'
        )

    def set_state(self):
        self.gameworld.state = 'main'

    def setup_map(self):
        self.gameworld.currentmap = self.gameworld.systems['map']

    def load_star(self):
        star_graphic = 'star.png'
        star_size = (28, 28)
        for i in range(50):
            rand_x = randint(0, self.gameworld.currentmap.map_size[0])
            rand_y = randint(0, self.gameworld.currentmap.map_size[1])
            create_component_dict = {
                'position': {
                    'position': (rand_x, rand_y)
                },
                'quadtree_renderer': {
                    'texture': star_graphic, 'size': star_size
                }
            }
            component_order = ['position', 'quadtree_renderer']

            self.gameworld.init_entity(create_component_dict, component_order)


class BasicApp(App):

    def build(self):
        pass

if __name__ == '__main__':
    BasicApp().run()
