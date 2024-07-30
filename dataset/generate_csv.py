import json


data = {}
data['Name']='New_Barista'
visual_path = f"../environment/frontend_server/saved_videos/{data['Name']}"
data['Context']='Sarah ordered a cup of coffee from the new barista Amy at her regular cafe.'
data['Desire']='Sarah wants her coffee ready as soon as possible, since she is in a hurry.'
data['Belief']="Sarah believes that the new barista Amy can make the coffee quickly."
data['Outcome']="Amy is still not very skilled at operating the coffee machine and hasn't been able to make the coffee properly."
data['Emotion']='Sarah is a bit angry and very disappointed with the barista.'
data['Action']="Sarah walked over to the barista and canceled her coffee order."
data['Emotional Expression']='Angry and Disappointed Emoji'
data['Opposing Desire']="Sarah doesn't mind when her coffee will be ready."
data['Opposing Belief']="Sarah does not trust that the new barista can make good coffee."
data['Opposing Outcome']="Amy quickly and perfectly made the coffee."
data['Opposing Emotion']='Sarah was very relaxed and understanding of the barista.'
data['Opposing Action']="Sarah stayed in place and waited patiently."
data['Opposing Expression']='Chill and Relaxed Emoji'
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