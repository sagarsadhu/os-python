import time

nemo = ['nemo']
others = ['dory', 'bruce', 'marlin', 'nemo', 'gil' 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo' for i in range(100000)]


def find_nemo(list_1):
    start_time = time.time()
    for item in list_1:
        if item == 'nemo':
            print('Found NEMO!')
    end_time = time.time()
    print(f'Call to find Nemo took {end_time - start_time} milliseconds')


find_nemo(large)
