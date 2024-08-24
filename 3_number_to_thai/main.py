"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"

        thai_numbers = {
            0: "ศูนย์",
            1: "หนึ่ง",
            2: "สอง",
            3: "สาม",
            4: "สี่",
            5: "ห้า",
            6: "หก",
            7: "เจ็ด",
            8: "แปด",
            9: "เก้า",
            10: "สิบ",
            100: "ร้อย",
            1000: "พัน",
            10000: "หมื่น",
            100000: "แสน",
            1000000: "ล้าน",
        }

        num_text = ""
        if number == 0:
            num_text = thai_numbers[0]
        else:
            digits = []
            while number > 0:
                digits.append(number % 10)
                number //= 10

            digits.reverse()
            num_digits = len(digits)

            for i, digit in enumerate(digits):
                position = num_digits - i
                if digit == 1 and position % 6 == 1 and i != 0:
                    num_text += "เอ็ด"
                elif digit == 2 and position % 6 == 2:
                    num_text += "ยี่" + thai_numbers[10]
                elif digit == 1 and position % 6 == 2:
                    num_text += thai_numbers[10]
                elif digit != 0:
                    num_text += thai_numbers[digit]
                    if position % 6 == 2:
                        num_text += thai_numbers[10]

                if digit != 0 or position == 7:
                    if position % 6 == 3:
                        num_text += thai_numbers[100]
                    elif position % 6 == 4:
                        num_text += thai_numbers[1000]
                    elif position % 6 == 5:
                        num_text += thai_numbers[10000]
                    elif position % 6 == 0:
                        num_text += thai_numbers[100000]
                    elif position == 7:
                        num_text += thai_numbers[1000000]

        return num_text.strip()


number_example1 = 101
number_example2 = -1
print("outputEx1 :", Solution().number_to_thai(number_example1))
print("outputEx2 :", Solution().number_to_thai(number_example2))
