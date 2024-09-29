import random as rd


def main():
    print('Hi, select the configuration of the game')
    print('1 - Human vs Human')
    print('2 - Human vs Robot (random)')
    print('3 - Human vs Robot (strategy)')
    mode = int(input())
    if mode == 1:
        launch_human_vs_human()
    elif mode == 2:
        launch_human_vs_robot_rand()
    elif mode == 3:
        launch_human_vs_robot_strat()


def hit_success(hit: int) -> bool:
    success_prob = (10 - hit + 1) / 10
    ans = rd.choices((True, False), weights=[success_prob, 1 - success_prob])
    return ans[0]


def launch_human_vs_human():
    print('Player 1, please type your name:')
    player_1 = input()
    print('Player 2, please type your name:')
    player_2 = input()
    first, second = rd.sample([player_1, player_2], k=2)
    print('The game has started\n')
    players = [first.capitalize(), second.capitalize()]
    move_ct = 0
    hp = [20, 20]
    while (hp[0] > 0) and (hp[1] > 0):
        print(f'{players[move_ct % 2]}, hit the rival (choose: 1 - 9)')
        hit = int(input())
        if hit_success(hit):
            hp[(move_ct + 1) % 2] -= hit
            print(f'You delivered {hit} damage')
        else:
            print('Miss :(')
        print(players[0], hp[0])
        print(players[1], hp[1])
        move_ct += 1
    print(f'{players[(move_ct + 1) % 2]} has won!')


if __name__ == '__main__':
    main()
