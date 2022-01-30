import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return(f'Done Sleeping {seconds}...')

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        print(f1.result())
        print(f2.result())
    

if __name__ == '__main__':
    main()

