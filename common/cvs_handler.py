#!/usr/bin/python
# coding:utf-8

"""
@author: wupeng
@file: cvs_handler.py
@time: 2018/9/11 19:52
"""
import csv


def cvs_writer(csvfilepath, write_row, mode):
    with open(csvfilepath, mode) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(write_row)
