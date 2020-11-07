'''
def A():
    x = 10              # A의 지역 변수 x
    def B():
        nonlocal x      # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20          # A의 지역 변수 x에 20 할당
    B()
    print(x)            # A의 지역 변수 x 출력

A()
'''

'''
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 1000
            y = y + 1000
            print(x)
            print(y)
        C()
    B()
A()
'''

x = 1
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()
A()
