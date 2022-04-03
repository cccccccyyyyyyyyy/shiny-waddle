#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os
import cv2
txt_dir = 'txt_out'
images_dir = 'VOCdevkit\VOC2007\JPEGImages'
afimages_dir = 'VOCdevkit/VOC2007/'
txts = []
imgs = []
for txt in os.listdir(txt_dir):
    txts.append(txt.split('.')[0])

for image_name in os.listdir(images_dir):
    imgs.append(os.path.splitext(image_name)[0])
    imgs.append(image_name.split('.')[0])
    image_name = image_name.split('.')[0]
    if image_name not in txts:
        image_name = image_name + '.jpg'
        pic_file_name = os.path.splitext(image_name)[0] + ".jpg"
        pic_file_path = os.path.join(images_dir,pic_file_name)
        image = cv2.imread(pic_file_path)
        # print(image_name)
        # os.remove(os.path.join(images_dir,image_name))
        cv2.imwrite(afimages_dir + pic_file_name, image)

for image_name in os.listdir(images_dir):
    imgs.append(os.path.splitext(image_name)[0])
    imgs.append(image_name.split('.')[0])
    image_name = image_name.split('.')[0]
    if image_name not in txts:
        image_name = image_name + '.jpg'
        pic_file_name = os.path.splitext(image_name)[0] + ".jpg"
        pic_file_path = os.path.join(images_dir,pic_file_name)
        # image = cv2.imread(pic_file_path)
        print(image_name)
        os.remove(os.path.join(images_dir,image_name))
        
from operator import length_hint
import os, sys
import glob
from PIL import Image

# 图像存储位置
src_img_dir = "VOCdevkit/VOC2007/JPEGImages"
# 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = "txt_out"
src_xml_dir = "VOCdevkit\VOC2007\Annotations"

cy = src_img_dir.split('/') 
t = len(cy)-1
img_Lists = glob.glob(src_img_dir + '/*.jpg')

img_basenames = [] # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))

img_names = [] # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)

for img in img_names:
    im = Image.open((src_img_dir + '/' + img + '.jpg'))
    width, height = im.size

    # open the crospronding txt file
    gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
    #gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write in xml file
    #os.mknod(src_xml_dir + '/' + img + '.xml')
    cyy = src_img_dir+img
    xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>'+str(cy[t])+'</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
    xml_file.write('    <path>'+str(cyy)+'</path>\n')
    xml_file.write('    <source>\n')
    xml_file.write('        <database>Unknown</database>\n')
    xml_file.write('    </source>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')

    # write the region of image on xml file
    i = 1
    for img_each_label in gt:
        spt = img_each_label.split(' ') #这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
        #print(spt)
        #spt打印['Images/s1.jpg', '391', '243', '428', '355', '426', '249', '468', '367', '']
        imax = len(spt)
        for i in range(0, imax-1 - 4, 4):
            #print(str(spt[i + 1]))
            xml_file.write('    <object>\n')
            xml_file.write('        <name>'+str(spt[0])+'</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(spt[i+2]) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(spt[i+3]) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(spt[i+4]) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(spt[i+5]) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')
    xml_file.write('</annotation>')