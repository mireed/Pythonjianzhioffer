# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0])
        if rows > 0 and cols > 0:
        	row = 0
        	col = cols - 1
        	while row < rows and col >= 0:
        		if target == array[row][col]:
        			return True
        		elif target > array[row][col]:
        			row += 1
        		else:
        			col -= 1
        return False