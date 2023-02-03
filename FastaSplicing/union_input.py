import zipfile, os, shutil
from Bio import SeqIO

encoding = 'utf-8' 
DIR = os.fsencode("zips")

def UnZipping():
    for zip in os.listdir(DIR):
        zipname = os.fsencode(zip)
        zippath = os.path.join(DIR, zipname).decode(encoding)

        with zipfile.ZipFile(zippath, mode='r') as archive:
            zipname = os.path.splitext(zipname)[0].decode(encoding)
            archive.extractall(f"zips/{zipname}")

def Union():
    for dir in os.listdir(DIR):
        dirname = os.fsencode(dir)
        pathdir = os.path.join(DIR, dirname)

        if os.path.isdir(pathdir):
            with open(f'input_files/{dirname.decode(encoding)}.fasta','w+') as f:
                for file in os.listdir(pathdir):
                    for record in SeqIO.parse(os.path.join(pathdir, os.fsencode(file)), "fasta"):
                        f.write(f'>{record.id}\n{record.seq}\n')
