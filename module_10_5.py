import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.datetime.now()
    print(f'{end - start} (Линейный вызов)')

    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (Многопроцессорный вызов)')

