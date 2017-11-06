import glob

TRAIN_FRACTION = 0.7
file_dir = 'seg_images'
img_list = glob.glob(file_dir+"/img*")
num_img = len(img_list)
num_train = int(num_img*TRAIN_FRACTION)
train_img = img_list[:num_train]
val_img = img_list[num_train:]

with open("synthia_train.txt", 'w') as f:
    for img in train_img:
        seg_name = img.replace("img", "seg")
        f.write(img + ' ' + seg_name + '\n')

with open("synthia_test.txt", 'w') as f:
    for img in val_img:
        seg_name = img.replace("img", "seg")
        f.write(img + ' ' + seg_name + '\n')


