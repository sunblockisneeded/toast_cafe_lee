import random

#첫 번째 단어는 음식 이름입니다. 세글자 음식이어야 합니다.
first_list = ['토스트','떡볶이', '햄버거', '비빔밥', '샐러드', '요거트']

second_list = ['카페', '뷔페', '샐러드바', '식당']

#세 번째 단어는 위인의 이름입니다. 존경하는 사람의 이름을 추가해도 좋습니다
third_list = ['이순신', '광개토대왕', '방정환', '알렉산더', '신사임당', '세종대왕']

first = random.sample(first_list,1)[0]
second = random.sample(second_list,1)[0]
third = random.sample(third_list,1)[0]


# 출력예시 : 식당 이름: 떡볶이뷔페광개토대왕
##          저희는 스타벅스 원두를 사용합니다
print(f'식당 이름: {first}{second}{third}')
print('저희는 스타벅스 원두를 사용합니다')