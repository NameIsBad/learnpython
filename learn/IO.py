# file_path = 'D:\source\\test\\python\\learn/module.py'

# f = open(file_path,'r',encoding='utf-8')
# s = f.read()
# print(s)

# try:
#     f= open(file_path,'r',encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open(file_path,'r',encoding='utf-8') as f:
#     print(f.read())

# with open(file_path,encoding='utf-8',errors='ignore') as f:
#     for s in f.readlines():
#         print(s.strip())


# from io import StringIO,BytesIO
# f = StringIO()
# f.write('hello')
# print(f.getvalue())

# f = StringIO('hello')
# f.write('word')
# print(f.getvalue())

# b = BytesIO()
# b.write('中文'.encode('utf-8'))
# print(b.getvalue())

# b1= BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(b1.read())

import os

# print(os.name,os.path,os.environ,os.pathsep,os.chdir,os.system,os.getcwd,sep='\n\n')
# print(os.environ)
# print(os.environ.get('path'))
# print(os.environ.get('nnn','default')) ##不存在默认返回None

# print(os.path.abspath('.'))
# print(os.path.join('/','test.py'))

# dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
# print('dirs',dirs)

# files = [x for x in os.listdir('.') if os.path.isfile(x)]
# print('files',files)


# def get_all_dirs(path,data=[]):
#     dir_list = [x for x in os.listdir(path) if os.path.isdir(x)]
#     if not dir_list:
#         return data
#     data = data + dir_list
#     for d in dir_list:
#         get_all_dirs(d,data)
#     return data

# ddd = get_all_dirs('.')
# print(ddd)



# for root,dirs,files in os.walk('./'):
#     for file in files:
#         print('dirs',dirs)
#         print(os.path.join(root,file))

def get_abspath(s):
    path = '.'  # path可随指定路径不同而进行修改，在这表示当前路径
    for root, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            if s in file_name:
                print(os.path.abspath(os.path.join(root, file_name)))
get_abspath('test')
