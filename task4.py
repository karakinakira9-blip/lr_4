import task1
import task2
import task3

import time


if __name__ == "__main__":

    start_time = time.time()
    for i in range(100):
        binary_object = task1.toml_parser('task1.toml')
        task1.serializer(binary_object)
    time1 = time.time() - start_time

    start_time = time.time()
    for i in range(100):
        binary_object = task2.toml_parser('task1.toml')
        task2.xml_serializer(binary_object)
    time2 = time.time() - start_time

    start_time = time.time()
    for i in range(100):
        binary_object = task3.toml_parser('task1.toml')
        task3.serializer(binary_object)
    time3 = time.time() - start_time

    print(time1,"\n",time2,"\n",time3)
