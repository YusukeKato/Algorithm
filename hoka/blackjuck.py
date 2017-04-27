import random
# 引く処理
def draw(a):
    k = random.randint(1,13)
    if k > 10:
        k = 10
    a.append(k)
    return a
# ゲーム本体
def blackjack():
    user = []; com = []
    count = 0
    while True:
        if count < 2:
            user = draw(user)
            com = draw(com)
            count += 1
        else:
            usum = 0; csum = 0
            print("あなた　: ", end="")
            for i in range(len(user)):
                if i == 0:
                    print(" * ", end="")
                else:
                    print(" " + str(user[i]), end="")
                usum += user[i]
            user2 = int(input("\n\n まだ引く？ 1:Yes 2:No >>> "))
            if user2 == 1:
                user = draw(user)
            else:
                for i in range(len(com)): csum += com[i]
                while True:
                    if csum > 15:
                        break
                    else:
                        k = random.randint(1,13)
                        if k > 10:
                            k = 10
                        com.append(k)
                        csum += k
                return user, com, usum, csum
# 判定
def judge(user, com, usum, csum):
    print("================================================================")
    if 1 in user:
        print("あなたの合計 : " + str(usum) + "\nコンピュータの合計 : " + str(csum))
        a = int(input("エースを１１として使う？ 1:Yes 2:No >>> "))
        if a == 1:
            usum += 10
    print("あなたの合計 : " + str(usum) + "\nコンピュータの合計 : " + str(csum))
    if usum > 21:
        print("２１を越えてしまった。あなたの負け......")
    elif csum > 21:
        print("コンピュータが２１を越えた。あなたの勝ち！！")
    elif usum > csum:
        print("あなたの勝ち！！")
    else:
        print("あなたの負け......")
    return
# main
try:
    while True:
        user,com,usum,csum = blackjack()
        judge(user, com, usum, csum)
        play = int(input('\n続けますか？ 1:Yes 2:No >>> '))
        if play == 2:
            break
except:
    print("error")
