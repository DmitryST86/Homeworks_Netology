import os


def create_all_in_one(directory):
    files = os.listdir(directory)
    files_list = []

    for file in files:
        with open(directory + "/" + file, encoding='utf-8') as current:
            if file[-4:] == '.txt' and file != 'all_in_1.txt':
                i = 4
                number_file = file[i]
                files_list.append([file, 0, [], number_file])
                for string in current:
                    files_list[-1][2].append(string.strip())
                    files_list[-1][1] += 1


    return sorted(files_list, key=lambda x: x[2], reverse=True)


def create_sorted_all_in_one_by_netology_rules(directory, name_file):
    count = 0
    with open(name_file + '.txt', 'w+', encoding='utf-8') as f:
        for file in create_all_in_one(directory):
            count += 1

            f.write(f'{file[0]}\n')
            f.write(f'{count}\n')
            for string in range(1, len(file[2])+1):
                f.write(f'Строка номер {string} файла номер {file[3]}\n')
            f.write('-------------------\n')


print(create_sorted_all_in_one_by_netology_rules(r'C:\Users\stadn\PycharmProjects\pythonProject\text_folder', 'all_in_1'))

