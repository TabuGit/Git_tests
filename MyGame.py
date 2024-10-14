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


def hit_success(hit: int) -> int:
    success_prob = (10 - hit + 1) / 10
    ans = rd.choices((hit, 0), weights=[success_prob, 1 - success_prob])[0]
    return ans


def set_max_hp() -> int:
    print('Choose max hp of the players')
    max_hp = int(input())
    return max_hp


def turns_counter(move: int) -> int:
    turn = move % 2
    return turn


def launch_human_vs_human():
    print('Players, please type your names:')
    player_1 = input()
    player_2 = input()
    first, second = rd.sample([player_1, player_2], k=2)
    players = [first.capitalize(), second.capitalize()]
    player_hp_1 = player_hp_2 = set_max_hp()
    print('The game has started\n')
    players_hp = [player_hp_1, player_hp_2]
    move = 0
    while (all(hp > 0 for hp in players_hp)):
        print(f'{players[turns_counter(move)]}, hit the rival (choose: 1 - 9)')
        hit = int(input())
        if hit_success(hit):
            players_hp[turns_counter(move - 1)] -= hit
            print(f'You delivered {hit} damage')
        else:
            print('Miss :(')
        move += 1
        print(f'{players_hp[0]} {players[0]}, {players_hp[1]} {players[1]}')
    print(f'{players[turns_counter(move - 1)]} has won!')


def launch_human_vs_robot_rand():
    print('Player, please type your name')
    player_human = input()
    players = [player_human.capitalize(), 'Robot']
    print('The game has started\n')
    player_hp = robot_hp = set_max_hp()
    players_hp = [player_hp, robot_hp]
    move = 0
    while (all(hp > 0 for hp in players_hp)):
        print(f'{players[0]}, hit the robot (choose: 1 - 9)')
        hit = int(input())
        if hit_success(hit):
            players_hp[1] -= hit
            print(f'You delivered {hit} damage')
        else:
            print('Miss :(')
        move += 1
        if players_hp[1] > 0:
            move += 1
            robot_damage = hit_success(rd.randint(1, 9))
            players_hp[0] -= robot_damage
            print(f'{robot_damage} damage from Robot')
        else:
            break
        print(f'{players_hp[0]} {players[0]}, {players_hp[1]} {players[1]}')
    print(f'{players[turns_counter(move - 1)]} has won!')


def launch_human_vs_robot_strat():
    print('Player, please type your name')
    player_human = input()
    players = [player_human.capitalize(), 'Robot']
    print('The game has started\n')
    player_hp = robot_hp = set_max_hp()
    players_hp = [player_hp, robot_hp]
    move = 0
    while (all(hp > 0 for hp in players_hp)):
        print(f'{players[0]}, hit the robot (choose: 1 - 9)')
        hit = int(input())
        if hit_success(hit):
            players_hp[1] -= hit
            print(f'You delivered {hit} damage')
        else:
            print('Miss :(')
        move += 1
        if players_hp[1] > 0:
            move += 1
            if players_hp[0] <= 5:
                hit = rd.randint(1, players_hp[0])
            else:
                hit = rd.randint(3, 5)
            robot_damage = hit_success(hit)
            players_hp[0] -= robot_damage
            print(f'You got {robot_damage} damage from robot')
        else:
            break
        print(f'{players_hp[0]} {players[0]}, {players_hp[1]} {players[1]}')
    print(f'{players[turns_counter(move - 1)]} has won!')


if __name__ == '__main__':
    main()
