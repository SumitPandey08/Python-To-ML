import multiprocessing
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.5)
        print(letter)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()

    print("Both processes have completed execution")


# after seeing output who can see both function started runing and take their time to complete and then it give the output
 