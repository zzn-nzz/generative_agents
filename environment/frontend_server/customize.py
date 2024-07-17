from maze import Maze
from path_finder import path_finder
from utils import *
import json

maze = Maze("1")
col_maze = maze.collision_maze
add_tiles = maze.address_tiles


target_play_name = '1step'

play_path = f'compressed_storage/{target_play_name}'

move_path = f'{play_path}/master_movement.json'
meta_path = f'{play_path}/meta.json'

move_data = json.load(open(move_path))

real_name_list = {
    'Klaus Mueller': "Tom",
    'Isabella Rodriguez': "Jen",
    'Maria Lopez': "Mar"
}

to_official_name = {
    "Tom": 'Klaus Mueller',
    "Jen": "Isabella Rodriguez",
    "Mar": "Maria Lopez"
}

def conv_coor(pos):
    # convert position name to coordinates
    for coor in add_tiles[pos]:
        return coor
    print(f"No place called {pos}")

def clear_file_all():
    for time in move_data:
        for persona in list(move_data[time].keys()):
            move_data[time].pop(persona)
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)

def move_file(persona, time, pos, pronunciatio="🚶", real_name=None):
    if persona in real_name_list:
        real_name = real_name_list[persona]
    if isinstance(pos, str):
        pos = conv_coor(pos)
    time = str(time)
    move_data[time][persona] = {
      "real_name": real_name,
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

def move(persona, start_pos, end_pos, start_time, real_name=None):
    if persona in real_name_list:
        real_name = real_name_list[persona]
    if isinstance(start_pos, str):
        start_pos = conv_coor(start_pos)
    if isinstance(end_pos, str):
        end_pos = conv_coor(end_pos)
    path = path_finder(col_maze, start_pos, end_pos, collision_block_id, verbose=True)
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

def set_pos(persona, pos, time=0, pronunciatio='🧘‍♂️', real_name=None):
    if persona in real_name_list:
        real_name = real_name_list[persona]
    if isinstance(pos, str):
        pos = conv_coor(pos)
    if not isinstance(time, str):
        time = str(time)
    if persona in move_data[time]:
        move_data[time][persona]['movement'] = [pos[0], pos[1]]
        move_data[time][persona]['real_name'] = real_name
    else:
        move_data[time][persona] = {
      "real_name": real_name,
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
# 'Isabella Rodriguez'
# 'Klaus Mueller'
# 'Maria Lopez'
clear_file_all()

init_pos = {
    "Tom": "the Ville:artist's co-living space:Latoya Williams's room:bed",
    "Mar": "the Ville:artist's co-living space:Rajiv Patel's room:guitar",
    "Jen": "the Ville:artist's co-living space:Abigail Chen's room:closet"
}

set_pos(to_official_name["Tom"], init_pos["Tom"], 0, '🙂😏')
set_pos(to_official_name["Mar"], init_pos["Mar"], 0, '🎵🤘🏻')
set_pos(to_official_name["Jen"], init_pos["Jen"], 0, '🧘🏻🔇')
#stop_move('Klaus Mueller', 0, 200)
move(to_official_name["Tom"], init_pos["Tom"], init_pos["Jen"], 0)