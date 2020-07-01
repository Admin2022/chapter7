#coding=utf-8
import os
def run(**args):
    #返回当前目录下的所有文件名字
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)
