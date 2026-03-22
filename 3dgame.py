
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import camera
from ursina import destroy
import random

app = Ursina()

# Environment
ground = Entity(model='plane', scale=(100,1,100), texture='grass', collider='box')
gun = Entity(model='cube', color=color.red, scale=(0.2,0.2,1), position=(0.5,-0.5,1.5), parent=camera.ui)

# Player
player = FirstPersonController()

# Enemy setup
enemies = []

def spawn_enemy():
    x = random.uniform(-20, 20)
    z = random.uniform(-20, 20)
    enemy = Entity(model='cube', color=color.green, scale=1, position=(x,1,z), collider='box')
    enemies.append(enemy)

# Spawn multiple enemies
for _ in range(5):
    spawn_enemy()

# Shooting logic
def input(key):
    if key == 'left mouse down':
        shoot()

def shoot():
    hit_info = raycast(camera.world_position, camera.forward, distance=100, ignore=[player, gun])
    if hit_info.hit:
        if hit_info.entity in enemies:
            enemies.remove(hit_info.entity)
            destroy(hit_info.entity)
            print("Enemy hit!")

app.run()
