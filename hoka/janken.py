import random
dic = {0:"グー", 1:"パー", 2:"チョキ"}
while True:
    print("\n！！じゃんけん！！\n")
    print("0:グー 1:パー 2:チョキ")
    user = int(input('入力 >>>'))
    if not(user == 0 or user == 1 or user == 2): break
    com = random.randint(0,2)
    print("あなた : " + dic[user] + " コンピュータ : " + dic[com])
    judge = (user - com + 3) % 3
    if judge == 0:
        print("あいこ")
    elif judge == 1:
        print("あなたの勝ち！！")
    else:
        print("あなたの負け......")
