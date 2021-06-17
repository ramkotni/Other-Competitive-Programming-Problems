# -*- coding: utf-8 -*-
"""Leetcode Problem 34 - Find First and Last Position of Element in Sorted Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-3Kqw8UQqKTzfVBRcKYrLml7ZRAq3kGX

Problem Statement : Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startPosition = -1    
        endPosition = -1    
        
        if (nums == None or len(nums) == 0):
            return [startPosition, endPosition]
        ## To calculate the starting position in an array
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
            if nums[mid] == target:
                startPosition = mid
      
        ## To calculate the ending position of an array    
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            if nums[mid] == target:
                endPosition = mid
                
        return [startPosition, endPosition]