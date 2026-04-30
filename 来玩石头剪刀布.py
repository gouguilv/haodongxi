import guessfist
import guessfist_unbreakable

choices = ['愿意','不愿意']
print('===先看看你实力===')

while True:

    play_choices = input('你是否莫名其妙愿意给作者十万块（愿意/不愿意）：').strip()
    if play_choices not in choices:
        print('看清楚再输进去哦')
        continue

    if play_choices == '愿意':
        print('小伙子，作者叔叔很看好你哦\n玩去吧')
        guessfist.play_game()
        break

    elif play_choices == '不愿意':
        print('作者叔叔很生气\n你完了')
        guessfist_unbreakable.play_game()

