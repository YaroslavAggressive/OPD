#%% Augmentation using albumentations library
# step 1: load library. In Anaconda Prompt(Anaconda):
# pip install albumentations


augmentation_path = Constants.augmentation_path

# load images and masks
size = int(tmp.get_size())
images = []
masks = []
batch = 100
for i in range(0, size, batch):
    for j in range(batch):
        im, m = tmp.get_image(i + j)
        if im is None or mask is None:
            im, m = tmp.get_image(0)
        images.append(im)
        masks.append(m)
        print(i + j)

    original_height, original_width = images[0].shape[0], images[0].shape[1]
    # rotate and noise with crop
    aug = Compose([
        RandomSizedCrop(p=0.8, min_max_height=(original_height / 2 - 1, original_height), height=original_height - 1,
                        width=original_width - 1),
        OneOf([
            HorizontalFlip(p=0.6),
            VerticalFlip(p=0.6),
            Transpose(p=0.6)
        ], p=1),
        RandomRotate90(p=0.8),
        MultiplicativeNoise(multiplier=[0.5, 1.5], elementwise=True, per_channel=True, p=0.5)
    ])

    for k in range(batch):
        augmented = aug(image=images[k], mask=masks[k])
        Image.fromarray(augmented['image']).save(augmentation_path + "/Images/" + str(int(size / 2) + k + i) + '.jpeg')
        Image.fromarray(augmented['mask']).save(augmentation_path + "/Masks/" + str(int(size / 2) + k + i) + 'PalleteMask.jpeg')
    images.clear()
    masks.clear()
