import json


data = {}
data['Name']='Noisy Novel'
visual_path = f"../environment/frontend_server/saved_images/{data['Name']}"
data['Context']='Tom is attempting to complete his novel today.'
data['Desire']='Tom wants to finish his novel undisturbed.'
data['Belief']='Tom believes that his neighbor will be considerate and quite.'
data['Outcome']="Tom's neighbor constantly makes loud noise and distractions."
data['Emotion']='Tom feels angry and overwhelmed.'
data['Action']="Tom decides to knock on his neighbor's door and confronts his neighbor about the noise."
data['Emotional Expression']='Angry Emoji'
data['Opposing Desire']='Tom hopes he can complete his novel in a noisy environment because it will inspire him more.'
data['Opposing Belief']='Tom believes that his neighbor will be loud and noisy.'
data['Opposing Outcome']="Tom's neighbor is quiet and peaceful today."
data['Opposing Emotion']='Tom feels happy and content.'
data['Opposing Action']='Tom stays at home in peace.'
data['Opposing Expression']='Happy, Satisfied Emoji'
data['Desire_visual']='null'
data['Belief_visual']='null'
data['Outcome_visual']=f'{visual_path}/outcome.jpg'
data['Emotion_visual']=f'{visual_path}/'
data['Action_visual']='null'
data['Emotional Expression_visual']=f'{visual_path}/expression.jpg'
data['Opposing Desire_visual']='null'
data['Opposing Belief_visual']='null'
data['Opposing Outcome_visual']=f'{visual_path}/opposing_outcome.jpg'
data['Opposing Emotion_visual']='null'
data['Opposing Action_visual']='null'
data['Opposing Expression_visual']=f'{visual_path}/opposing_expression.jpg'

with open('data.json', 'r') as dat:
    orig_data = json.load(dat)
    orig_data.append(data)

with open('data.json', 'w') as dat:
    json.dump(orig_data, dat, indent=2)