from pathlib import Path

path = Path('Task_2/cats_file.txt')

def get_cats_info(path: list) -> list[dict]:

    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cats_list.append({'id': id, 'name': name, 'age': age})

    except FileNotFoundError:
        return "File not found"

    except Exception as e:
        print(f'{e} with file')

    return cats_list


print(get_cats_info('Task_2/cats_file.txt'))
