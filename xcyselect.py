# 选出对应名称的标签
import os
import cv2
import xml.etree.cElementTree as ET
images_dir = 'VOCdevkit\VOC2007\JPEGImages'
afimages_dir = 'VOCdevkit\VOC2007\JPEGImages2'
xml_dir = 'VOCdevkit\VOC2007\Annotations'
afxml_dir = 'VOCdevkit\VOC2007\Annotations2'
#创建列表
xmls = []
#读取xml文件名(即：标注的图片名)
for xml in os.listdir(xml_dir):
    path_xml = os.path.join(xml_dir, xml)
    tree = ET.parse(path_xml)
    root = tree.getroot()
    for member in root.findall('object'):
        objectname = member.find('name').text
        if objectname == 'playPhone':
            tree.write(os.path.join(afxml_dir,xml))
#!/usr/bin/python
# -*- coding: UTF-8 -*-
list_pic = os.listdir(images_dir)
for xml_file_name in os.listdir(afxml_dir):
    pic_file_name = os.path.splitext(xml_file_name)[0] + ".JPG"
    pic_file_path = os.path.join(images_dir,pic_file_name)
    image = cv2.imread(pic_file_path)
    cv2.imwrite(afimages_dir + pic_file_name, image)