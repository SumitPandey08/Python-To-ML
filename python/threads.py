import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.4)
        print(letter)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Both threads have completed execution")

#here both thread is working at same time

# but there is a issue regarding race between both threads so we ue lock for safty measure

import threading
import time

lock = threading.Lock()

def print_numbers():
    for i in range(5):
        time.sleep(1)
        with lock :
         print(i)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.4)
        with lock :
         print(letter)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Both threads have completed execution")