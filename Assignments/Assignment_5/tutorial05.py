import os
import re

home = r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment5'

def rename_FIR(folder_name):
    padding = int(input('Enter the padding of the Episode Number\n'))
    os.chdir('Subtitles')
    for file in os.listdir(folder_name):
        ep_nos = re.findall(r'(?:Episode|Ep)\s*(\d+)', file)
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
    season_padding = int(input("Enter the season number padding...\n"))
    episode_padding = int(input('Enter the episode number padding...\n'))
    os.chdir('Subtitles')
    for file in os.listdir(folder_name):
        season, ep_no, ep_name = re.findall(r'(\d+)(?:\D+)(\d+)\W*([^\.]+)', file)[0]
        extension = re.search(r'\.mp4|\.srt', file).group()
        season = season.lstrip('0')
        ep_no = ep_no.lstrip('0')
        new_filename = folder_name + ' - Season ' + '0'*(season_padding - len(season)) + season + ' Episode ' + '0'*(episode_padding - len(ep_no)) + ep_no + ' - ' + ep_name + extension
        try:
            os.rename(os.path.join(folder_name, file), os.path.join(folder_name, new_filename))
        except FileExistsError:
            os.remove(os.path.join(folder_name, file))
    

def rename_Sherlock(folder_name):
    season_padding = int(input("Enter the season number padding...\n"))
    episode_padding = int(input('Enter the episode number padding...\n'))
    os.chdir('Subtitles')
    for file in os.listdir(folder_name):
        season, ep_no = re.findall(r'(?:S\w*)\s*(\d+)\W*(?:E\w*)\s*(\d+)', file)[0]
        extension = re.search(r'\.mp4|\.srt', file).group()
        season = season.lstrip('0')
        ep_no = ep_no.lstrip('0')
        new_filename = folder_name + ' - Season ' + '0'*(season_padding - len(season)) + season + ' Episode ' + '0'*(episode_padding - len(ep_no)) + ep_no + extension
        try:
            os.rename(os.path.join(folder_name, file), os.path.join(folder_name, new_filename))
        except FileExistsError:
            os.remove(os.path.join(folder_name, file))
    

def rename_Suits(folder_name):
    season_padding = int(input("Enter the season number padding...\n"))
    episode_padding = int(input('Enter the episode number padding...\n'))
    os.chdir('Subtitles')
    for file in os.listdir(folder_name):
        season, ep_no, ep_name = re.findall(r'(\d+)(?:\D+)(\d+)\W*([^\.]+)', file)[0]
        extension = re.search(r'\.mp4|\.srt', file).group()
        season = season.lstrip('0')
        ep_no = ep_no.lstrip('0')
        new_filename = folder_name + ' - Season ' + '0'*(season_padding - len(season)) + season + ' Episode ' + '0'*(episode_padding - len(ep_no)) + ep_no + ' - ' + ep_name + extension
        try:
            os.rename(os.path.join(folder_name, file), os.path.join(folder_name, new_filename))
        except FileExistsError:
            os.remove(os.path.join(folder_name, file))
    

def rename_How_I_Met_Your_Mother(folder_name):
    season_padding = int(input("Enter the season number padding...\n"))
    episode_padding = int(input('Enter the episode number padding...\n'))
    os.chdir('Subtitles')
    for file in os.listdir(folder_name):
        match_list = re.findall(r'(\d+)(?:\D+)(\d+)\W*(.+?)(?:\.720p|\.HDTV|\.en|\.1080p|\.fov)', file, re.IGNORECASE)
        if not match_list:
            match_list = re.findall(r'(\d+)\D+(\d+)\W*(.+)(?:\.mp4|\.srt)', file)
        extension = re.search(r'\.mp4|\.srt', file).group()
        season = match_list[0][0].lstrip('0')
        ep_no = match_list[0][1].lstrip('0')
        ep_name = match_list[0][2].strip()
        new_filename = folder_name + ' - Season ' + '0'*(season_padding - len(season)) + season + ' Episode ' + '0'*(episode_padding - len(ep_no)) + ep_no + ' - ' + ep_name + extension
        try:
            os.rename(os.path.join(folder_name, file), os.path.join(folder_name, new_filename))
        except FileExistsError:
            os.remove(os.path.join(folder_name, file))


print('Enter the number correspoding to the Web Series..')
print("1. FIR\n2. Game of Thrones\n3. Sherlock\n4. Suits\n5. How I Met Your Mother")
inp = input()
if inp == '1':
    rename_FIR('FIR')
elif inp == '2':
    rename_Game_of_Thrones('Game of Thrones')
elif inp == '3':
    rename_Sherlock('Sherlock')
elif inp == '4':
    rename_Suits('Suits')
elif inp == '5':
    rename_How_I_Met_Your_Mother('How I Met Your Mother')