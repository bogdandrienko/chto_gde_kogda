ball = 0

question1 = 'Сколько у собаки хвостов? '
answer1 = 1

question2 = 'Сколько у кошки лап? '
answer2 = 4

question3 = 'Сколько у слона полушарий мозга? '
answer3 = 2

answer1_from_user = int(input(question1))
if answer1_from_user == answer1:
    ball = ball + 1

answer2_from_user = int(input(question2))
if answer2_from_user == answer2:
    ball = ball + 1

answer3_from_user = int(input(question3))
if answer3_from_user == answer3:
    ball = ball + 1

# input(f'игра окончена | {ball} балла(-ов)')
input('игра окончена | ' + str(ball) + "балла(-ов)")
