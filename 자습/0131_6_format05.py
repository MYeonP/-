output_a = "{:f}".format(52.273)        #{:f} = float 자료형의 실수 출력
output_b = "{:15f}".format(52.273)      # 15칸 만들기
output_c = "{:+15f}".format(52.273)     # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273)    # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

"""
실행결과

52.273000
      52.273000
     +52.273000
+0000052.273000

"""