from functools import partial
from kivent_cython import GameSystem
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from math import radians
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


class AsteroidSystem(GameSystem):
    """docstring for AsteroidSystem"""
    def create_asteroid(self, pos):
        x, y = pos
        x_vel = randint(-100, 100)
        y_vel = randint(-100, 100)
        angle = radians(randint(0, 360))
        angular_velocity = radians(randint(-150, 150))

        shape_dict = {
            'inner_radius': 0,
            'outer_radius': 32,
            'mass': 50,
            'offset': (0, 0),
        }

        col_shape = {
            'shape_type': 'circle',
            'elasticity': .5,
            'collision_type': 1,
            'shape_info': shape_dict,
            'friction': 1.0,
        }

        col_shapes = [col_shape]

        physics_component = {
            'main_shape': 'circle',
            'velocity': (x_vel, y_vel),
            'position': (x, y),
            'angle': angle,
            'angular_velocity': angular_velocity,
            'vel_limit': 250,
            'ang_vel_limit': radians(200),
            'mass': 50,
            'col_shapes': col_shapes,
        }

        asteroid_component = {'health': 2}

        create_component_dict = {
            'cymunk-physics': physics_component,
            'physics_renderer': {'texture': 'asteroid.png'},
            'asteroids': asteroid_component,
        }

        component_order = ['cymunk-physics', 'physics_renderer', 'asteroids']

        self.gameworld.init_entity(create_component_dict, component_order)

    def asteroids_collide(self, space, arbiter):
        gameworld = self.gameworld
        entities = gameworld.entities

        asteroid1_id = arbiter.shapes[0].body.data
        asteroid2_id = arbiter.shapes[1].body.data
        asteroid1 = entities[asteroid1_id]
        asteroid2 = entities[asteroid2_id]

        asteroid1_data = asteroid1['asteroids']
        asteroid2_data = asteroid2['asteroids']
        asteroid1_data['health'] -= 1
        asteroid2_data['health'] -= 1

        if asteroid1_data['health'] <= 0:
            Clock.schedule_once(partial(
                gameworld.timed_remove_entity,
                asteroid1_id
            ))

        if asteroid2_data['health'] <= 0:
            Clock.schedule_once(partial(
                gameworld.timed_remove_entity,
                asteroid2_id
            ))

        print('{0} hit {1}'.format(asteroid1_id, asteroid2_id))


class TestGame(Widget):
    def __init__(self, *args, **kwargs):
        super(TestGame, self).__init__(*args, **kwargs)
        Clock.schedule_once(self._init_game)

    def init_game(self, dt):
        self.setup_states()
        self.set_state()
        self.setup_map()
        self.setup_collision_callbacks()

        self.load_stars()
        self.load_asteroids()
        Clock.schedule_interval(self.update, 1./60.)

    def _init_game(self, dt):
        try:
            self.init_game(0)
        except:
            print("Rescheduling init")
            Clock.schedule_once(self._init_game)

    def update(self, dt):
        self.gameworld.update(dt)

    def setup_states(self):
        self.gameworld.add_state(
            state_name='main',
            systems_added=['quadtree_renderer', 'physics_renderer'],
            systems_removed=[],
            systems_paused=[],
            systems_unpaused=[
                'quadtree_renderer', 'physics_renderer', 'cymunk-physics'],
            screenmanager_screen='main'
        )
        self.gameworld.add_state(
            state_name='pause',
            systems_added=['quadtree_renderer', 'physics_renderer'],
            systems_removed=[],
            systems_paused=['cymunk-physics'],
            systems_unpaused=['quadtree_renderer', 'physics_renderer'],
            screenmanager_screen='pause'
        )

    def set_state(self):
        self.gameworld.state = 'main'

    def set_pause(self):
        self.gameworld.state = 'pause'

    def setup_map(self):
        self.gameworld.currentmap = self.gameworld.systems['map']

    def load_stars(self):
        star_graphic = 'star.png'
        star_size = (28, 28)
        for i in range(50):
            rand_x = randint(0, self.gameworld.currentmap.map_size[0])
            rand_y = randint(0, self.gameworld.currentmap.map_size[1])
            create_component_dict = {
                'position': {'position': (rand_x, rand_y)},
                'quadtree_renderer': {
                    'texture': star_graphic,
                    'size': star_size,
                }
            }
            component_order = ['position', 'quadtree_renderer']

            self.gameworld.init_entity(create_component_dict, component_order)

    def load_asteroids(self):
        asteroid_system = self.gameworld.systems['asteroids']
        for i in range(50):
            rand_x = randint(0, self.gameworld.currentmap.map_size[0])
            rand_y = randint(0, self.gameworld.currentmap.map_size[1])

            asteroid_system.create_asteroid((rand_x, rand_y))

    def setup_collision_callbacks(self):
        systems = self.gameworld.systems
        physics = systems['cymunk-physics']
        asteroid_system = systems['asteroids']
        physics.add_collision_handler(
            1, 1,
            separate_func=asteroid_system.asteroids_collide
        )


class BasicApp(App):

    def build(self):
        pass

if __name__ == '__main__':
    BasicApp().run()
