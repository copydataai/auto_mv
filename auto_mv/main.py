from os import listdir, path
from shutil import move

def main():
    download = path.expanduser('~') + '/Downloads'

    books = ['.epub', '.pdf', ]

    documents = path.expanduser('~') + '/Documents/new_books'

    files = [file for file in listdir(download) for book in books if book in file]
    if files:
        for file in files:
            start = download + '/' + file
            end = documents
            move(start,end)
        print(listdir(documents))
    else:
        print('Don\'t find files .pdf, .epub ')

    print(files)


if __name__ == '__main__':
    main()
