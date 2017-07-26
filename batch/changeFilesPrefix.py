#! python

from os import rename, listdir

oldprefix = "ke"
fnames = listdir('.')

for fname in fnames:
    if fname.startswith(oldprefix):
        rename(fname, fname.replace(oldprefix, 'x', 1))
