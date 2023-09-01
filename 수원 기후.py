import matplotlib.pyplot as plt
a= open ("수원 기후.csv","r")
lines= a.readlines()
#print(lines) 
b=(input("조회할 기간이 하루인지 여러기간인지 선택해주세요."))

if b=='하루':
    c=(input("조회할 기간을 선택해주세요. Ex) 2023-07-14"))
    d=(input("하루 평균 기온, 최고온도. 최저온도 중 확인하고 싶은 것을 선택해주세요."))

    if d=="하루 평균 기온":
        for i in lines:
            if c in i:
                print(i[15:19])

    if d=="최저온도":
        for i in lines:
            if c in i:
                print(i[20:24])

    if d=="최고온도":
        for i in lines:
            if c in i:
                print(i[25:29])


if b=="여러기간":
    e=(input("조회할 여러기간 중 시작 할 날짜를 작성해주세요. Ex) 2023-07-14"))
    f=(input("조회할 여러기간 중 끝 할 날짜를 작성해주세요. Ex) 2023-07-18"))
    d=(input("평균 기온, 평균 최고온도. 평균 최저온도 중 확인하고 싶은 것을 선택해주세요."))


    if d=="평균 기온":
        list = []
        list2= []
        for i in lines:
            if i[0:10]>=e and i[0:10] <=f:
                 list.append(float(i[15:19]))
                 list2.append(i[0:10])
        plt.plot(list2,list)
        plt.show()

        #print('평균', sum(list)/len(list))  

    if d=="평균 최저온도":
        for i in lines:
             if c in i:
                print(i[20:24])

    if d=="평균 최고온도":
        for i in lines:
            if c in i:
                print(i[25:29])

    
