list_of_targets = [int(num) for num in input().split(" ")]
counter = 0
old_value = 0

command = input()
while not command == "End":
    target = int(command)

    if target in range(len(list_of_targets)):
        old_value = list_of_targets[target]
        list_of_targets[target] = -1
        for shot in range(len(list_of_targets)):
            if list_of_targets[shot] > old_value and not list_of_targets[shot] == -1:
                list_of_targets[shot] -= old_value
            elif list_of_targets[shot] <= old_value and list_of_targets[shot] != -1:
                list_of_targets[shot] += old_value

        counter += 1

    command = input()

if command == "End":
    list_of_targets = [str(el) for el in list_of_targets]
    list_of_targets = " ".join(list_of_targets)
    print(f'Shot targets: {counter} -> {list_of_targets}')















#
#     for index in range(len(list_of_targets)):
#         if index == target:
#             if index not in shot_targets:
#                 for i in range(len(list_of_targets)):
#                     if list_of_targets[i] > list_of_targets[index] and i not in shot_targets:
#                         list_of_targets[i] -= list_of_targets[index]
#                     elif list_of_targets[i] <= list_of_targets[index] and i not in shot_targets:
#                         list_of_targets[i] += list_of_targets[index]
#                 list_of_targets[index] = -1
#                 shot_targets.append(index)
#                 counter += 1
#
#     command = input()
#
# if command == "End":
#     print(f'Shot targets: {counter} -> {" ".join(str(list_of_targets))}')

