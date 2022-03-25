# 算标签个数
import os.path
import glob
import xml.etree.ElementTree as ET

path = r'VOCdevkit/VOC2007/Annotations' 
#存储标签的路径，修改为自己的Annotations标签路径   
sum3 = 0
for xml_file in glob.glob(path + '/*.xml'):
     ####### 返回解析树
    tree = ET.parse(xml_file)
    ##########获取根节点
    root = tree.getroot()
    sum2 = 0
    for member in root.findall('object'):
        objectname = member.find('name').text
        sum = 0
        if objectname == 'playPhone':
            obname = objectname
            sum+=1
            sum2 = sum2+sum
            sum3 = sum2+sum3
print(obname,'=',sum3)
