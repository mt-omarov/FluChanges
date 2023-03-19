from Bio import SeqIO
import re, os, pandas as pd
import textwrap
import sqlite3

encoding = 'utf-8' 
directory = os.fsencode("input_files")
sqliteConnection = sqlite3.connect('fastaSeq.db')

def GetCities():
    cities = dict()
    csv_cities = pd.read_csv("worldcities.csv")

    # record = SeqIO.parse("structured_files/iav_h3n2/HA.fasta", "fasta")
    # print(record.id[:record.id.index("/")])
    # print(csv_cities.loc[csv_cities['city'] == 'Tokyo']['country'])




def StructureQualifier():
    for file in os.listdir(directory):
        filename = os.fsencode(file)
        filepath = os.path.join(directory, filename)
        records = dict()

        for record in SeqIO.parse(filepath, "fasta"):
            headline = record.id
            parts = re.split('=', headline)
            if len(parts) == 17:
            # it means, that parts[12] == segment name;
                segment = parts[12]
                segment_id = parts[0][parts[0].find('/')+1:]
            
                if segment in records:
                    records[segment][segment_id] = record.seq
                else:
                    records[segment] = dict()
                    records[segment][segment_id] = record.seq
                    # we collect out seqs in data structute 'records{flu_segment : {record_id : seq}}'
            else:
                if len(parts) in records:
                    records[len(parts)][headline] = record
                else:
                    records[len(parts)] = dict()
                    records[len(parts)][headline] = record

        foldername = os.path.splitext(filename)[0].decode(encoding)
        if not os.path.exists(f"structured_files/{foldername}"):
            os.makedirs(f"structured_files/{foldername}")
            # we create a new folder for flu output files
        for key in records:
            with open(f'structured_files/{foldername}/{key}.fasta','w+') as f:
                for id in records[key]:
                    seq = textwrap.fill(str(records[key][id]), width=100)
                    f.write(f'>{id}\n{seq}\n')
        
        # if not os.path.exists(f"structured_files_temp/{foldername}"):
        #     os.makedirs(f"structured_files_temp/{foldername}")

        # for key in records:
        #     with open(f'structured_files_temp/{foldername}/{key}.fasta','w+') as f:
        #         for id in records[key]:
        #             SeqIO.write(records[key][id], f, "fasta")

# def Temp():
    

# GetCities()
# StructureQualifier()