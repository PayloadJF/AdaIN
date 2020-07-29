# -*- coding: utf-8 -*-
# @File  : COCO_Wikiart_images_20000.py
# @Author: Fan Ji
# @Date  : 2020/7/29
# @Desc  :
# @Contact : fan.ji@cripac.ia.ac.cn

import os

size_of_datasets = 20000

content_dir_source = '/data4/fan.ji/test2017/test2017/'
style_dir_source = '/data4/fan.ji'
content_dir_train = '/data4/fan.ji/AdaIN/datasets/train/content/'
style_dir_train = '/data4/fan.ji/AdaIN/datasets/train/style/'

if not os.path.exists(content_dir_tran):
    os.makedirs(content_dir_train)

if not os.path.exists(style_dir_train):
    os.makedirs(style_dir_train)

for root, dirs, names in os.walk(content_dir_source):
    number = 0
    for name in names:
        img_path = os.path.join(root, name)
        target_path = os.path.join(content_dir_train, name)
        os.rename(img_path, target_path)
        print(number, '    ', size_of_datasets, '   content')
        number += 1
        if number >= size_of_datasets:
            break
    break

for root, dirs, names in os.walk(style_dir_source):
    number = 0
    for name in names:
        img_path = os.path.join(root, name)
        target_path = os.path.join(style_dir_train, name)
        os.rename(img_path, target_path)
        print(number, '    ', size_of_datasets, '    style')
        number += 1
        if number >= size_of_datasets:
            break
    break
