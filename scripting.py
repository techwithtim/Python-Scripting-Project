import os

print('\\t\tC:\\Home',
      os.getcwd(),
      os.path.join(os.getcwd(), 'foo', 'foo'),
      os.path.isabs('/'),
      os.path.relpath('/foo/Target', '/foo/Source'),
      os.path.exists('foo'),
      os.path.isfile('foo'),
      os.path.isdir('foo'),  sep=os.linesep)
try:
    print(os.path.getsize('scripting.py'))
    print(os.listdir('data'))
    open('foo.txt', 'w')
    print(os.unlink('foo.txt'))
    print(os.mkdir('database'))
    print(os.rmdir(os.path.join("database"))) # Do it this way
    print(os.makedirs("database\\config"))
    print(os.removedirs("database\\config"))
except (FileNotFoundError, FileExistsError) as E:
    pass
for current_folder, sub_folders, files in os.walk('data', topdown=False):
    print(f'Current folder is {current_folder}')


from pathlib import Path

print(Path.cwd())
p = Path() # No method to change path once initialised
print(p.joinpath('data', 'filtered'))
print(p.is_absolute())
print(Path('..').resolve())
# Only works with subpaths, so OS example doesn't work :(
print(Path('/foo/Source').relative_to('/foo'))
print(p.exists())
print(p.is_file())
print(p.is_dir())
print(p.stat().st_size)
open("foo.txt", "w")
print(Path('foo.txt').unlink())
print(Path('database').mkdir())
print(Path('database').rmdir())
for files in Path(p / 'data' / 'database').iterdir(): # Same with regex '*' below,
    print(f'Current folder is {files}')
for files in Path(p / 'data' / 'database').glob('**'): # BFS compared os, '**' only dirs pre-order
    print(f'Current folder is {files.name}, relative path {files}')

# The 'os.linesep' is used when you want to iterate through the lines of a text file. The internal scanner recognises
# the 'os.linesep' and replaces it by a single '\n'. Below we're writing, so we can set the newline to be the encoded
# Windows newline '\r\n' and then to see it worked, we have to read it in binary because we want to see the encoded
# '\r\n', if we just used 'r' then it'd only show '\n'
with open("demo", mode="w", newline="\r\n") as file:
    file.write("one\ntwo\nthree\n")
with open("demo", mode="rb") as file:
    print(repr(file.read()))