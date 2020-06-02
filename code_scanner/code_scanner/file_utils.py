import os


def find_all_py_in_curr():
    print(os.getcwd())
    find_all_with_extension(os.getcwd(), '.py')


def find_all_with_extension(folder, ext):
    for file in os.listdir(folder):
        if file.endswith(ext):
            print(os.path.join(folder, file))
