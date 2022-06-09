import os

def face_rec(name:str):
    directory = 'images/'
    for filename in os.listdir(directory):
        f = os.path.join(directory,filename)
        if os.path.isfile(f):
            basename = os.path.basename(f)
            (filename,ext) = os.path.splitext(basename)
            if filename == name:
                return 'Present'
    return 'Absent'