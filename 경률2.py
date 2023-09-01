Friend=['가','나','다','라','마'] 
while True :
    a=int(input('1. 친구 리스트, 2. 친구 추가, 3. 친구 삭제, 4. 이름변경, 5. 종료   ' )) 
    if a==1:
        print (Friend)
    if a==2:
        b=str(input('추가할 친구 이름을 입력해주세요.'))
        Friend.append(b)
        print (Friend)
        print ('추가가 완료되었습니다.')
    if a==3:
        c=str(input('삭제할 친구 이름을 입력해주세요.'))
        Friend.remove(c)
        print (Friend)
        print ('삭제가 완료되었습니다.')
    if a==4:
        d=str(input('변경할 친구 이름을 입력해주세요.')) 
        Friend.index(d) 
       
        e=str(input('새로 변경할 이름을 작성해주세요.'))
        Friend.insert(Friend.index(d),e)
        Friend.remove(d)
        print (Friend)
    if a==5:
        f=str(input('종료하시겠습니까? 예 아니요로만 답해주세요'))
        if f=='예':
            print ('감사합니다')
            break
        if f=='아니요':
            continue 
            
            
        




