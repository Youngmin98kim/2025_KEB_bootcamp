import random
drinks = ['위스키','와인','소주','고량주']
drinks_food = ['초콜릿','치즈','삼겹살','양꼬치']

drinks.append('사케')
drinks.append('위스키')

drinks_food.append('광어회')
drinks_food.append('낙곱새')

while True:
    menu = input(f'다음 술중에 고르세요.\n 1){drinks[0]}  2){drinks[1]}  3){drinks[2]}  4){drinks[3]}  5){drinks[4]}  6)랜덤 추천  7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {drinks_food[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {drinks_food[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는 {drinks_food[2]} 입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {drinks_food[3]} 입니다')
    elif menu == '5':
        print(f'{drinks[4]}에 어울리는 안주는 {drinks_food[4]} 입니다')
    elif menu == '6':
        random_drink = random.choice(drinks)
        print(f'{random_drink}에 어울리는 안주는 {drinks_food[drinks.index(random_drink)]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break
