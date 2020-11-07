st = []
print(st)

st.append(10)
print("append(10) : ", st)

st.append(20)
print("append(20) : ", st)

st.append(30)
print("append(30) : ", st)

print(st.pop())
print("pop() : ", st)

print(st.pop())
print("pop() : ", st)

print(st.pop())
print("pop() : ", st)


######################
st = []

for i in range(4):
    st.append((i+1)*10)
    print(st)
'''
for i in range(len(st)):
    st.pop()
    print(st)
'''
'''
#오류발생!!
for i in st:
    print(st.pop())
    print(st)
'''

print("********************")
for i in st:
    st.remove(i)
    print(st)

