"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_trailing_zero(self, number: int) -> int:
        if number < 0:
            return "number cannot be negative"
        count = 0
        i = 5
        while number // i >= 1:
            count += number // i
            i *= 5
        return count


number_example1 = 7
number_example2 = -10
print("outputEx1 :", Solution().find_trailing_zero(number_example1))
print("outputEx2 :", Solution().find_trailing_zero(number_example2))
