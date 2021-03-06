# 选出需要的标签和对应的图片
import os
# from types import ClassMethodDescriptorType
import cv2
import xml.etree.cElementTree as ET
# 原来路径
images_dir = 'VOCdevkit\VOC2007\JPEGImages'
xml_dir = 'VOCdevkit\VOC2007\Annotations'
# 移动到的路径
afimages_dir = 'VOCdevkit/VOC2007/JPEGImages2/'
afxml_dir = 'VOCdevkit\VOC2007\Annotations2'
# #创建列表
xmls = []
#读取xml文件名(即：标注的图片名)
for xml in os.listdir(xml_dir):
    path_xml = os.path.join(xml_dir, xml)
    tree = ET.parse(path_xml)
    root = tree.getroot()
    for member in root.findall('object'):
        objectname = member.find('name').text
        if objectname == 'noGloved':
            tree.write(os.path.join(afxml_dir,xml))
# 加上这部分代码可以将得到的标签文件里面不需要的标签删掉
##########################################################
xmls1 = []
#classes里面写上你需要的标签，其他标签会被删掉
classes = ['gloved','noGloved']
for xml in os.listdir(afxml_dir):
    path_xml = os.path.join(afxml_dir, xml)
    tree = ET.parse(path_xml)
    root = tree.getroot()
    for member in root.findall('object'):
        objectname = member.find('name').text
        if not objectname in classes:
            root.remove(member)
    tree.write(os.path.join(afxml_dir,xml))
##############################################################
# !/usr/bin/python
# -*- coding: UTF-8 -*-
list_pic = os.listdir(images_dir)
for xml_file_name in os.listdir(afxml_dir):
    pic_file_name = os.path.splitext(xml_file_name)[0] + ".jpg"
    pic_file_path = os.path.join(images_dir,pic_file_name)
    image = cv2.imread(pic_file_path)
    cv2.imwrite(afimages_dir + pic_file_name, image)
