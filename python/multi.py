import concurrent.futures

def func1():
    while True:
        print("func1")

def func2():
    while True:
        print("func2")


if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    executor.submit(func1)
    executor.submit(func2)