#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
# -*- encoding: utf-8 -*-
'''
@File    :   26.删除排序数组中的重复项.py
@Time    :   2019/09/17 16:36:58
@Author  :   Leung
@Version :   3.6.x
@Contact :   aa269440877@outlook.com
@WebSite :   https://github.com/ld269440877/
'''

import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# here put the import lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow = 0
            for fast in range(1,len(nums)):
                slow += 1
                nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0

