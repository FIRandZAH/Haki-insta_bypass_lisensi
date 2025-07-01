import requests,os
try:
    from tqdm import tqdm
except ImportError:
    os.system("pip install tqdm")
os.system("pkg install unzip")
def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as file, tqdm(
        desc=f"Downloading {filename}",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        ncols=80
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))

def utama():
    url1 = 'https://github.com/FIRandZAH/Haki_main/raw/refs/heads/main/part1.zip'
    url2 = url1.replace('part1', 'part2')
    download_file(url1, 'part1.zip')
    os.system("unzip -o part1.zip")
    download_file(url2, 'part2.zip')
    os.system("unzip -o part2.zip")
    os.system("python firzah1.py")
    os.system("python compile.py")
utama()
