import os
del_dir="mAP-master (1)\mAP-master\input\detection-results"           #要处理文件的目录
filelist=os.listdir(del_dir)       #提取文件名存放在filelist中

for file in filelist:               #遍历文件名
    del_file=del_dir+'/'+file       #程序和文件不在同一目录下要用绝对路径
    lines = []
    gt = open(del_file).read().splitlines()
    for a in gt:
        spt = a.split(' ')
        if str(spt[0])==("unweared"):
            lines.append(a)
            lines.append('\n')
        else:
            continue
    fd=open(del_file,"w")
    fd.writelines(lines)
    fd.close