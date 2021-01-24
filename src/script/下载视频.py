import os
import requests

"""
下载M3U8文件里的所有片段
"""

url : str = ''

file_name : str  = ''

# 本地存储地址（最终生成文件地址）
download_dir : str  = ''

# ts文件夹地址
ts_dir : str  = os.path.join(download_dir, file_name, '_ts')

def check_download_dir(download_dir):
    # 校验本地存储文件夹 - 不存在则用默认下载地址
    if not os.path.isdir(download_dir):
        download_dir = os.path.join(os.getcwd(), 'download')
        # 默认文件夹如果未创建，则创建默认文件夹
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        print('不存在的文件夹，默认下载%s'%download_dir)

def check_m3u8(response_content):
    # 读取文件里的每一行，切割成list
    file_line : list = response_content.split("\n")
    if file_line[0] != "#EXTM3U":
        print('非M3U8的链接')
        raise BaseException(u"非M3U8的链接")

def download(url):
    download_path = os.getcwd() + "/download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
        unknow = True  # 用来判断是否找到了下载的地址
        for index, line in enumerate(file_line):
            if "EXTINF" in line:
                unknow = False
                # 拼出ts片段的URL
                pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]
                print(pd_url)
                res = requests.get(pd_url)
                c_fule_name = str(file_line[index + 1])
                print('开始下载')
                with open(download_path + "/" + c_fule_name, 'ab') as f:
                    f.write(res.content)
                    f.flush()
        if unknow:
            raise BaseException("未找到对应的下载链接")
        else:
            print("下载完成")


if __name__ == '__main__':
    download("https://videomy.yongaomy.com/20200111/MIDE-095/1500kb/hls/index.m3u8")