#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os



def binPath():
    '''启动路径'''
    binPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'bin','')
    return binPath

def configPath():
    '''配置路径'''
    configPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'')
    return configPath

def dataPath():
    '''数据路径'''
    dataPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data','')
    return dataPath

def logPath():
    '''日志路径'''
    logPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'log','')
    return logPath

def reportPath():
    '''报告路径'''
    reportPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'report','')
    return reportPath

def testCasePath():
    '''业务路径'''
    testCasePath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'src','testCase','')
    return testCasePath

def utilsPath():
    '''日志路径'''
    utilsPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'src','utils','')
    return utilsPath

def qiaokuInterfaceObject():
    '''接口对象地址'''
    interfaceObjectPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'src','testCase','interfaceObject','')
    return interfaceObjectPath

# @staticmethod
# def screenshot_path():
#     '''截图路径'''
#     screenshotPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\screenshot\\'
#     return screenshotPath
#
# @staticmethod
# def test_suit_path():
#     '''执行路径'''
#     test_suit_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\src\\test_suit\\'
#     return test_suit_path

if __name__ == '__main__':
    print(logPath())
