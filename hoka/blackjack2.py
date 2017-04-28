import random
# プレイヤークラス
class player:
    def __init__(self):
        self.card = []
        self.sum = 0
    def two_card(self):
        for i in range(2):
            self.card = take(self.card)
    def req_sum(self):
            self.sum = sum(self.card)
# カードを引く
def take(a):
    k = random.randint(1,13)
    if k > 10: k = 10
    a.append(k)
    return a
# さらにカードを引くかどうか
def plus_card(p1):
    while True:
        p1.req_sum()
        print(p1.card)
        print("あなたの合計 : %d" %p1.sum)
        if p1.sum > 21: return p1
        print("まだ引きますか？")
        key = int(input("1:Yes 2:No >>> "))
        if key == 1:
            p1.card = take(p1.card)
        else:
            return p1
# player2がカードを引く（自動）
def plus_card_p2(p2):
    while True:
        p2.req_sum()
        if p2.sum < 16:
            p2.card = take(p2.card)
        else:
            return p2
# 判定
def judge(p1, p2):
    print("\nあなた : %d    あいて : %d" %(p1.sum, p2.sum))
    if p1.sum > 21:
        print("２１を越えてしまいました\nあなたの負けです......")
    elif p2.sum > 21:
        print("相手が２１を越えました\nあなたの勝ちです！！")
    elif p1.sum > p2.sum:
        print("あなたの勝ちです！！")
    else:
        print("あなたの負けです......")
    return
# 繰り返す
def loop():
    key = int(input("続けますか？　1:Yes 2:No >>> "))
    if key == 1:
        return True
    else:
        return False
# main
try:
    flag = True
    while flag:
        for i in range(30): print("=", end="")
        p1 = player(); p2 = player()
        p1.two_card(); p2.two_card()
        p1 = plus_card(p1)
        p2 = plus_card_p2(p2)
        for i in range(30): print("=", end="")
        judge(p1, p2)
        flag = loop()
except:
    print("error")
