import os
import shutil

# 进入要操作的文件夹
os.chdir('D:\\val2014')

# 创建目标文件夹
if not os.path.exists('D:\\pycharm_python_project\\yolo3-pytorch-bilibili-1\\VOCdevkit\\VOC2007\\JPEGImages'):
    os.mkdir('D:\\pycharm_python_project\\yolo3-pytorch-bilibili-1\\VOCdevkit\\VOC2007\\JPEGImages')

# 遍历源文件夹中的所有文件
for file_name in os.listdir():
    # 判断文件是否为图片，此处以 .jpg 文件为例
    if file_name.endswith('.jpg'):
        # 使用 shutil.move 函数将文件移动到目标文件夹中
        shutil.move(file_name, 'D:\\pycharm_python_project\\yolo3-pytorch-bilibili-1\\VOCdevkit\\VOC2007\\JPEGImages')
        print(file_name,"ok")