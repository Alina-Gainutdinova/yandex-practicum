def get_together_games(games_1, games_2):
    # Напишите здесь код функции для поиска пересечений
    set(games_1).intersection(set(games_2))

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games, alisa_games)
# Напечатайте итоговый перечень игр в цикле
for game in together_games:
    print(game)