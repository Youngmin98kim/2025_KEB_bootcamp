# import random
#
# # numbers = list()
# # for i in range(5):
# #     numbers.append(random.randint(1, 100))
# numbers = [random.randint(1, 100) for i in range(10)]
# print(numbers)
#
# try:
#     pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
#     print(numbers[pick])
#     print(5/0)
# except IndexError as err: #index 숫자 입력
#     print(f"Wrong index number\n{err}")
# except ValueError as err: #숫자 입력하도록
#     print(f"Input Only Number~\n{err}")
# except ZeroDivisionError as err:
#     print(f"The denominator cannot be 0.\n{err}")
# except Exception as err: #예외처리 중 최상위 class
#     print(f"Error occurs : {err}")

import random


class OopsException(Exception):
    pass

# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    print(5/2)
    raise OopsException("Oops~~")  # exception! class의 생성자를 사용
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as err:
    print(f"Input only number~\n{err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
# except OopsException as err:
#     print(f"Oops Oops {err}")
except Exception as err:
    print(f"Error occurs : {err}")
else:
    print(f"Program terminate")