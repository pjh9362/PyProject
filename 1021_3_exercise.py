Kor, Eng, Mat, Sci = map(int, input("국어, 영어, 수학, 과학 점수를 입력하시오 : ").split())

total = Kor + Eng + Mat + Sci

print(Kor, Eng, Mat, Sci, sep="+")

print("총합은", total, "입니다")
