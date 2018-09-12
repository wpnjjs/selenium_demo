#!/usr/bin/python
# coding:utf-8

"""
@author: wupeng
@file: preview.py
@time: 2018/9/11 16:33
"""
from unittest import TestCase, main
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import win32com.client
import time


class Test_preview(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.layui.com/demo/')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_add(self):
        self.driver.switch_to.frame('LAY_demo')
        self.driver.find_element_by_css_selector('.layui-table-tool-temp > div:nth-child(1)').click()

    def test_choice_column(self):
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector('#LAY_demo'))
        self.driver.find_element_by_css_selector('.layui-table-tool-self > div:nth-child(1)').click()
        self.driver.find_element_by_css_selector(
            '.layui-table-tool-panel > li:nth-child(1) > div:nth-child(2) > i:nth-child(2)').click()
        classvalue = self.driver.find_element_by_css_selector(
            'div.layui-table-fixed:nth-child(3) > div:nth-child(1) > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2)').get_attribute(
            'class')
        assert 'layui-hide' in classvalue
        self.driver.find_element_by_css_selector(
            '.layui-table-tool-panel > li:nth-child(1) > div:nth-child(2) > i:nth-child(2)').click()
        classvalue = self.driver.find_element_by_css_selector(
            'div.layui-table-fixed:nth-child(3) > div:nth-child(1) > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2)').get_attribute(
            'class')
        assert 'layui-hide' not in classvalue

    def test_export(self):
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector('#LAY_demo'))
        self.driver.find_element_by_css_selector('.layui-table-tool-self > div:nth-child(2)').click()
        self.driver.find_element_by_css_selector('.layui-table-tool-panel > li:nth-child(1)').click()
        time.sleep(10)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('~', 0)

    def test_del(self):
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector('#LAY_demo'))
        self.driver.find_element_by_css_selector(
            'div.layui-table-fixed:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > a:nth-child(3)').click()
        time.sleep(3)
        assert u'真的删除行么' == self.driver.find_element_by_css_selector('.layui-layer-content').text
        self.driver.find_element_by_css_selector('.layui-layer-btn0').click()
        assert '10000' != self.driver.find_element_by_css_selector(
            'div.layui-table-fixed:nth-child(3) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1)').text

    def test_dropandmoveto(self):
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector('#LAY_demo'))
        self.driver.find_element_by_css_selector(
            'div.layui-table-fixed:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(1) > div:nth-child(1) > a:nth-child(3)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.layui-layer-btn0').click()
        try:
            text = self.driver.find_element_by_css_selector(
                'div.layui-table-fixed:nth-child(3) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(2) > div:nth-child(1)').text
            print text
            assert '10009' != text
        except NoSuchElementException, e:
            print "Exception"
            print e
        Select(self.driver.find_element_by_css_selector('.layui-laypage-limits > select:nth-child(1)')).select_by_index(
            3)
        time.sleep(3)
        self.driver.find_element_by_css_selector('.layui-tab-title > li:nth-child(2)').click()
        self.driver.execute_script('window.scrollTo(0,450)')
        time.sleep(3)

    def test_backtodefaultcontext(self):
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector('#LAY_demo'))
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(
            'li.layui-nav-itemed:nth-child(3) > dl:nth-child(2) > dd:nth-child(2) > a:nth-child(1)').click()
        time.sleep(1.5)
        self.driver.find_element_by_css_selector(
            'form.layui-form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(
            u'小米')
        self.driver.find_element_by_css_selector(
            'form.layui-form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector(
            'form.layui-form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys(
            '小米'.decode('utf-8'))
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    main()
