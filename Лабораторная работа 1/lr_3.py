list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
# Общее количество игроков
total_players = len(list_players)

# индекс середины
middle_index = len(list_players) // 2
# Списки команд
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]
# Печать команд
print(first_team)
print(second_team)
