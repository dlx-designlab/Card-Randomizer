import glob
import os

#pathを指定する場合
#path = './app/static/image/rammojammo_cards'
#files = glob.glob(path +'/*.jpg')

#ディレクトリ直下に置く場合
files = glob.glob('*.jpg')

for i, old_name in enumerate(files):
    new_name = "card-{0:01d}.jpg".format(i + 1)
    os.rename(old_name, new_name)