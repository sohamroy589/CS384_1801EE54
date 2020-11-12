import os
import re

home = r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment5'

def rename_FIR(folder_name):
    padding = int(input('Enter the padding of the Episode Number\n'))
    os.chdir('Subtitles')
    for file in os.listdir(folder_name):
        ep_nos = re.findall(r'(?:Episode|Ep)\s+(\d+)', file)
        extension = re.search(r'\.mp4|\.srt', file).group()
        if not ep_nos:
            return
        ep_no = ep_nos[0].lstrip('0')
        new_filename =folder_name + ' - Episode ' + '0'*(padding - len(ep_no)) + ep_no + extension
        try:
            os.rename(os.path.join(folder_name,file), os.path.join(folder_name,new_filename))
        except FileExistsError:
            os.remove(os.path.join(folder_name,file))
    

def rename_Game_of_Thrones(folder_name):
    # rename Logic 
    pass
    

def rename_Sherlock(folder_name):
    # rename Logic 
    pass
    

def rename_Suits(folder_name):
    # rename Logic 
    pass
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    pass
    

if __name__ == '__main__':
    folder = input('Enter the full name of the Web Series..').strip()
    if folder == 'FIR':
        rename_FIR(folder)