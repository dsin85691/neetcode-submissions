class Solution:
    def addBinary(self, a: str, b: str) -> str:
        new_b = [] 
        a_r, b_r = len(a) - 1, len(b) - 1
        carry_b = 0
        # Binary ops (add)
        while a_r >= 0 or b_r >= 0 or carry_b:
            a_c = int(a[a_r]) if a_r >= 0 else 0
            b_c = int(b[b_r]) if b_r >= 0 else 0
            val = a_c + b_c + carry_b
            new_b.append(str(val % 2))
            carry_b = val // 2
            a_r -= 1
            b_r -= 1
        return "".join(new_b)[::-1]
