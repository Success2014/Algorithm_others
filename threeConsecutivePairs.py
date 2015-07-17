# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:31:03 2015

http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=137485&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311
刚做完Zenefits OA。题目是找打牌的时候的炸弹：），瞬间想到斗地主~~~

实际就是找array里面more than 3 consecutive pairs, if exist return true, 
otherwise return false.


假设输入是sorted array. 
否则hash table需要清0.比如[1,1,2,2,1,2,2,2,3,3,4,4]
idea:
hashmap，key是array中的数，value记录到这个数的最长连续pair的数量

@author: Neo
"""

def findTP(nums):
    if not nums:
        return False
    n = len(nums)
    if n < 6:
        return False
    d = {}
    curt = None
    count = 0
    for i in xrange(n):
        if nums[i] == curt:
            count += 1
        else:
            curt = nums[i]
            count = 1
        
        if count >= 2:
            if len(d) == 0:
                d[curt] = 1
            else:
                d[curt] = d[curt-1] + 1
                if d[curt] == 3:
                    return True
    return False
    




nums = [1,1,2,2,2,3,3,4]    
print findTP(nums)    
    