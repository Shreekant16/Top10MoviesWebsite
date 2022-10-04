from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://editorial.rottentomatoes.com/guide/popular-movies/")


soup = BeautifulSoup(response.content, 'lxml')
names = soup.find_all('div', {'class':'article_movie_title'})
description = soup.find_all('div', {'class': 'row countdown-item-details'})
images = ['https://resizing.flixster.com/DsEf7MQy00zMCZMJ0IrbPaJ9mPg=/fit-in/180x240/v2/https://resizing.flixster.com/PhdCnJ_2CL5VsLUAQHS6heKxDYo=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzYyY2Y1OThhLTNkZjYtNDMyMS05NGM3LWI1ZTFlYTY4MzU2OS5qcGc=',
          'https://resizing.flixster.com/YEz-TCOWjcRUsx13iOkR4Deo3aw=/fit-in/180x240/v2/https://resizing.flixster.com/6Ce6e_0XkidJuYJN0kCXykPDezo=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2M2ODA3YzkwLWYyM2MtNGFhYS04MGViLTYzN2ZhYWIyYmU1Yi5qcGc=',
          'https://resizing.flixster.com/WEXirzMc5Cn4UIVQo-EzjmX-YsQ=/fit-in/180x240/v2/https://resizing.flixster.com/nQnxy2UKVyzDnmtkw4Of55iOaDY=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzJlMmI1YWM4LWIyYmYtNDMzOC1iMzJhLWU4MzM2MmYwNmQ1NS5qcGc=',
          'https://resizing.flixster.com/yfRxmeFA5-rad8yCZqOHSvoqLWg=/fit-in/180x240/v2/https://resizing.flixster.com/dX60R1nXMJfzdK6j2at14tigHPc=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2JiMmM0MTExLWYwMTUtNDBhYy1hZmY5LTQ3Yjc1ODM1ZDA4OS5qcGc=',
          'https://resizing.flixster.com/lHvMuR2gj87UAiLoABFQ2oIMn4M=/fit-in/180x240/v2/https://resizing.flixster.com/AYB9OnYW72piM-dTh56P5tkuhMI=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2ZhOWFiYTQ2LWYxODUtNDU2OS1hNjY5LTRlOTlkYjA2NmVlZC5qcGc=',
          'https://resizing.flixster.com/XMmhnBXRpZcV5ux1G8DwsSDiG2M=/fit-in/180x240/v2/https://resizing.flixster.com/BwXaeEZJNNzzduc8EaebjKl2aGc=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzY4YTIwMGI3LTk1YjUtNDY1ZC1hYmMyLTIwM2UwZjc2OTY4Mi5qcGc=',
          'https://resizing.flixster.com/CrF-V8Q3D_pBSPjFJmCGCzE_md0=/fit-in/180x240/v2/https://resizing.flixster.com/xAE4GIkcbO4u4FKreqMguDTdDl8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2ZmMTk0ZDFkLTY5NGEtNDIxZC04ZTVjLTY5MmEyNzUyNzQ4MS5qcGc=',
          'https://resizing.flixster.com/LpeNGUD_abNHfGsTppuz-Z1w9qU=/fit-in/180x240/v2/https://resizing.flixster.com/i0LGVXf_j-QlrVGCf4EQui7tyAc=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzZiZjQ0N2Y2LWI4MmQtNDZmNC1iZjRlLWQ2NDUwOTcwNzZhZi5qcGc=',
          'https://resizing.flixster.com/y6e98fOAzyKK1U_2NgOQGisVv-E=/fit-in/180x240/v2/https://resizing.flixster.com/Ym6ucXdlZjGTqRWEMVr0r3H16Ro=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzA3ZGY2MjgxLTI1NjEtNGFhMC1iYzQ0LTllOGFhYTczNzYxNy5qcGc=',
          'https://resizing.flixster.com/ZT9xzhoAPtf4LB_i-i2Y3s4-yHo=/fit-in/180x240/v2/https://resizing.flixster.com/mN-iX29W83cQRf8_HssTQgGcFAk=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzY3OGI4YzVhLWYxNzEtNGM0YS05OTM5LWI0M2NiODllNDRkNC5wbmc=',
          'https://resizing.flixster.com/CvinnVABtVo7p-3d7rxxXdsJwiI=/fit-in/240x240/v2/https://resizing.flixster.com/0Wuqfdlk2B3QUnrB7wPlQ7c47AI=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzI3OTIwZDU1LTEwNmQtNGYwZS1iNjhlLTIwNmU0MjdiYmY2MS5qcGc=']

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', x=names, y=description, z=images)

if __name__ == '__main__':
    app.run(debug=True)