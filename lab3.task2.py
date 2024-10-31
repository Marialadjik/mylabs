def find_common_participants(group_1, group_2, delit=','): # TODO Напишите функцию find_common_participants
    common_participants = list(set(group_1.split(delit)).intersection(group_2.split(delit)))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common)# TODO Провеьте работу функции с разделителем отличным от запятой
