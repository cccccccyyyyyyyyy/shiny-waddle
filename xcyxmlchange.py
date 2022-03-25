'''
通过解析xml文件，批量修改xml文件里的标签名称，比如把标签zero改成num
'''
import os.path
import glob
import xml.etree.ElementTree as ET

path = r'数据集\Annotations'    #存储标签的路径，修改为自己的Annotations标签路径   
sum3 = 0
for xml_file in glob.glob(path + '/*.xml'):
    ####### 返回解析树
	tree = ET.parse(xml_file)
	##########获取根节点
	root = tree.getroot()
	#######对所有目标进行解析
	# *******************************这个用来批量改打标文件名称
	# for member in root.findall('object'):
	# 	objectname = member.find('name').text
	# 	if objectname == 'uncovered':      #原来的标签名字
	# 		print(objectname)
	# 		member.find('name').text = str('cover')    #替换的标签名字
	# 		tree.write(xml_file)
	# ****************************************************************
	# ********************************这个用来统计xml文件夹中某个标签的数量
	sum2 = 0
	for member in root.findall('object'):
		objectname = member.find('name').text
		sum = 0
		if objectname == 'playPhone':
			sum+=1
		sum2 = sum2+sum
	sum3 = sum2+sum3
print(objectname,'=',sum3)
# ****************************************************************************


