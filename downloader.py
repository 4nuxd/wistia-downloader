""# Wistia Video Downloader
# Author: 4nuxd
# Version: 1.0.0
# Dependencies: requests, re, os, colorama, tqdm

import requests
import re
import os
from colorama import *
from tqdm import tqdm

init()

merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
banner = f"""
{putih}███╗   ██╗ ██████╗  ██████╗ ██████╗   {putih}A Wistia Video{hijau} Downloader  
████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗  {hijau}Version: {putih}v 1.0.0
██╔██╗ ██║██║   ██║██║   ██║██████╔╝  {putih}Author: {hijau}4nuxd
██║╚██╗██║██║   ██║██║   ██║██╔══██╗  {hijau}Note: {putih}Every Action Has a Consequence
██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝  {putih}Join: {hijau}https://github.com/4nuxd/
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝   {hijau}Bored..? : {putih}http://bit.ly/3MTMHyU
___________________________________________________________________________
    {reset}"""

def get_wistia_video_url(video_id):
    embed_url = f"http://fast.wistia.net/embed/iframe/{video_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(embed_url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch embed page")
        return None
    
    match = re.search(r'"url":"(http[^"]+?)"', response.text)
    if match:
        video_url = match.group(1).replace("\\", "")
        return video_url
    else:
        print("Video URL not found in page source")
        return None

def download_video(video_url, video_id, file_name):
    video_path = f"{file_name}.mp4"
    
    response = requests.get(video_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    if response.status_code == 200:
        with open(video_path, 'wb') as file, tqdm(
            desc=video_path,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                bar.update(len(chunk))
        print(f"\nDownload complete: {video_path}")
        return video_path
    else:
        print("Failed to download video")
        return None

def main():
    clear()
    print(banner)
    video_id = input("Enter Wistia Video ID: ")
    file_name = input("Enter file name to save as (without extension): ")
    video_url = get_wistia_video_url(video_id)
    if video_url:
        print(f"Video URL: {video_url}")
        video_path = download_video(video_url, video_id, file_name)
    else:
        print("Could not retrieve video URL")

if __name__ == "__main__":
    main()
""
