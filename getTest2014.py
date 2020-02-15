import json

with open('/home/sseal2/annotations/captions_val2014.json') as f:
    data = json.load(f)

with open("test.txt", 'w') as f:
    for entry in data['annotations']:
        f.write('{} {}\n'.format(entry['image_id'], entry['caption']))
