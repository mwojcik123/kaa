from kaa.physics import BodyNodeType, BodyNode, HitboxNode
from kaa.geometry import Vector, Polygon
from common.enums import HitboxMask
import registry
import settings
from kaa.transitions import NodeSpriteTransition
import random
from common.enums import EnemyMovementMode



class Enemy(BodyNode):

    def __init__(self, position, hp=100, *args, **kwargs):
        # node's properties
        super().__init__(body_type=BodyNodeType.dynamic, mass=1,
                         z_index=10, position=position,
                         transition=NodeSpriteTransition(registry.global_controllers.assets_controller.enemy_frames,
                                                         duration=max(200, random.gauss(400,100)), loops=0),
                         *args, **kwargs)
        self.stagger_time_left = 1
        
        self.add_child(HitboxNode(
            shape=Polygon([Vector(-8, -19), Vector(8, -19), Vector(8, 19), Vector(-8, 19), Vector(-8, -19)]),
            mask=HitboxMask.enemy,
            collision_mask=HitboxMask.all,
            trigger_id=settings.COLLISION_TRIGGER_ENEMY,
        ))
        if random.randint(0, 100) < 75:
            self.movement_mode = EnemyMovementMode.MoveToPlayer
        else:
            self.movement_mode = EnemyMovementMode.MoveToWaypoint
        self.current_waypoint = None  # for those which move to a waypoint, we'll keep its corrdinates here
        self.randomize_new_waypoint()  # and randomize new waypoint

        self.acceleration_per_second = 300  # how fast will enemy accelerate
        self.max_velocity = random.randint(75, 125)  # we'll make enemy stop accelerating if velocity is above this value

        
        
        # custom properties
        self.hp = hp

        
        

    def stagger(self):
        # use the "stagger" sprite
        self.sprite = registry.global_controllers.assets_controller.enemy_stagger_img
        # stagger stops enemy from moving:
        self.velocity = Vector(0, 0)
        # track time for staying in the "staggered" state
        self.stagger_time_left = 12

    def recover_from_stagger(self):
        # start using the standard sprite animation again
        self.transition=NodeSpriteTransition(registry.global_controllers.assets_controller.enemy_frames,
                                                        duration=max(200, random.gauss(400, 100)), loops=0)

        self.stagger_time_left = 0
    def randomize_new_waypoint(self):
        self.current_waypoint = Vector(random.randint(50, settings.VIEWPORT_WIDTH-50),
                                       random.randint(50, settings.VIEWPORT_HEIGHT-50))