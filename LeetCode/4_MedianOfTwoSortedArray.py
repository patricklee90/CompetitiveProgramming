'''
Question Link: https://leetcode.com/problems/median-of-two-sorted-arrays/ 

Solution Explanation: https://www.interviewbit.com/blog/median-of-two-sorted-arrays/
'''

class Solution(object):

    def findMedianSortedArraysBF(self, nums1, nums2):
        i = 0
        j = 0
        m1, m2 = -1, -1
        n = len(nums1)
        m = len(nums2)
        print(f"n+m/2 {(n+m)//2}")

        if((m+n)%2 == 1):
            return "odd"
        else:
            print("even")
            for count in range(((n+m)//2)+1):
                m2 = m1
                if(i != n and j!= m):
                    if nums1[i] > nums2[j]:
                        m1=nums2[j]
                        j+=1
                    else:
                        m1 = nums1[i]
                        i+=1
                elif(i<n):
                    m1 = nums1[i]
                    i += 1
                
                # for case when j<m,
                else:
                    m1 = nums2[j]
                    j += 1
            print(m1+m2)
            return (m1+m2)/2

    # Merge Sort
    def findMedianSortedArraysMS(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        m1, m2 = -1, -1

        if((m+n)%2 == 1):
            for count in range(((n+m)//2)+1):
                if(i!=n and j!=m):
                    if nums1[i] > nums2[j]:
                        m1 = nums2[j]
                        j += 1
                    else:
                        m1 = nums1[i]
                        i += 1
                elif(i < n):
                    m1 = nums1[i]
                    i += 1
                # for case when j < m
                else:
                    m1 = nums2[j]
                    j += 1
                
            return m1
        
        else:
            for count in range(((n+m)//2)+1):
                m2 = m1
                if(i != n and j!= m):
                    if nums1[i] > nums2[j]:
                        m1=nums2[j]
                        j+=1
                    else:
                        m1 = nums1[i]
                        i+=1
                elif(i<n):
                    m1 = nums1[i]
                    i += 1
                
                # for case when j<m,
                else:
                    m1 = nums2[j]
                    j += 1
            print(m1+m2)
            return (m1+m2)/2

num1 = [1,2]
num2 = [3,4]

solution = Solution()

print(solution.findMedianSortedArraysMS(num1,num2))