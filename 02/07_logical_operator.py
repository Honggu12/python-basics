# 일반적으로 피연산자(operand)는 True 또는 False 값을 가지는 연산

a = 20

# not T = F
# not F = T
print(not a <20)

# T and T = T
# T and F = F
# F and T = F
# F and F = F
print(a < 30 and a != 30)

# T or T = T
# T or F = T
# F or T = T
# F or F = F
print(a == 30 or a>30)

# 연산식에서 int 값(False -> 0, True -> 1)으로 평가된다.

print(True * False)

# 다른 타입의 객체도 bool 타입으로 형반환이 가능하다.
print(bool(10), bool(0))
print(bool(3.14), bool(0.))


# 논리식의 계산순서
print(True or 'logical')
print(True or bool('logical'))
print(False or 'logical')
print([] or 'logical')
print([] and 'logical')

def f():
    print('hello world')

