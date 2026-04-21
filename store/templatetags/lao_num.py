from django import template

register = template.Library()

@register.filter(name='num_to_lao')
def num_to_lao(value):
    try:
        if not value or value == 0: return "(ສູນກີບ)"
        
        num_dict = {
            '0': 'ສູນ', '1': 'ໜຶ່ງ', '2': 'ສອງ', '3': 'ສາມ', '4': 'ສີ່',
            '5': 'ຫ້າ', '6': 'ຫົກ', '7': 'ເຈັດ', '8': 'ແປດ', '9': 'ເກົ້າ'
        }
        # ໃຊ້ Standard Unit ຂອງລາວ: ໜ່ວຍ, ສິບ, ຮ້ອຍ, ພັນ, ໝື່ນ, ແສນ
        unit_list = ['', 'ສິບ', 'ຮ້ອຍ', 'ພັນ', 'ສິບ', 'ແສນ']
        
        num_str = str(int(float(value)))[::-1]
        result = ""
        
        for i, digit in enumerate(num_str):
            unit_idx = i % 6
            if digit != '0':
                # 1. ຫຼັກສິບ: ເລກ 1 ບໍ່ອອກສຽງ, ເລກ 2 ອອກສຽງ "ຊາວ"
                if unit_idx == 1:
                    digit_text = "ຊາວ" if digit == '2' else ("" if digit == '1' else num_dict[digit])
                    unit_text = "ສິບ"
                # 2. ຫຼັກໜ່ວຍ (ຫຼື ຫຼັກລ້ານ): ເລກ 1 ອອກສຽງ "ເອັດ" ຖ້າມີຕົວເລກທາງໜ້າ
                elif unit_idx == 0 and digit == '1' and len(num_str) > 1:
                    digit_text = "ເອັດ"
                    unit_text = "ລ້ານ" if i >= 6 else ""
                else:
                    digit_text = num_dict[digit]
                    unit_text = unit_list[unit_idx] if i < 6 else "ລ້ານ"
                
                result = digit_text + unit_text + result
            else:
                # ຖ້າເປັນເລກ 0 ແຕ່ຕົກຢູ່ຫຼັກລ້ານ ໃຫ້ຕື່ມຄຳວ່າ "ລ້ານ"
                if i > 0 and unit_idx == 0:
                    result = "ລ້ານ" + result

        return f"({result}ກີບ)"
    except:
        return ""