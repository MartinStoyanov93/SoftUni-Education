string_of_numbers = input().split(", ")
even_list = []

print([i for i in range(len(string_of_numbers)) if int(string_of_numbers[i]) % 2 == 0])


# for i in range(len(string_of_numbers)):
#     if int(string_of_numbers[i]) % 2 == 0:
#         even_list.append(i)
# print(even_list)
