
from multiprocessing import Pool
from datetime import datetime



def read_info(name):
    with open(name, 'r') as file:
        all_data = []
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == '__main__':

    filenames = [f'./file_{i}.txt' for i in range(1, 5)]

    # Линейный вызов:
    start_time_linear = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time_linear = datetime.now()
    print(f"Линейное выполнение заняло: {end_time_linear - start_time_linear} секунд")

    # Мультипроцессный вызов:
    pool = Pool()
    start_time_multiprocess = datetime.now()
    results = pool.map(read_info, filenames)
    pool.close()
    pool.join()
    end_time_multiprocess = datetime.now()
    print(f"Многопроцессное выполнение заняло: {end_time_multiprocess - start_time_multiprocess} секунд")

