import os
from kaa.sprites import Sprite, split_spritesheet
from kaa.geometry import Vector

class AssetsController:

    def __init__(self):
        # Load images:
        self.background_img = Sprite(os.path.join('assets', 'gfx', 'background.png'))
        self.title_screen_background_img = Sprite(os.path.join('assets', 'gfx', 'title-screen.png'))
        self.player_img = Sprite(os.path.join('assets', 'gfx', 'player.png'))
        self.machine_gun_img = Sprite(os.path.join('assets', 'gfx', 'machine-gun.png'))
        self.force_gun_img = Sprite(os.path.join('assets', 'gfx', 'force-gun.png'))
        self.grenade_launcher_img = Sprite(os.path.join('assets', 'gfx', 'grenade-launcher.png'))
        self.machine_gun_bullet_img = Sprite(os.path.join('assets', 'gfx', 'machine-gun-bullet.png'))
        self.force_gun_bullet_img = Sprite(os.path.join('assets', 'gfx', 'force-gun-bullet.png'))
        self.grenade_launcher_bullet_img = Sprite(os.path.join('assets', 'gfx', 'grenade-launcher-bullet.png'))
        self.enemy_stagger_img = Sprite(os.path.join('assets', 'gfx', 'enemy-stagger.png'))
        # few variants of bloodstains, put them in the same list so we can pick them randomly later
        self.bloodstain_imgs = [Sprite(os.path.join('assets', 'gfx', f'bloodstain{i}.png')) for i in range(1, 5)]

        # Load spritesheets
        self.enemy_spritesheet = Sprite(os.path.join('assets', 'gfx', 'enemy.png'))
        self.blood_splatter_spritesheet = Sprite(os.path.join('assets', 'gfx', 'blood-splatter.png'))
        self.explosion_spritesheet = Sprite(os.path.join('assets', 'gfx', 'explosion.png'))
        # enemy-death.png has a few death animations, so make this a list
        self.enemy_death_spritesheet = Sprite(os.path.join('assets','gfx','enemy-death.png'))

        # use the spritesheets to create framesets
        self.enemy_frames = split_spritesheet(self.enemy_spritesheet, frame_dimensions=Vector(33, 74))
        self.blood_splatter_frames = split_spritesheet(self.blood_splatter_spritesheet, frame_dimensions=Vector(50, 50))
        self.explosion_frames = split_spritesheet(self.explosion_spritesheet, frame_dimensions=Vector(100, 100), frames_count=75)

        self.enemy_death_frames = [
            split_spritesheet(self.enemy_death_spritesheet.crop(Vector(0, i*74), Vector(103*9, 74)),
                              frame_dimensions=Vector(103, 74)) for i in range(0, 5)
        ]
