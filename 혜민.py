for i in range(5):
    password = input("비밀번호를 입력해주세요  ")
    if password == "경률1234":
        print("로그인성공")
        break
    else :
        print("다시입력해주세요")

if i == 4 :
    print("5번 초과. 비밀번호 새로 설정해주세요")
