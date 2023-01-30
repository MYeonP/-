# 입력을 받습니다
string = input("입력> ")

# 출력합니다
print("입력 + 100: ", string + 100)

"""

입력> 300
Traceback (most recent call last):
  File "c:\study\자습\input_error.py", line 5, in <module>
    print("입력 + 100: ", string + 100)

TypeError: can only concatenate str (not "int") to str
-> 300과 100을 더하려고 했으나 input() 함수로 입력받은 자료는 모두 문자열로 저장된다.
따라서 "300" + 100이 되어 문자열 + 숫자는 더할 수가 없어서 발생한 오류!
 

"""