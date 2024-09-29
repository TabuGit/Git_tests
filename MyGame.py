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


if __name__ == '__main__':
    main()
