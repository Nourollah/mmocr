# Text Recognition Training set, including:
# Synthetic Datasets: SynthText, Syn90k

train_root = 'data/mixture'

train_img_prefix1 = f'{train_root}/Syn90k/mnt/ramdisk/max/90kDICT32px'
train_ann_file1 = f'{train_root}/Syn90k/label.lmdb'

train1 = dict(
    type='OCRDataset',
    img_prefix=train_img_prefix1,
    ann_file=train_ann_file1,
    loader=dict(
        type='AnnFileLoader',
        repeat=1,
        file_format='lmdb',
        parser=dict(type='LineJsonParser', keys=['filename', 'text'])),
    pipeline=None,
    test_mode=False)

train_img_prefix2 = f'{train_root}/SynthText/' + \
    'synthtext/SynthText_patch_horizontal'
train_ann_file2 = f'{train_root}/SynthText/label.lmdb'

train_img_prefix3 = f'{train_root}/SynthText_Add'
train_ann_file3 = f'{train_root}/SynthText_Add/label.txt'

train2 = dict(train1)
train2['img_prefix'] = train_img_prefix2
train2['ann_file'] = train_ann_file2

train3 = dict(
    type='OCRDataset',
    img_prefix=train_img_prefix3,
    ann_file=train_ann_file3,
    loader=dict(
        type='AnnFileLoader',
        repeat=1,
        file_format='txt',
        parser=dict(
            type='LineStrParser',
            keys=['filename', 'text'],
            keys_idx=[0, 1],
            separator=' ')),
    pipeline=None,
    test_mode=False)

train_list = [train1, train2, train3]
