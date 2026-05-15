# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # Base case: A single element is already sorted
        if len(pairs) <= 1:
            return pairs

        # Find the middle point
        m = len(pairs) // 2

        # Recursively sort both halves
        sorted_pairs1 = self.mergeSort(pairs[0:m])
        sorted_pairs2 = self.mergeSort(pairs[m:])

        # Merge the two sorted halves
        merged_arr = self.merge(sorted_pairs1, sorted_pairs2)
        return merged_arr

    def merge(self, sorted_arr1: List[Pair], sorted_arr2: List[Pair]) -> List[Pair]:
        ptr1 = 0
        ptr2 = 0
        merged_arr = []

        # Merge the arrays while there are elements in both
        while ptr1 < len(sorted_arr1) and ptr2 < len(sorted_arr2):
            if sorted_arr1[ptr1].key <= sorted_arr2[ptr2].key:  # Change to `<=` for ascending order
                merged_arr.append(sorted_arr1[ptr1])
                ptr1 += 1
            else:
                merged_arr.append(sorted_arr2[ptr2])
                ptr2 += 1

        # Only extend with the remaining elements from either array
        if ptr1 < len(sorted_arr1):
            merged_arr.extend(sorted_arr1[ptr1:])
        else:
            merged_arr.extend(sorted_arr2[ptr2:])

        return merged_arr