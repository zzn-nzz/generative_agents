from maze import Maze
from path_finder import path_finder
from utils import *
import json

maze = Maze("1")
col_maze = maze.collision_maze
add_tiles = maze.address_tiles


target_play_name = 'Rainy_Party' # TODO

play_path = f'compressed_storage/{target_play_name}'

move_path = f'{play_path}/master_movement.json'
meta_path = f'{play_path}/meta.json'

move_data = json.load(open(move_path))

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

def get_last_data(persona, time):
    for t in range(time, -1, -1):
        t = str(t)
        if persona in move_data[t]:
            return move_data[t][persona]

def set_direction(persona, start_time, end_time, dir=None):
    for all_time in range(start_time, end_time + 1):
        # print(all_time)
        t = str(all_time)
        if persona not in move_data[t]:
            move_data[t][persona] = get_last_data(persona, all_time)
        # print(move_data[t][persona])
        move_data[t][persona]["face_dir"] = dir
        # print(move_data[t][persona])
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)
 
def move_file(persona, time, pos, pronunciatio="Hide", real_name=None, chat = ""):
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
      "chat": chat,
      "face_dir": None
    }
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)

def clear_file(persona, time):
    time = str(time)
    if persona in move_data[time]:
        move_data[time].pop(persona)
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)

def move(persona, end_pos, start_time, real_name=None, chat = ""):
    if persona in real_name_list:
        real_name = real_name_list[persona]
    start_pos = get_last_data(persona, start_time)["movement"]
    if isinstance(start_pos, str):
        start_pos = conv_coor(start_pos)
    if isinstance(end_pos, str):
        end_pos = conv_coor(end_pos)
    path = path_finder(col_maze, start_pos, end_pos, collision_block_id, verbose=True)
    #print(path)
    #quit()
    n = len(path)
    now = start_time
    for i in range(n):
        move_file(persona, now, path[i], chat=chat)
        now += 1
    return now

    
def stop_move(persona, start_time, end_time):
    for i in range(end_time - start_time):
        now = start_time + i
        clear_file(persona, now)

def adj_pos(pos, dir="left", stp=1, coor=None):
    if isinstance(pos, str):
        pos = conv_coor(pos)
    if coor != None:
        return (pos[0] + coor[0], pos[1] + coor[1])
    if dir == 'left':
        return (pos[0] - stp, pos[1])
    elif dir == 'right':
        return (pos[0] + stp, pos[1])
    elif dir == 'up':
        return (pos[0], pos[1] - stp)
    elif dir == 'down':
        return (pos[0], pos[1] + stp)


def set_pos(persona, pos, time=0, pronunciatio='Hide', real_name=None, chat = ""):
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
      "chat": chat,
      "face_dir": None
    }
    with open(move_path, 'w') as file:
        json.dump(move_data, file, indent=2)
# 'Isabella Rodriguez'
# 'Klaus Mueller'
# 'Maria Lopez'
clear_file_all()

real_name_list = { # TODO
    'Sam Moore': "Cam",
    'Tamara Taylor': "Bid",
    'Yuriko Yamamoto': "Dru"
}

to_official_name = {}

for key, value in real_name_list.items():
    to_official_name[value] = key

def toname(s):
    return to_official_name[s]

init_pos = { # TODO
    "Cam": adj_pos("the Ville:Johnson Park:park", coor=(7, -5)),
    "Bid": adj_pos("the Ville:Johnson Park:park", stp=2),
    "Dru": adj_pos("the Ville:Johnson Park:park", dir="right", stp=3)
}

dru = "Dru"
cam = "Cam"
bid = "Bid"
all_agents = [dru, cam, bid]
for agent in all_agents:
    set_pos(toname(agent), init_pos[agent], 0)

# Outcome
tstp = move(toname(dru), adj_pos(init_pos[cam], "left"), 5, chat="i am moving first")

set_direction(toname(dru), tstp, tstp + 6, 'r')
# # Opposite Outcome
# tstp = move(toname(dru), init_pos[dru], adj_pos(init_pos[cam], stp=0), 5)


# Expression
set_pos(to_official_name[cam], init_pos[cam], tstp + 3, pronunciatio="😔😭", chat="hi")

# # Opposite Expression
# set_pos(to_official_name[cam], init_pos[cam], tstp + 3, pronunciatio="😄😄")
# quit()
# # Action
# ref = "the Ville:Adam Smith's house:main room:refrigerator"
# n_tstp = move(toname(cam), init_pos[cam], init_pos[bid], tstp + 6)
# n_tstp = move(toname(dru), adj_pos(init_pos[cam], "left"), init_pos[bid], tstp + 8)
# nn_tstp = move(toname(cam), init_pos[bid], ref, n_tstp + 1)
# nn_tstp = move(toname(bid), init_pos[bid], ref, n_tstp + 3)
# nn_tstp = move(toname(dru), init_pos[bid], ref, n_tstp + 2)

# Opposite Action

set_direction(toname(cam), 0, tstp + 20, 'l')
tstp = move(toname(cam), adj_pos(init_pos[cam], coor=(-1, -3)), tstp + 20, chat="I am moving")

tstp = move(toname(dru), adj_pos(init_pos[cam], "left"), tstp + 20, chat="i am moving to cam")

