def main():
    from pathlib import Path
    import os

    # Operation
    pathObj1 = Path('A') / 'B'
    print(pathObj1)

    # Get current path
    pathObjNow = Path.cwd() # C:\Users\user\Kani\python\AutomateTheBoringStuffWithPython,2ndEdition\Ch9-ReadAndWriteFiles
    print(Path.cwd())
    print(os.getcwd())  # Same
    os.chdir('C:\\Users\\user\\Kani\\python')   # Change folder
    print(Path.cwd())
    print(os.getcwd())  # Same
    print(Path.home())  # C:\Users\user

    # abspath and relpath
    os.chdir(pathObjNow)
    print(os.path.abspath('.'))
    print(os.path.isabs(pathObjNow))    # True
    print(os.path.relpath(pathObjNow, 'C:\\Users\\user'))   # Kani\python\AutomateTheBoringStuffWithPython,2ndEdition\Ch9-ReadAndWriteFiles

    # Part of path
    p = Path(f'{Path.cwd().parents[0]}\\Ch7-Regex\\ex.py')  # C:\Users\user\Kani\python\AutomateTheBoringStuffWithPython,2ndEdition\Ch7-Regex\ex.py
    # Only Windows' Path object has drive attribute
    print(p.anchor, p.parent, p.name, p.stem, p.suffix, p.drive) # C:\, p - ex.py, ex.py, ex, .py, C:
    print(os.path.basename(p), os.path.dirname(p))  # ex.py, p - ex.py
    print(os.path.split(p)) # tuple(dirname, basename)
    '''
    In commandline mode:
    p.split(os.sep) -> Windows: dict of part of path
    p.split(os.path.sep) -> MacOS, Linux: first member in dict is None, same as Windows' at last
    '''

    # Get size and content of file
    print(os.path.getsize(pathObjNow.parents[0]))   # 4096
    print(os.listdir(pathObjNow.parents[0]))    # Ch1-9
    # Glob mode
    print(list(Path(f'{Path.cwd().parents[0]}\\Ch8-InputValidation').glob('*.py'))) # Generator used for once

    # Legal or not
    print(p.is_dir(), p.is_file(), p.exists())  # False True True

    # Read and Write
    f = Path.cwd() / 'test.txt'
    print(f.write_text('Hello'))    # 5(chr), no need for specify encoding
    print(f.read_text())    # Hello
    fOpen1 = open(f, 'r')    # default='r'
    print(fOpen1.read()) # Hello
    fOpen1.close()
    fOpen2 = open(f, 'a')
    fOpen2.write('Hi')  # Append 'Hi' before 'Hello'
    fOpen2.close()
    fOpen1 = open(f, 'r')
    print(fOpen1.read())    # HelloHi
    fOpen1.close()

    # Save variable into file with shelve
    import shelve
    os.chdir(Path.cwd() / 'test2')  # Set current path
    shelfFile = shelve.open('test2.txt')
    cats = ['cat1', 'cst2', 'cat3']
    shelfFile['cats'] = cats
    shelfFile.close()
    shelfFile = shelve.open('test2.txt')
    print(shelfFile['cats'])    # ['cat1', 'cst2', 'cat3']
    shelfFile.close()
    os.chdir(pathObjNow)    # Reset the current path
    # Save with pprint
    import pprint
    fileObj = open('test3.txt', 'w')
    fileObj.write('cats = ' + pprint.pformat(cats) + '\n')  # Writeback a list by pprint
    fileObj.close()
    fileObj = open('test3.txt', 'r')
    print(fileObj.read())   # cats = ['cat1', 'cst2', 'cat3']
    fileObj.close()

if __name__ == '__main__':
    main()
