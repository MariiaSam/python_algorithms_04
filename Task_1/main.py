from pathlib import Path


path = Path('Task_1/salary_file.txt')


def total_salary(path: str) -> str:

    total = 0
    number_of_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                number_of_developers += 1

    except FileNotFoundError:
        return "File not found"

    except Exception as e:
        print(f'{e} with file')

    if  number_of_developers > 0:
        average = total // number_of_developers
        return f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}'
    else:
        print('У файлі відсутня інформація стосовно заробітної плати розробників ')


print(total_salary('Task_1/salary_file.txt'))