#!/usr/bin/python$
# coding=utf-8
import os
import os.path
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

rootdir = '/Users/Jack/Downloads/quanmindahui1/text'  # 指明被遍历的文件夹
print(os.path.isdir(rootdir))
from PIL import Image
# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
print(rootdir)

for parent, dirnames, filenames in os.walk(rootdir):

    for filename in filenames:  # 输出文件信息

        if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("jpeg"):
            try:
                image = Image.open(os.path.join(parent, filename))
                if filename.endswith("jpg") or filename.endswith("jpeg"):
                    replace_reg = re.compile(r'(jpg|jpeg)')
                    filenameNew = replace_reg.sub('png', filename)
                    # filenameNew = filename.replace(r"(jpg|jpeg)", "png")
                    # print(filenameNew)
                    if image.format == 'JPEG':
                        print(".jpg--jpg" + os.path.join(parent, filename))
                        image.save(os.path.join(parent, filename), 'PNG')
                        os.rename(os.path.join(parent, filename),
                                  os.path.join(parent, filenameNew))
                    if image.format == 'PNG':
                        print(".jpg--png" + os.path.join(parent, filename))
                        os.rename(os.path.join(parent, filename),
                                  os.path.join(parent, filenameNew))
                elif filename.endswith("png"):
                    if image.format != 'PNG':
                        print(".png--jpg" + os.path.join(parent, filename))
                    # if image.format == 'PNG':
                        # print(".png--png" + os.path.join(parent, filename))
            except:
                print('Exception %s' % os.path.join(parent, filename))

                # if image.format == 'PNG':
                #     print(os.path.join(parent, filename))
                #     image.save(os.path.join(parent, filename),'JPEG')
