

# coding=utf-8
import os
import pygame
import random
# import tensorflow as tf
# from pygame.locals import *

'''
车牌号生成
'''

# pygame初始化
pygame.init()
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
city = ['京', '津', '沪', '渝', '冀', '豫', '云', '辽', '黑', '湘', '皖', '鲁', '新', '苏', '浙', '赣', '鄂', '桂', '甘', '晋', '蒙', '陕',
        '吉', '闽', '贵', '粤', '青', '藏', '川', '宁', '琼']

TRAINSIZE = 100  # 生成样本量
FILE_PATH = 'images/'


def save(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

#随机文本
def random_text(char_set=number + ALPHABET, captcha_size=7):
    rtext = []
    rtext.append(random.choice(city))
    rtext.append(random.choice(ALPHABET))
    for i in range(2, captcha_size):
        c = random.choice(char_set)
        rtext.append(c)
    str = ''.join(rtext)
    return str

#标签数据
def write_label(instr):
    label_filename = os.path.join(FILE_PATH, "plate/labels.txt")
    with open(label_filename, "a") as f:
        f.writelines(instr + ' ')

#图片数据
font = pygame.font.Font(os.path.join(FILE_PATH, "font/msyh.ttf"), 32)  # 注意这里Windows和Mac系统使用的方法是不同的
filepath = os.path.join(FILE_PATH, "plate/images")
fileformate = ".jpg"
if not os.path.exists(filepath):
    os.makedirs(filepath)

# 完全随机产生样本有可能使得某些中文字样本偏少无法得到很好的训练，
# 可以通过扩大样本生成量来解决，或者其他手段
for x in range(TRAINSIZE):
    text = random_text()
    # 渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
    ftext = font.render(text.decode('utf8'), True, (65, 83, 130), (255, 255, 255))
    filename = filepath + text + fileformate
    # 保存图片
    label = text + fileformate + "," + text
    # pygame.image.save(ftext, filename)
    #  图片保存地址,.decode('utf8')  解决中文路径乱码
    pygame.image.save(ftext, os.path.join(filepath, text.decode('utf8') + ".jpg"))
    write_label(label)
    print(label)

print("完成")