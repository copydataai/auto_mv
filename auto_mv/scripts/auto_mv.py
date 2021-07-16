"""Principal libraries for moving and create dirs."""
from os import listdir, path,getcwd,mkdir
from shutil import move
import click

global FINDS

@click.command()
@click.option(
        '--only', 
        type=str, 
        default='all', 
        help='Specificlly type to search: book,music,video and docs'
        )
@click.option(
        '--start', 
        type=str, 
        default='.', 
        help='Define your path to scan'
        )
@click.option(
        '--end', 
        type=str, 
        default='.', 
        help='Define you files to move.'
        )
def auto_mv(only, start, end):
    """Manage files extension for automate files."""
    type_file(only)
    main_route(start, end)

def type_file(only):
    """Define your type file to moving."""
    global FINDS
    books = ['book','.epub', '.pdf',]
    videos = ['video','.mp4', '.mpg4']
    musics = ['music','.mp3', '.m4a', '.opus']
    docs = ['docs','.docx', '.xls']
    if only == 'all':
        FINDS = books + videos + musics + docs
    elif only == 'book':
        FINDS = books
    elif only == 'video':
        FINDS = videos
    elif only == 'music':
        FINDS = musics
    elif only == 'docs':
        FINDS = docs
    else:
        FINDS = ['.' + only]


def main_route(start, end):
    """The path to scan and path to moving files"""
    if start == '.' and end == '.':
        start = getcwd()
        end = getcwd()
        _scan(start, end)
    elif start == '.' and path.isdir(end):
        start = getcwd()
        _scan(start, end)
    elif end == '.' and path.isdir(start):
        end = getcwd()
        _scan(start, end)
    else:
        click.echo('This path not exist')


def _scan(dir_start, dir_end):
    """This scan files and move files"""
    global FINDS
    files = [file for file in listdir(dir_start) for find in FINDS  if find in file]
    end_path = create_dir(dir_end)
    _move(files, dir_start, end_path)

def _move(files, dir_start, dir_end):
    """This move files """
    if files:
        for file in files:
            start = dir_start + '/' + file
            move(start, dir_end)
            click.echo(dir_end)
    else:
        print('Don\'t find files {finds}')


def create_dir(dir_end):
    """Receive exit path."""
    global FINDS
    if not path.isdir(f'{dir_end}/new_{FINDS[0]}'):
        paths = path.join(dir_end, 'new_' + FINDS[0])
        mkdir(paths)
        return paths
    option = input('You want new directory? [y/N]').lower()
    if option == 'y':
        new_dir = input('Enter name dir: ')
        return f'new_book/{new_dir}/'
    return 'new_book/'
