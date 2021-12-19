import requests
import time
import threading
from threading import *
img_names = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03'
]
t1 = time.perf_counter()

print("Download started in serial computation")
for img_url in img_names:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

t2 = time.perf_counter()

print(f'Downloaded in serial and Finished in {t2-t1} seconds')

s = time.perf_counter()

print("Download started in parallel computation")
def first():
    url = img_names[0]
    files=requests.get(url)
    with open("img1.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

def first2():
    url = img_names[1]
    files=requests.get(url)
    with open(f"img 2.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

def first3():
    url = img_names[2]
    files=requests.get(url)
    with open("img 3.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

def first4():
    url = img_names[3]
    files=requests.get(url)
    with open("img 4.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

def first5():
    url = img_names[4]
    files=requests.get(url)
    with open("img 5.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

def first6():
    url = img_names[5]
    files=requests.get(url)
    with open("img 6.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

def first7():
    url = img_names[6]
    files=requests.get(url)
    with open(f"img 7.jpg",'wb') as file:
        file.write(files.content)
        print("Photo was downloaded....")

t1=Thread(target=first)
t2=Thread(target=first2)
t3=Thread(target=first3)
t4=Thread(target=first4)
t5=Thread(target=first5)
t6=Thread(target=first6)
t7=Thread(target=first7)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t7.join()
t6.join()
t5.join()
t4.join()
t3.join()
t2.join()
t1.join()

f = time.perf_counter()
print(f"Downloaded in prallel and Fineshed in {round(f-s, 2)} second(s)")