# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 11:04
# @Author  : Tony Yu
# @Author URI: https://www.diandian100.cn
import os

def batch_up_files(path, old, new, suffix='.html'):
    """
    批量替换文件内容
    :param path: 文件所在的路径
    :param old: 要替换的字符串
    :param new: 替换后的字符串
    :param suffix: 要替换的文件后缀
    :return:
    """
    # 所有要修改的文件路径列表
    files = []
    # 循环根目录下的所有文件夹，输出文件夹路径, 文件夹名字, 文件名
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            # 只操作用户传进来的后缀文件
            if file.endswith(suffix):
                # 将要操作的文件路径添加至列表
                files.append(os.path.join(dirpath, file))

    # 开始循环操作列表中的文件
    for file in files:
        with open(str(file), 'r', encoding="utf8", errors='ignore') as f:
            # 读取文件内容
            contents = f.read()
            # 判断要替换的字符串是否在当前文件中，在就处理
            if old in contents:
                # 文件读取指针移动到开头
                f.seek(0)
                # 替换内容
                contents = contents.replace(old, new)
        # 再次打开该文件，将新内容写入
        with open(str(file), 'w', encoding="utf8", errors='ignore') as f:
            f.write(contents)
        print(file, '已修改完毕……')

if __name__ == '__main__':
    s ="<script src=\"https://my.openwrite.cn/js/readmore.js\" type=\"text/javascript\"></script><script>const btw = new BTWPlugin();btw.init({id: 'main', blogId: '123456789', name: 'tonyu', qrcode: '公众号地址', keyword: '验证码',});</script>"
    batch_up_files('./', s, '')