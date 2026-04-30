#定义一个玩家必输的函数
import sys

def play_game():
    choices = ["石头", "剪刀", "布", "退出"]
    print("===石头剪刀布游戏===")

    rounds = 0
    while True:
        #玩家输入
        player_choice = input("请出拳（石头、剪刀、布），或输入 '退出' 结束游戏：").strip()
        if player_choice == "退出":
            print('乐乐，你也就这样了吧')
            input("按回车键关闭窗口...")
            sys.exit()

        if player_choice not in choices:
            print('你瞎了吗？什么东西都输进去是吧？')
            continue

        if player_choice == '石头':
            print('你输了\n电脑叔叔出了个布，气不气？')

        elif player_choice == '剪刀':
            print('你输了\n电脑叔叔出了个石头，气不气？')

        elif player_choice == '布':
            print('你输了\n电脑叔叔出了个剪刀，气不气？')

        rounds += 1
        print("-"*30)

        if rounds % 3 == 0:
            options = ['要', '不要']
            while True:
                choice = input(f"输了{rounds}局了，要不要再选一次，弟弟？(要/不要)").strip()
                if choice not in options:
                    print("能不能看清楚一点，你输的啥玩意？")
                    continue
                if choice == '不要':
                    print("那你继续呗")
                    break
                elif choice == '要':
                    print("那你再选一次吧")
                    return

if __name__ == "__main__":
    play_game()
