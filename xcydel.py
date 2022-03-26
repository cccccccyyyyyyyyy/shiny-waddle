import os
import xml.etree.cElementTree as ET
images_dir = 'VOCdevkit\VOC2007\JPEGImages'
xml_dir = 'VOCdevkit\VOC2007\Annotations'

#创建列表
xmls = []
#读取xml文件名(即：标注的图片名)
for xml in os.listdir(xml_dir):
    path_xml = os.path.join(xml_dir, xml)
    tree = ET.parse(path_xml)
    root = tree.getroot()
    if len(root.findall('object'))==0:
         os.remove(os.path.join(xml_dir,xml))
    else:
    #xmls.append(os.path.splitext(xml)[0])    #append()参数：在列表末尾添加新的对象，即将所有文件名读入列表
        xmls.append(xml.split('.')[0])#splitext和split的区别：前者('0001','.jpg'), 后者('0001','jpg') 在此可选用
print(xmls)
#读取所有图片
for image_name in os.listdir(images_dir):
    image_name = image_name.split('.')[0]
    if image_name not in xmls:
        image_name = image_name + '.jpg'
        # print(image_name)
        os.remove(os.path.join(images_dir,image_name))
for xml in os.listdir(xml_dir):
    xml = xml.split('.')[0]
    if xml not in imgs:
        xml = xml +'.xml'
        os.remove(os.path.join(xml_dir,xml))


 
 
