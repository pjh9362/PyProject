kor, eng, mat, sci = map(int, input("국어 영어 수학 과학 점수를 입력하시오 : ").split())

mean = (kor + eng + mat + sci)/4

if 0<=kor<=100 and 0<=eng<=100 and 0<=mat<=100 and 0<=sci<=100:
    if mean >= 80 :
        print('합격')
    else :
        print('불합격')
else:
    print('잘못된 점수')
