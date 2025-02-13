#assignment
#메뉴 삭제 추가에 대응되는 코드를 추가 : 반복문, len함수, input 에서 문자열 결합
#가격을 합산해서 영수증을 발급하기 : 제품명, 단가, 수량, 소계, total prices, 부가세
 #ex. d_s_p = {"위스키":['초콜릿',50_000],,}
# d_s_p = {"위스키":['초콜릿',50_000]}
#print(d_s_p["위스키"]) #초콜릿, 오만원
#print(d_s_p["위스키"][1]) #오만원

import random

drinks = ['위스키','와인','소주','고량주']
drinks_food = ['초콜릿','치즈','삼겹살','양꼬치']
prices = [50000,30000,5000,7500]
prices_list = []
count_prices = {}
#total_prices =
def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {drinks_food[n]}입니다. 해당 메뉴의 가격은 {prices[n]}입니다.')
    prices_list.append(prices[n])

def sum_prices() :
    print(f'이제까지 총 가격은 {sum(prices_list)} 입니다.')

def receipt() :
    print(f'')

drinks.append('사케')
drinks.append('위스키')
drinks.append('데킬라')

drinks_food.append('광어회')
drinks_food.append('낙곱새')
drinks_food.append('소금')

prices.append(25000)
prices.append(35000)
prices.append(25000)

menu_list = '다음 술 중에 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i+1}){drinks[i]} '
#f'다음 술중에 고르세요.\n 1){drinks[0]}  2){drinks[1]}  3){drinks[2]}  4){drinks[3]}  5){drinks[4]}  6)랜덤 추천  7) 종료 : '
menu_list = menu_list + f'{len(drinks)+1}) 랜덤 추천 {len(drinks)+2}) 종료 : '
while True:
    menu = int(input(menu_list))
    if 1 <= menu < len(drinks): #비교연산자
        print_menu(menu-1)
    #if menu == int(i+1) :
    #    print(f'{drinks[i]}에 어울리는 안주는 {drinks_food[i]} 입니다')

    elif menu == len(drinks)+1 :
        random = random.randint(0,len(drinks)-1)
        print(f'{drinks[random]}에 어울리는 안주는 {drinks_food[random]}입니다.')
        #random_drink = random.choice(drinks)
        #print(f'{random_drink}에 어울리는 안주는 {drinks_food[drinks.index(random_drink)]} 입니다')

    elif menu == len(drinks)+2 :
       for num in count_prices :
           if num in prices_list:
               count_prices[num] += 1
           else:
               count_prices[num] =1
       print(f'{sum_prices()} 다음에 또 오세요.')
       break
