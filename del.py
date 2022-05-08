infile = open('mAP-master (1)\mAP-master\input\detection-results\model-20.txt','r')
transit = "" #创立空的字符串用于储存文件
for line in infile: #使用迭代器读取每一段文本文件的内容
    if 'weared' in line: #判断作者姓名是否在此行数据中
        words = line.rstrip('\n').split(' ') #去掉一行数据末尾的换行符，以空格为分割点分割字符串返回一个列表
        for word in words:
            if word == 'by':
                transit += word+' '
            else:
                transit += word.capitalize()+' ' #capitalize()返回首字母大写的字符串
        transit += '\n' #在此行末尾加上去掉的换行符
    else:
        transit += line #将数据写入过渡的字符串中
infile.close()
onfile = open('model-15.txt','w') #以清空原文本文件内容的方式打开文件写入
onfile.write(transit)
onfile.close()
