import glob
import ipdb

file_dir = 'seg_images'
img_list = glob.glob(file_dir+"/img*")
train_vid = 'seq_train.txt'
test_vid = 'seq_test.txt'

def decode_txt(p):
    with open(p, 'r') as f:
        d = f.read()
        d = d.split('\n')
        d.pop()
        return d

train_list = decode_txt(train_vid)
test_list = decode_txt(test_vid)

ipdb.set_trace()
with open("synthia_train.txt", 'w') as f:
    for img in img_list:
        for i in train_list:
            if i in img:
                seg_name = img.replace("img", "seg")
                f.write(img + ' ' + seg_name + '\n')

with open("synthia_test.txt", 'w') as f:
    for img in img_list:
        for i in test_list:
            if i in img:
                seg_name = img.replace("img", "seg")
                f.write(img + ' ' + seg_name + '\n')


