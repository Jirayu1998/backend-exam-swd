"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not be less than 0"

        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        roman_text = ""
        for value, symbol in roman_numerals.items():
            while number >= value:
                roman_text += symbol
                number -= value

        return roman_text


number_example1 = 101
number_example2 = -1
print("outputEx1 :", Solution().number_to_roman(number_example1))
print("outputEx2 :", Solution().number_to_roman(number_example2))
