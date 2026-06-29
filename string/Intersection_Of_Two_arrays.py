class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_intersections = set()
        nums2_set = set(nums2)
        for num in nums1:
            if num in nums2_set:
                unique_intersections.add(i)
        return list(unique_intersections)