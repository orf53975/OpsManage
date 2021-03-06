#!/usr/bin/env python  
# _#_ coding:utf-8 _*_ 
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from .ansible import  *
from .assets import  *
from .cron import  *
from .deploy import  *
from .sql import  *
from .sched import  *