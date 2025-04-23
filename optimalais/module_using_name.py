def speak():
    if __name__ == '__main__':
        print('This program is being run by itself')
    else:
        print('I am being imported from another module')

if __name__ == '__main__':
    speak()