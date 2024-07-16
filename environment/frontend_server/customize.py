from maze import Maze
from path_finder import path_finder
from utils import *
import json

maze = Maze("1").collision_maze

target_play_name = '1step'

play_path = f'compressed_storage/{target_play_name}'

move_path = f'{play_path}/master_movement.json'
meta_path = f'{play_path}/meta.json'

move_data = json.load(open(move_path))

def move_file(persona, time, pos, pronunciatio="🚶"):
    time = str(time)
    move_data[time][persona] = {
      "movement": [
          pos[0],
          pos[1]
      ],
      "pronunciatio": pronunciatio,
      "description": "sleeping @ the Ville:Dorm for Oak Hill College:Klaus Mueller's room:bed",
      "chat": None
    }
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)

def clear_file(persona, time):
    time = str(time)
    if persona in move_data[time]:
        move_data[time].pop(persona)
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)

def move(persona, start_pos, end_pos, start_time):
    path = path_finder(maze, start_pos, end_pos, collision_block_id, verbose=True)
    #print(path)
    #quit()
    n = len(path)
    for i in range(n):
        now = start_time + i
        move_file(persona, now, path[i])
    
def stop_move(persona, start_time, end_time):
    for i in range(end_time - start_time):
        now = start_time + i
        clear_file(persona, now)

def set_pos(persona, pos, time=0, pronunciatio='🧘‍♂️'):
    if persona in move_data[time]:
        move_data[time][persona]['movement'] = [pos[0], pos[1]]
    else:
        move_data[time][persona] = {
      "movement": [
          pos[0],
          pos[1]
      ],
      "pronunciatio": pronunciatio,
      "description": "sleeping @ the Ville:Dorm for Oak Hill College:Klaus Mueller's room:bed",
      "chat": None
    }

move('Klaus Mueller', (127, 46), (73, 14), 0)