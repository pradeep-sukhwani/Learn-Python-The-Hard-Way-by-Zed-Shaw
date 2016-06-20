from sys import exit

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
			next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    def enter(self):
        print why, "Good Job!"
		exit(1)

class Start(Scene):
	
	def enter(self):
		print "Once upon a time their was a boy name 'Ichabod Crane' who loves a girl name 'Grace Abigail' known by 'Abbie'. One"
		print "day they were playing hide and seek and the girl has to hide somewhere so at a nearby distance she saw a house and"
		print "she thought it would be nice place to hide. As the front door was locked so she climbed up on that door and she jumped"
		print "inside and she felt and she was also bleeding and she drop one of her earings in front of the gate on the inside side."
		print "Ichabod was looking for her but he didn't find her, after some time he also found that house, he went near to the"
		print "front and he looked at one of her earings, so he climbed up he jumbed in and picked up her earings.\n"
		print "Now you see a door in front of you."
		print "Go there.\n"
		
class FreeRoom(Scene):

    def enter(self):
        pass

class PoisonRoom(Scene):

    def enter(self):
        pass

class IllusionRoom(Scene):

    def enter(self):
        pass

class AlienRoom(Scene):

    def enter(self):
        pass

class MummiesRoom(Scene):

    def enter(self):
        pass

class LionRoom(Scene):

    def enter(self):
        pass

class GirlRoom(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('FreeRoom')
a_game = Engine(a_map)
a_game.play()