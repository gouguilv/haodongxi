import random


def get_winner(player, computer):
    """
    判断胜负
    :param player: 玩家手势（字符串）
    :param computer: 电脑手势（字符串）
    :return: 结果字符串
    """
    if player == computer:
        return "平局！"
    elif (player == "石头" and computer == "剪刀") or \
            (player == "剪刀" and computer == "布") or \
            (player == "布" and computer == "石头"):
        return "你赢了！"
    else:
        return "电脑赢了。"


def play_game():
    """
    主游戏函数
    """
    choices = ["石头", "剪刀", "布"]
    print("===== 石头剪刀布游戏 =====")

    while True:
        # 玩家输入
        player_choice = input("请出拳（石头、剪刀、布），或输入 '退出' 结束游戏：").strip()

        if player_choice == "退出":
            print("感谢游玩，再见！")
            break

        if player_choice not in choices:
            print("输错啦，宝宝，看清楚再重新输入（石头、剪刀、布）。")
            continue

        # 电脑随机选择
        computer_choice = random.choice(choices)
        print(f"电脑出了：{computer_choice}")

        # 判定胜负
        result = get_winner(player_choice, computer_choice)
        print(result)
        print("-" * 30)


if __name__ == "__main__":
    play_game()