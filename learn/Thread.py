# import os

# print('Process (%s) start...' % os.getpid())


# from multiprocessing import Process

# def run_proc(name):
#     print('Run child process %s (%s) ...' % (name,os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc,args=('other',))
#     print('Child Process Start...')
#     p.start()
#     p.join()
#     print('Child process end.')


# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.0' % (name,os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(3)
#     for i in range(6):
#         p.apply_async(long_time_task,args = (i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('End')


# import subprocess

# r= subprocess.call(['ping','192.168.0.51'])


# import time,threading

# def loop():
#     print('thread %s is runing...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is runing...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='hhh')
# print('thread will run..')
# t.start()
# print('thread waiting..')
# t.join()
# print('tread %s ended.' % threading.current_thread().name)


# import threading

# local_school = threading.local()

# def process_student():
#     std = local_school.student
#     print('Hello. %s in(%s)' % (std,threading.current_thread().name))

# def process_thread(name):
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target=process_thread,args=('bob',))
# t2 = threading.Thread(target=process_thread,args=('pop',))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('END')


# import re
# if re.match(r'\d{3}-\d{3,6}', '010-12345'):
#     print('ok')
# else:
#     print('error')
# s = 'a b  c'
# print(s.split(' '))
# print(re.split(r'\s+', s))

# p = '010-123456'
# m = re.match(r'^(\d{3})-(\d{3,8})$', p)
# print(m[0])
# print(m[1])
# print(m[2])

# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 预编译

import re


def is_valid_email(addr):
    if not addr:
        return False
    if re.match(r'\w+@\w+\.\w', addr):
        return True
    return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

