import json
import numpy as np
import os
from collections import defaultdict

captions_file = 'annotations/captions_val2014.json'

captions_file_image_ids = []
with open(captions_file) as f:
    data = json.load(f)
for entry in data['annotations']:
    captions_file_image_ids.append(entry['image_id'])

print('number of captions:', len(data['annotations']))
print('number of ids:', len(captions_file_image_ids))
print('number of unique ids:', len(np.unique(captions_file_image_ids)))
print('num_captions / 5:', len(data['annotations']) / 5.0)

# count frequencies                                                                                 \
                                                                                                     
d = defaultdict(int)
for id in captions_file_image_ids:
    d[id] += 1
frequencies = [d[key] for key in d]
# count frequencies of frequencies                                                                  \
                                                                                                     
d2 = defaultdict(int)
for count in frequencies:
    d2[count] += 1
print('frequencies:', d2)

print('------------')
images_dir = '/home/sseal2/val2014'
contents = os.listdir(images_dir)
print('length of all contents:', len(contents))
print('number of dirs:', np.count_nonzero([os.path.isdir(x) for x in contents]))
print('number that end in jpg:', np.count_nonzero([x.endswith('.jpg') for x in contents]))

print('-------------------')
image_ids = [x.replace('.jpg', '') for x in contents]
image_ids = [x.split('_')[-1] for x in image_ids]
image_ids = [str(int(x)) for x in image_ids]
captions_file_image_ids = [str(int(x)) for x in captions_file_image_ids]
image_ids = set(image_ids)
captions_file_image_ids = set(captions_file_image_ids)
print('len(image_ids):', len(image_ids))
print('len(captions_file_image_ids):', len(captions_file_image_ids))
intersection_set = image_ids.intersection(captions_file_image_ids)
print('len(intersection):', len(intersection_set))
