items={"커피":7, "펜":5, "사탕":10}
a=input("판매할 물건을 입력하세요.")
b=int(input("판매한 물건의 갯수를 입력하시오."))
items[a]-=b
print(items)
