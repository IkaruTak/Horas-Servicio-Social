import os

def found(target):
    initial_dir = '/home/'

    path = ''
    for root, _, files in os.walk(initial_dir):
        if target in files:
           path = os.path.join(root, target)
           break

    return path
