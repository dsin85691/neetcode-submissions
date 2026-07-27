class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_func = lambda y: abs(x - y)
        a, b = 0, len(arr) - 1 
        # Time Comp: O(n), O(1) space
        while b - a + 1 > k: 
            # We compare the distance of the elements at the edges
            # If the left element is further from x than the right element,
            # or if they are equal but the left is larger (not possible in sorted),
            # we remove the left element.
            if abs_func(arr[a]) > abs_func(arr[b]):
                a += 1
            else:
                # If the right is further OR distance is equal,
                # we remove the right element because we prefer smaller numbers.
                b -= 1
        return arr[a:b+1]